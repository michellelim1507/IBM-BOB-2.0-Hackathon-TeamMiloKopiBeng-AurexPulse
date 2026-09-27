from flask import Flask, jsonify, request, send_from_directory, Response
from pathlib import Path
import os
import re
import shutil
import subprocess
import sys

from scanner import scan_project
from project_detector import detect_project
from code_analyzer import analyze_code
from optimization_task import create_tasks
from bob_prompt import generate_bob_prompt
from bob_bridge import save_bob_task
from emergency_room.orchestrator import run_emergency_room

BASE = Path(__file__).resolve().parent
WORKSPACE = BASE / "workspace"
WEB = BASE

app = Flask(__name__)
WORKSPACE.mkdir(exist_ok=True)

def valid_github(url):
    return re.match(r"^https://github\.com/[^/\s]+/[^/\s]+(?:\.git)?/?$", url.strip()) is not None

def clone_repository(url):
    if not valid_github(url):
        raise ValueError("Please enter a public GitHub repository URL.")

    name = url.rstrip("/").split("/")[-1]
    if name.endswith(".git"):
        name = name[:-4]

    path = WORKSPACE / name
    if path.exists():
        return name, path, "existing"

    result = subprocess.run(
        ["git", "clone", "--depth", "1", url, str(path)],
        capture_output=True,
        text=True,
        timeout=180
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "Git clone failed.")
    return name, path, "cloned"

def issue_json(issue, project_path):
    return {
        "severity": issue[0],
        "description": issue[1],
        "file": os.path.relpath(issue[2], project_path),
        "line": issue[3]
    }

@app.route("/")
def home():
    return serve_html("homepage.html")

@app.route("/homepage.html")
def homepage():
    return serve_html("homepage.html")

@app.route("/analysisPage.html")
def analysis_page():
    return serve_html("analysisPage.html")

def serve_html(filename):
    path = WEB / filename
    original = path.read_text(encoding="utf-8")
    # The original frontend file is not edited. This bridge is appended only to
    # the HTTP response so the existing UI remains pixel/source unchanged.
    html = original.replace("</body>", '<script src="/aurexpulse-web-bridge.js"></script></body>')
    return Response(html, mimetype="text/html")

@app.get("/aurexpulse-web-bridge.js")
def bridge():
    return send_from_directory(WEB, "aurexpulse-web-bridge.js", mimetype="application/javascript")

@app.post("/api/analyze")
def api_analyze():
    data = request.get_json(silent=True) or {}
    url = str(data.get("repository", "")).strip()
    try:
        name, path, state = clone_repository(url)
        files = scan_project(str(path))
        detected = detect_project(str(path))
        issues = analyze_code(str(path))
        return jsonify({
            "ok": True,
            "project": name,
            "project_path": str(path),
            "repository": url,
            "state": state,
            "files": len(files),
            "detected": detected,
            "issues": [issue_json(i, str(path)) for i in issues],
            "counts": {
                "python": sum(x.endswith(".py") for x in files),
                "javascript": sum(x.endswith(".js") for x in files),
                "html": sum(x.endswith(".html") for x in files),
                "css": sum(x.endswith(".css") for x in files)
            }
        })
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 400

@app.post("/api/emergency")
def api_emergency():
    data = request.get_json(silent=True) or {}
    issue = data.get("issue") or {}
    project_path = data.get("project_path")
    if not project_path:
        return jsonify({"ok": False, "error": "Project path is missing."}), 400

    abs_file = Path(project_path) / issue.get("file", "")
    selected = [
        issue.get("severity", "LOW"),
        issue.get("description", ""),
        str(abs_file),
        int(issue.get("line", 0))
    ]
    try:
        result = run_emergency_room(selected)
        if result is None:
            return jsonify({"ok": False, "error": "Emergency Room returned no result."}), 500
        return jsonify({
            "ok": True,
            "result": {
                "department": result[0],
                "issue": result[1],
                "file": os.path.relpath(result[2], project_path),
                "line": result[3],
                "recommendation": result[4]
            }
        })
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500

@app.post("/api/bob")
def api_bob():
    data = request.get_json(silent=True) or {}
    issue = data.get("issue") or {}
    project_path = data.get("project_path")
    if not project_path:
        return jsonify({"ok": False, "error": "Project path is missing."}), 400

    abs_file = Path(project_path) / issue.get("file", "")
    selected = [
        issue.get("severity", "LOW"),
        issue.get("description", ""),
        str(abs_file),
        int(issue.get("line", 0))
    ]
    try:
        prompt = generate_bob_prompt(selected, project_path)
        output = save_bob_task(selected, prompt, project_path)
        return jsonify({"ok": True, "prompt": prompt, "file": output})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500

@app.get("/api/health")
def health():
    return jsonify({"ok": True, "service": "AurexPulse Web App"})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

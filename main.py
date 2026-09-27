import os
import subprocess

from scanner import analyze_project
from project_detector import detect_project
from code_analyzer import analyze_code, display_issues
from risk_report import generate_risk_report
from optimization_task import create_tasks, display_tasks
from task_manager import select_task
from bob_prompt import generate_bob_prompt, display_bob_prompt
from bob_bridge import save_bob_task
from emergency_room.orchestrator import run_emergency_room


print("==============================")
print("        AUREXPULSE")
print("==============================")


repository_url = input("Enter GitHub Repository URL: ")

project_name = repository_url.rstrip("/").split("/")[-1]

if project_name.endswith(".git"):
    project_name = project_name[:-4]


workspace = "workspace"

if not os.path.exists(workspace):
    os.makedirs(workspace)


project_path = os.path.join(workspace, project_name)


print("\n[1] Repository received:")
print(repository_url)


if os.path.exists(project_path):

    print("\n[2] Checking repository...")
    print("\n[✓] Repository already exists.")
    print(f"[✓] Using existing project: {project_path}")

else:

    print("\n[2] Cloning repository...")

    result = subprocess.run(
        ["git", "clone", repository_url, project_path],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:

        print("\n[✗] Failed to clone repository.")
        print(result.stderr)

        exit()

    print("\n[✓] Repository cloned successfully!")
    print(f"[✓] Project: {project_name}")
    print(f"[✓] Location: {project_path}")


analyze_project(project_path)


detected = detect_project(project_path)

print("\n==============================")
print("      PROJECT OVERVIEW")
print("==============================")

for item in detected:
    print(f"[✓] {item}")

print("\n[✓] Project understanding completed.")

issues = analyze_code(project_path)
display_issues(issues)
generate_risk_report(issues)
tasks = create_tasks(issues)
display_tasks(tasks)
selected_task = select_task(tasks)

if selected_task is not None:

    if selected_task[0] == "HIGH":

        print("\n[!] HIGH-RISK ISSUE DETECTED")
        print("[→] Sending task to Emergency Room...")

        emergency_result = run_emergency_room(selected_task)

        

    else:

        print("\n[✓] Normal optimization task.")

    bob_prompt = generate_bob_prompt(
        selected_task,
        project_path
    )

    display_bob_prompt(bob_prompt)

    save_bob_task(
        selected_task,
        bob_prompt,
        project_path
    )
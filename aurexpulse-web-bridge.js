(() => {
  let lastAnalysis = null;

  function addFeed(text, type = "info") {
    const feed = document.getElementById("diagFeed");
    if (!feed) return;
    const line = document.createElement("div");
    line.className = "feed-line " + type;
    line.textContent = text;
    feed.appendChild(line);
    feed.scrollTop = feed.scrollHeight;
  }

  function escapeHtml(value) {
    return String(value ?? "").replace(/[&<>"']/g, c => ({
      "&":"&amp;", "<":"&lt;", ">":"&gt;", '"':"&quot;", "'":"&#039;"
    }[c]));
  }

  function issueToAbsolute(issue) {
    return issue;
  }

  async function analyzeRepository(url) {
    addFeed("[SCAN] Connecting to AurexPulse backend...", "info");
    const response = await fetch("/api/analyze", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({repository: url})
    });
    const data = await response.json();
    if (!data.ok) throw new Error(data.error || "Analysis failed.");
    lastAnalysis = data;

    addFeed("[OK] Repository: " + data.project, "ok");
    addFeed("[SCAN] " + data.files + " files indexed.", "info");
    data.detected.forEach(x => addFeed("[OK] Detected: " + x, "ok"));
    data.issues.forEach(x => addFeed(
      "[" + x.severity + "] " + x.description + " — " + x.file + ":" + x.line,
      x.severity === "HIGH" ? "warn" : "info"
    ));

    const high = data.issues.filter(x => x.severity === "HIGH").length;
    addFeed("[OK] Analysis complete. " + data.issues.length + " issue(s), " + high + " high-risk.", "ok");
    renderDynamicPanels();
    return data;
  }

  function renderDynamicPanels() {
    if (!lastAnalysis) return;

    const securityBody = document.querySelector("#winSec .win-body");
    if (securityBody) {
      const high = lastAnalysis.issues.filter(x => x.severity === "HIGH");
      const med = lastAnalysis.issues.filter(x => x.severity === "MEDIUM");
      const low = lastAnalysis.issues.filter(x => x.severity === "LOW");
      securityBody.innerHTML = `
        <div class="sec-item"><span>High-risk findings</span><span class="badge ${high.length ? "warn":""}">${high.length}</span></div>
        <div class="sec-item"><span>Medium-risk findings</span><span class="badge">${med.length}</span></div>
        <div class="sec-item"><span>Low-risk findings</span><span class="badge">${low.length}</span></div>
        <div class="sec-item"><span>Repository files</span><span class="badge">${lastAnalysis.files}</span></div>
        <button class="btn-block" id="backendSecurityScan">RUN FULL SECURITY SCAN</button>
        <p style="font-size:10px;color:var(--muted);margin:8px 0 0;text-align:center;">Live result from the AurexPulse scanner.</p>`;
      document.getElementById("backendSecurityScan").onclick = () => {
        addFeed("[SECURITY] Full scan requested.", "info");
        high.length ? addFeed("[WARN] " + high.length + " high-risk finding(s) require investigation.", "warn")
                    : addFeed("[OK] No high-risk findings detected.", "ok");
      };
    }

    const emgBody = document.querySelector("#winEmg .win-body");
    if (emgBody) {
      const high = lastAnalysis.issues.filter(x => x.severity === "HIGH");
      emgBody.innerHTML = "";
      if (!high.length) {
        emgBody.innerHTML = '<div class="emg-item"><span class="emg-tag med">CLEAR</span><span>No high-risk incidents detected.</span></div>';
      } else {
        high.forEach((issue, index) => {
          const row = document.createElement("div");
          row.className = "emg-item";
          row.innerHTML = `<span class="emg-tag critical">HIGH</span><span>${escapeHtml(issue.description)} — ${escapeHtml(issue.file)}:${issue.line}</span>`;
          emgBody.appendChild(row);

          const actions = document.createElement("div");
          actions.className = "emg-actions";
          ["Triage", "Diagnose", "Bob Task"].forEach(action => {
            const btn = document.createElement("button");
            btn.textContent = action;
            btn.onclick = () => handleEmergency(issue, action);
            actions.appendChild(btn);
          });
          emgBody.appendChild(actions);
        });
      }
    }
  }

  async function handleEmergency(issue, action) {
    addFeed("[EMERGENCY] " + action + " → " + issue.description, "warn");
    if (action === "Bob Task") {
      await createBobTask(issue);
      return;
    }

    try {
      const response = await fetch("/api/emergency", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({issue, project_path: lastAnalysis.project_path})
      });
      const data = await response.json();
      if (!data.ok) throw new Error(data.error || "Emergency Room failed.");

      addFeed("[ER] " + data.result.department + " investigation complete.", "ok");
      addChat("Emergency Room: " + data.result.recommendation);
    } catch (e) {
      addFeed("[ER ERROR] " + e.message, "warn");
    }
  }

  async function createBobTask(issue) {
    try {
      const response = await fetch("/api/bob", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({issue, project_path: lastAnalysis.project_path})
      });
      const data = await response.json();
      if (!data.ok) throw new Error(data.error || "Bob task generation failed.");
      addFeed("[BOB] Optimization task generated.", "ok");
      addChat("Bob task generated and saved to: " + data.file);
      window.__aurexBobPrompt = data.prompt;
    } catch (e) {
      addFeed("[BOB ERROR] " + e.message, "warn");
    }
  }

  function addChat(text) {
    const log = document.getElementById("chatLog");
    if (!log) return;
    const msg = document.createElement("div");
    msg.className = "msg bot";
    msg.innerHTML = '<span class="tag">AUREXPULSE</span><div>' + escapeHtml(text) + '</div>';
    log.appendChild(msg);
    log.scrollTop = log.scrollHeight;
  }

  // Replace only the behavior of the existing frontend function.
  // No HTML/CSS/layout is changed.
  window.scanRepo = async function() {
    const input = document.getElementById("repoUrl");
    const url = input ? input.value.trim() : "";
    if (!url) return;
    try {
      await analyzeRepository(url);
    } catch (e) {
      addFeed("[ERROR] " + e.message, "warn");
    }
  };

  window.runScan = async function() {
    if (!lastAnalysis) {
      addFeed("[SECURITY] Analyze a repository first.", "warn");
      return;
    }
    renderDynamicPanels();
    addFeed("[SECURITY] Live security scan complete.", "ok");
  };

  window.runAutoFix = async function() {
    if (!lastAnalysis) {
      addFeed("[EMERGENCY] Analyze a repository first.", "warn");
      return;
    }
    const high = lastAnalysis.issues.filter(x => x.severity === "HIGH");
    if (!high.length) {
      addFeed("[EMERGENCY] No high-risk task available for Bob.", "ok");
      return;
    }
    await createBobTask(high[0]);
  };

  window.addEventListener("DOMContentLoaded", () => {
    // Keep all existing frontend elements, interactions and styling intact.
    const repo = document.getElementById("repoUrl");
    if (repo) {
      repo.addEventListener("keydown", e => {
        if (e.key === "Enter") window.scanRepo();
      });
    }
  });
})();

# IBM BOB 2.0 Hackathon-Team MiloKopiBeng-AurexPulse

AurexPulse
AI-powered code intelligence and security platform built with IBM Bob 2.0 to detect, diagnose, and resolve software issues before they become emergencies.
AurexPulse is a code intelligence and security platform built with IBM Bob 2.0. It analyzes public GitHub repositories, identifies potential code issues, and guides developers from issue discovery to recommended next steps.

## Problem
A development team can spend hours tracking down problem across the project. The application runs, but somewhere in the repository is a possible hardcoded password, an outdated dependency, security risks or code that no longer matches the project requirements. Finding and understanding these issues takes time as developers still must understand where the issues are, how serious it is, and what to do next. 

## Solutions
![AurexPulse homepage](homepage.png)
This is the homepage of AurexPulse. We built AurexPulse with IBM Bob to help developers investigate the problem. It is designed for small teams working on projects they may not know inside out. The process starts with the user enters a URL and asking a code question or checking security risks of the project. They can explore code in Code Analysis, view possible risks in Security, and focus on urgent findings in the Emergency Room.

![Code analysis](codeanalysis.png)
On the left, developers can ask a question or choose an action such as detecting requirement conflicts. In the middle, they enter a GitHub repository URL to start a scan. On the right, the diagnostics feed shows what AurexPulse finds as it examines the project. It reads through every line of code, identifies backend and frontend files, flagged potential issues and points the developer to the code they need to inspect. The page helps the team move from an unfamiliar repository to a list of specific issues they can investigate and prioritize. 

![Security analysis](security.png)
The Security page scans the project to identify potential risks by severity and helps developers see which ones need attention first. It flags possible exposure of confidential information and displays the results of selected security-rule checks. Developers can then inspect each finding to determine whether there is a real security or compliance issue. 

![Emergency Room](emergencyroom.png)
Emergency Room brings the high-risk findings into one place so developers can investigate them first. Each finding shows where the suspected issue appears in the code and offers options to resolve it. This helps the team decide what needs action before release. In the planned workflow, specialized AI subagents will investigate the cause, propose a fix, and run a targeted test. The developer will review their findings and approve any code change. 

## What makes it unique? 

The idea behind AurexPulse is simple, an alert is useful only when developers know what to do with it. What makes it distinctive is the path from discovery to action, instead of leaving long lists of warnings, it connects each findings to the code and provides a clear step on how to resolve it. By connecting repository context, clear findings, and an investigation workflow, AurexPulse helps developers focus their limited time on the problems most likely to affect their release. Developers review the evidence and stay in control of any proposed code change. Our goal is to carry that process through to a targeted test, so the team can see whether an approved fix worked before shipping.

## IBM BOB Usage Statement
> **Example project:** The screenshots below show IBM Bob analyzing `flask-shop-master`, a separate sample Flask application. It is included only to demonstrate the analysis and remediation workflow; it is not part of AurexPulse.

<p align="center">
  <img src="docs/screenshots/tokenused.jpeg" alt="IBM Bob task context and usage" width="850">
</p>
Part 1 – AI-Powered Code Analysis: Task Context
![Token usage](docs/screenshots/tokenused.jpeg)
This screenshot shows the Bob task context used to analyse the Flask Shop workspace. The project consumed about 105.4k of the available context window, showing that Bob had access to a substantial amount of project information for code understanding. This stage supports AurexPulse’s AI-Powered Code Analysis by allowing the model to inspect the project as a whole instead of reviewing isolated files. It provides the foundation for identifying outdated code, understanding the project architecture, explaining the purpose of major components, and tracing the relationship between frontend, backend, and database logic.
<p align="center">
  <img src="docs/screenshots/tokenused.jpeg" alt="IBM Bob task context and usage" width="850">
</p>

Part 2 – Security: Privacy, Database and Remaining Risk Review
![Security Privacy, Database and Remaining Risk Review](docs/screenshots/Security%20Privacy%2C%20Database%20and%20Remaining%20Risk%20Review.jpeg)
This screenshot focuses on AurexPulse’s Security function. It shows secure-code improvements such as replacing random.choice with secrets.choice for reset tokens, replacing a removed inspection API, and updating deprecated logging. More importantly, Bob reports critical unresolved risks that require human action, including a committed RSA private key, a hardcoded application secret, exposed payment configuration, a default database password, an insufficiently protected test-payment route, and file-upload validation concerns. These findings demonstrate privacy-information leakage, user/database protection, credential security, and security-rule checking. Keeping unresolved risks visible also prevents automated fixes from creating a false impression that the project is completely secure.
<p align="center">
  <img src="docs/screenshots/Security%20Privacy%2C%20Database%20and%20Remaining%20Risk%20Review.jpeg" alt="Security, privacy, database, and remaining-risk review" width="850">
</p>

Part 3 – Emergency Room: Diagnosis and Auto Fix
![Emergency Room autofix](docs/screenshots/emergencyroomautofix.jpeg)
This screenshot demonstrates the AurexPulse Emergency Room workflow. Bob first explored the codebase and collected evidence before applying targeted fixes to confirmed problems. The visible changes include protection against an unsafe login redirect, while the task panel lists additional fixes such as an ownership check, stronger password-reset token generation, removal of deprecated code, and logging updates. This represents AI Diagnosis, AI Recommendation, and Auto Fix in one workflow. Bob also attempted to run tests; when the Python runtime was unavailable, it reported the limitation and performed static verification instead of claiming a successful runtime test.
<p align="center">
  <img src="docs/screenshots/emergencyroomautofix.jpeg" alt="Emergency Room diagnosis and autofix" width="850">
</p>

Parts 1, 2 and 3 – Architecture, Security Findings and Applied Fixes
![Architecture, Security Findings and Applied Fixes](docs/screenshots/Architecture%2C%20Security%20Findings%20and%20Applied%20Fixes.jpeg)
This screenshot connects all three AurexPulse areas. Bob summarizes the application architecture as a Flask and SQLAlchemy e-commerce system and describes the flow between templates, forms, the model layer, database, and optional caching. This supports frontend and backend understanding and explains how the code is structured. The same report identifies security weaknesses and prioritizes them by severity, including an open redirect, missing order ownership validation, a Python compatibility issue, weak reset-token generation, and a deprecated logging call. The table then records the corresponding changes, giving developers a clear diagnosis-to-fix trail.
<p align="center">
  <img src="docs/screenshots/Architecture%2C%20Security%20Findings%20and%20Applied%20Fixes.jpeg" alt="Architecture, security findings, and applied fixes" width="850">
</p>



## Features
- Analyze a public GitHub repository
- Detect project types and inspect source files
- Review potential code issues and generate a risk report
- Route high-risk issues through the Emergency Room workflow
- Generate optimization tasks and IBM Bob prompts

## Run locally
Requirements
- Python
- Git

## Setup
git clone https://github.com/michellelim1507/IBM-BOB-2.0-Hackathon-TeamMiloKopiBeng-AurexPulse.git

cd IBM-BOB-2.0-Hackathon-TeamMiloKopiBeng-AurexPulse

python -m venv .venv

## For Windows
.venv\Scripts\activate

## For macOS/Linux
source .venv/bin/activate

## Install dependencies and start the web app:
pip install -r requirements.txt

python webapp.py

Then open http://127.0.0.1:5000 in your browser.

To run the command-line workflow instead, use:

python main.py

## Project structure
- emergency_room/   # High-risk issue workflow
- main.py           # Command-line workflow
- webapp.py         # Flask web application
- analysisPage.html # Analysis page
- homepage.html     # Home page
- requirements.txt  # Python dependencies


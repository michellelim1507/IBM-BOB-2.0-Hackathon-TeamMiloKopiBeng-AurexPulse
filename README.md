# IBM BOB 2.0 Hackathon 
TeamMiloKopiBeng-AurexPulse

AurexPulse
AI-powered code intelligence and security platform built with IBM Bob 2.0 to detect, diagnose, and resolve software issues before they become emergencies.
AurexPulse is a code intelligence and security platform built with IBM Bob 2.0. It analyzes public GitHub repositories, identifies potential code issues, and guides developers from issue discovery to recommended next steps.

## Problem
A development team can spend hours tracking down problem across the project. The application runs, but somewhere in the repository is a possible hardcoded password, an outdated dependency, security risks or code that no longer matches the project requirements. Finding and understanding these issues takes time as developers still must understand where the issues are, how serious it is, and what to do next. 

## Solutions


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


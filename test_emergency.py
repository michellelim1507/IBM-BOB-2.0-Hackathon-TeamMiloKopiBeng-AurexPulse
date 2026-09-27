from emergency_room.orchestrator import run_emergency_room


print("\n========== TEST 1: SECURITY ==========")

security_issue = [
    "HIGH",
    "Possible hardcoded password",
    "flaskshop/settings.py",
    82
]

run_emergency_room(security_issue)


print("\n========== TEST 2: CODE ==========")

code_issue = [
    "MEDIUM",
    "Debug print found",
    "app.py",
    25
]

run_emergency_room(code_issue)


print("\n========== TEST 3: CONFLICT ==========")

conflict_issue = [
    "HIGH",
    "Merge conflict detected",
    "app.py",
    120
]

run_emergency_room(conflict_issue)
from emergency_room.triage_agent import triage_incident
from emergency_room.security_agent import investigate_security
from emergency_room.code_agent import investigate_code
from emergency_room.conflict_agent import investigate_conflict


def display_emergency_result(result):

    print("\n================================")
    print("       EMERGENCY RESULT")
    print("================================")

    if result is None:
        print("\n[✗] No investigation result.")
        return

    category = result[0]
    issue = result[1]
    file_path = result[2]
    line_number = result[3]
    recommendation = result[4]

    print(f"\nDepartment : {category}")
    print(f"Issue      : {issue}")
    print(f"File       : {file_path}")
    print(f"Line       : {line_number}")

    print("\nRecommendation:")
    print(recommendation)

    print("\n[✓] Emergency investigation completed.")


def run_emergency_room(issue):

    print("\n==============================")
    print("      EMERGENCY ROOM")
    print("==============================")

    print("\n[!] Incident received.")

    category = triage_incident(issue)

    print(f"[✓] Triage result: {category}")

    if category == "SECURITY":

        result = investigate_security(issue)

    elif category == "CONFLICT":

        result = investigate_conflict(issue)

    else:

        result = investigate_code(issue)

    display_emergency_result(result)

    return result
def generate_risk_report(issues):

    high = 0
    medium = 0
    low = 0

    for issue in issues:

        severity = issue[0]

        if severity == "HIGH":
            high += 1

        elif severity == "MEDIUM":
            medium += 1

        elif severity == "LOW":
            low += 1

    print("\n==============================")
    print("         RISK REPORT")
    print("==============================")

    print(f"\nHIGH RISK   : {high}")
    print(f"MEDIUM RISK : {medium}")
    print(f"LOW RISK    : {low}")

    total = high + medium + low

    print(f"\nTOTAL ISSUES: {total}")

    if high > 0:
        print("\n[!] High-risk issues require attention.")

    elif medium > 0:
        print("\n[!] Medium-risk issues detected.")

    else:
        print("\n[✓] No high-risk issues detected.")

    print("\n[✓] Risk report generated.")
    
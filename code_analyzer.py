import os


def analyze_code(project_path):

    issues = []

    for root, directories, filenames in os.walk(project_path):

        for filename in filenames:

            if not filename.endswith((".py", ".js", ".html", ".css")):
                continue

            file_path = os.path.join(root, filename)

            try:

                with open(
                    file_path,
                    "r",
                    encoding="utf-8",
                    errors="ignore"
                ) as file:

                    lines = file.readlines()

            except Exception:
                continue

            for line_number, line in enumerate(lines, start=1):

                # Detect debug prints
                if "print(" in line:

                    issues.append(
                        [
                            "LOW",
                            "Debug print detected",
                            file_path,
                            line_number
                        ]
                    )

                # Detect TODO comments
                if "TODO" in line.upper():

                    issues.append(
                        [
                            "LOW",
                            "TODO comment found",
                            file_path,
                            line_number
                        ]
                    )

                # Detect hardcoded passwords
                if "password =" in line.lower():

                    issues.append(
                        [
                            "HIGH",
                            "Possible hardcoded password",
                            file_path,
                            line_number
                        ]
                    )

    return issues


def display_issues(issues):

    print("\n==============================")
    print("       CODE ANALYSIS")
    print("==============================")

    if len(issues) == 0:

        print("\n[✓] No basic issues detected.")

        return

    print(f"\nPotential issues: {len(issues)}")

    for issue in issues:

        severity = issue[0]
        description = issue[1]
        file_path = issue[2]
        line_number = issue[3]

        print("\n------------------------------")

        print(f"Severity : {severity}")
        print(f"Issue    : {description}")
        print(f"File     : {file_path}")
        print(f"Line     : {line_number}")

    print("\n[✓] Code analysis completed.")
    
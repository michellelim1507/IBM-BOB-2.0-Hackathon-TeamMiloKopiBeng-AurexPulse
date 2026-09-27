import os


def scan_project(project_path):

    files = []

    for root, directories, filenames in os.walk(project_path):

        for filename in filenames:

            file_path = os.path.join(root, filename)

            relative_path = os.path.relpath(
                file_path,
                project_path
            )

            files.append(relative_path)

    return files


def analyze_project(project_path):

    files = scan_project(project_path)

    python_files = 0
    javascript_files = 0
    html_files = 0
    css_files = 0

    for file in files:

        if file.endswith(".py"):
            python_files += 1

        elif file.endswith(".js"):
            javascript_files += 1

        elif file.endswith(".html"):
            html_files += 1

        elif file.endswith(".css"):
            css_files += 1

    print("\n==============================")
    print("       PROJECT ANALYSIS")
    print("==============================")

    print(f"\nTotal files : {len(files)}")

    print(f"Python      : {python_files}")
    print(f"JavaScript  : {javascript_files}")
    print(f"HTML        : {html_files}")
    print(f"CSS         : {css_files}")

    print("\n[✓] Repository structure scanned.")
    print("[✓] Project is ready for deeper analysis.")

    print("\n[✓] Project scan completed.")
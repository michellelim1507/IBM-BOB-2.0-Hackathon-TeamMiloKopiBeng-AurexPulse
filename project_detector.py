import os


def detect_project(project_path):

    detected = []

    files = []

    for root, directories, filenames in os.walk(project_path):

        for filename in filenames:
            relative_path = os.path.relpath(
                os.path.join(root, filename),
                project_path
            )

            files.append(relative_path.lower())

    # Backend detection
    if any(file.endswith(".py") for file in files):
        detected.append("Python Backend")

    if any("flask" in file for file in files):
        detected.append("Flask")

    if any("requirements.txt" in file for file in files):
        detected.append("Python Dependencies")

    # Frontend detection
    if any(file.endswith(".html") for file in files):
        detected.append("HTML Frontend")

    if any(file.endswith(".css") for file in files):
        detected.append("CSS")

    if any(file.endswith(".js") for file in files):
        detected.append("JavaScript")

    # Database detection
    database_files = [
        "database.db",
        "database.sqlite",
        ".sql"
    ]

    for file in files:

        for database_file in database_files:

            if database_file in file:
                detected.append("Database")

    # Testing detection
    if any(
        "test" in file or "tests" in file
        for file in files
    ):
        detected.append("Testing")

    # Documentation
    if any("readme" in file for file in files):
        detected.append("Documentation")

    return detected
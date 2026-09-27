def investigate_code(issue):

    description = issue[1]
    file_path = issue[2]
    line_number = issue[3]

    return [
        "CODE",
        description,
        file_path,
        line_number,
        "Inspect the affected code and identify the root cause."
    ]
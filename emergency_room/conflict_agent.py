def investigate_conflict(issue):

    description = issue[1]
    file_path = issue[2]
    line_number = issue[3]

    return [
        "CONFLICT",
        description,
        file_path,
        line_number,
        "Inspect related components for integration or data conflicts."
    ]
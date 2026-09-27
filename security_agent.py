def investigate_security(issue):

    description = issue[1]
    file_path = issue[2]
    line_number = issue[3]

    description_lower = description.lower()

    if "password" in description_lower:

        recommendation = (
            "Check whether the password is hardcoded. "
            "If it is a real credential, move it to an environment variable "
            "or secure configuration."
        )

    elif "api key" in description_lower:

        recommendation = (
            "Check whether the API key is exposed in source code. "
            "Move sensitive credentials to environment variables "
            "or a secure secret store."
        )

    elif "secret" in description_lower:

        recommendation = (
            "Check whether a sensitive secret is stored directly "
            "in the source code."
        )

    elif "token" in description_lower:

        recommendation = (
            "Check whether the token is exposed in source code "
            "and move it to secure configuration."
        )

    elif "sql injection" in description_lower:

        recommendation = (
            "Inspect database queries and use parameterized queries "
            "to prevent SQL injection."
        )

    else:

        recommendation = (
            "Inspect the affected code for a genuine security issue."
        )

    return [
        "SECURITY",
        description,
        file_path,
        line_number,
        recommendation
    ]
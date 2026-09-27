def triage_incident(issue):

    description = issue[1].lower()

    if (
        "password" in description
        or "api key" in description
        or "secret" in description
        or "token" in description
        or "sql injection" in description
        or "security" in description
    ):
        return "SECURITY"

    elif (
        "conflict" in description
        or "merge conflict" in description
    ):
        return "CONFLICT"

    elif (
        "debug" in description
        or "code structure" in description
        or "poor code" in description
        or "duplicate" in description
    ):
        return "CODE"

    else:
        return "CODE"
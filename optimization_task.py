def create_tasks(issues):

    tasks = []

    for issue in issues:

        severity = issue[0]
        description = issue[1]
        file_path = issue[2]
        line_number = issue[3]

        task = [
            severity,
            description,
            file_path,
            line_number
        ]

        tasks.append(task)

    return tasks


def display_tasks(tasks):

    print("\n==============================")
    print("     OPTIMIZATION TASKS")
    print("==============================")

    if len(tasks) == 0:

        print("\n[✓] No optimization tasks generated.")

        return

    for index, task in enumerate(tasks, start=1):

        severity = task[0]
        description = task[1]
        file_path = task[2]
        line_number = task[3]

        print("\n------------------------------")

        print(f"Task       : #{index}")
        print(f"Priority   : {severity}")
        print(f"Problem    : {description}")
        print(f"File       : {file_path}")
        print(f"Line       : {line_number}")

    print("\n[✓] Optimization tasks generated.")
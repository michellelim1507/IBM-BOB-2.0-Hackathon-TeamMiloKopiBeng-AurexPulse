def select_task(tasks):

    if len(tasks) == 0:
        print("\n[✓] No tasks available.")
        return None

    print("\n==============================")
    print("      AUREXPULSE TASKS")
    print("==============================")

    for index, task in enumerate(tasks, start=1):

        severity = task[0]
        description = task[1]
        file_path = task[2]
        line_number = task[3]

        print(f"\n[{index}] {severity}")
        print(f"    Problem : {description}")
        print(f"    File    : {file_path}")
        print(f"    Line    : {line_number}")

    while True:

        choice = input("\nSelect task to optimize: ")

        if choice.isdigit():

            task_number = int(choice)

            if 1 <= task_number <= len(tasks):

                selected_task = tasks[task_number - 1]

                print("\n[✓] Task selected.")

                return selected_task

        print("[✗] Invalid task selection.")
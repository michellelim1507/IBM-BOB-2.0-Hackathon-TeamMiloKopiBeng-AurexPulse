import json
import os


def save_bob_task(task, prompt, project_path):

    bob_task = {
        "project": project_path,
        "priority": task[0],
        "problem": task[1],
        "file": task[2],
        "line": task[3],
        "prompt": prompt
    }

    output_path = os.path.join(
        project_path,
        "aurexpulse_bob_task.json"
    )

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            bob_task,
            file,
            indent=4
        )

    print("\n[✓] Bob task saved.")
    print(f"[✓] Task file: {output_path}")

    return output_path
def generate_bob_prompt(task, project_path):

    severity = task[0]
    description = task[1]
    file_path = task[2]
    line_number = task[3]

    prompt = f"""
You are working as a software optimization agent.

PROJECT:
{project_path}

TASK PRIORITY:
{severity}

PROBLEM:
{description}

TARGET FILE:
{file_path}

TARGET LINE:
{line_number}

OBJECTIVE:
Analyze the identified problem and implement an appropriate fix.

REQUIREMENTS:
1. Understand the existing code before making changes.
2. Modify only the files necessary to solve the problem.
3. Preserve existing application functionality.
4. Do not expose passwords, API keys, tokens, or other secrets.
5. Avoid introducing unrelated changes.
6. Follow the existing project's coding style.
7. Run relevant tests after making the changes.
8. Report what was changed and whether the tests passed.

EXPECTED RESULT:
The identified problem is resolved while the existing
application continues to function correctly.
"""

    return prompt


def display_bob_prompt(prompt):

    print("\n==============================")
    print("       BOB TASK PROMPT")
    print("==============================")

    print(prompt)

    print("[✓] Bob task generated.")
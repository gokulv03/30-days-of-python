import os

for i in range(1, 31):
    folder_name = f"day{i:02}"
    os.makedirs(folder_name, exist_ok=True)

    with open(os.path.join(folder_name, "notes.md"), "w") as f:
        f.write(f"# Day {i} Notes\n\nWhat I learned today:\n\n")

    with open(os.path.join(folder_name, "exercises.py"), "w") as f:
        f.write(f"# Day {i} Exercises\n\n# Your code here\n")

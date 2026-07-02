#!/usr/bin/env python3
import subprocess
import sys

def run_command(cmd):
    result = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    return result.returncode, result.stdout.strip(), result.stderr.strip()

def get_input(prompt, default=""):
    try:
        val = input(prompt).strip()
        return val if val else default
    except (KeyboardInterrupt, EOFError):
        print("\nOperation cancelled.")
        sys.exit(0)

def main():
    print("=" * 60)
    print("🚀 Git Conventional Commit Helper 🚀")
    print("=" * 60)

    # 1. Check git status
    code, stdout, stderr = run_command("git status -s")
    if code != 0:
        print(f"❌ Error running git status: {stderr}")
        sys.exit(1)
    
    if not stdout:
        print("✅ No modified or untracked files found. Nothing to commit!")
        sys.exit(0)

    print("\nModified/Untracked Files:")
    print(stdout)
    print("-" * 60)

    # 2. Select commit type
    types = [
        ("feat", "A new feature (e.g., feat: add linear regression metric)"),
        ("fix", "A bug fix (e.g., fix: resolve division-by-zero error)"),
        ("docs", "Documentation changes (e.g., docs: update README setup)"),
        ("style", "Formatting, visual elements, SVGs (e.g., style: redesign skills chart)"),
        ("refactor", "A code change that neither fixes a bug nor adds a feature"),
        ("test", "Adding or correcting tests (e.g., test: add validation test)"),
        ("chore", "Build tasks, dependencies, configs (e.g., chore: update requirements.txt)"),
    ]

    print("\nSelect the commit type:")
    for idx, (t, desc) in enumerate(types):
        print(f"  {idx + 1}) {t:<10} - {desc}")
    
    while True:
        choice = get_input("\nEnter number (1-7): ")
        if choice.isdigit() and 1 <= int(choice) <= len(types):
            commit_type = types[int(choice) - 1][0]
            break
        print("❌ Invalid input. Please enter a number between 1 and 7.")

    # 3. Enter optional scope
    scope = get_input("\nEnter optional scope (e.g., readme, model, dashboard) [Press Enter to skip]: ")
    scope_str = f"({scope})" if scope else ""

    # 4. Enter description
    while True:
        description = get_input("\nEnter short description (imperative mood, e.g., 'Add neural network baseline'): ")
        if description:
            break
        print("❌ Description is required!")

    # 5. Format commit message
    commit_msg = f"{commit_type}{scope_str}: {description}"
    print("\n" + "=" * 60)
    print("Formatted Commit Message:")
    print(f"\033[1;32m{commit_msg}\033[0m")
    print("=" * 60)

    # 6. Ask to stage files
    stage_choice = get_input("\nStage all modified files before committing? (y/n) [default: y]: ", "y").lower()
    if stage_choice == "y":
        code, stdout, stderr = run_command("git add .")
        if code != 0:
            print(f"❌ Error staging files: {stderr}")
            sys.exit(1)
        print("✅ Staged all files.")
    else:
        file_list = get_input("Enter files to stage individually (space-separated) or skip: ")
        if file_list:
            code, stdout, stderr = run_command(f"git add {file_list}")
            if code != 0:
                print(f"❌ Error staging files: {stderr}")
                sys.exit(1)
            print(f"✅ Staged: {file_list}")

    # 7. Confirm and execute commit
    commit_choice = get_input(f"\nExecute commit? (y/n) [default: y]: ", "y").lower()
    if commit_choice == "y":
        # Run commit command safely using git commit -m
        # Escape quotes in message to prevent shell command injection issues
        escaped_msg = commit_msg.replace('"', '\\"')
        code, stdout, stderr = run_command(f'git commit -m "{escaped_msg}"')
        if code != 0:
            print(f"❌ Error committing changes: {stderr}")
            sys.exit(1)
        print("\n🎉 Commit created successfully!")
        print(stdout)
    else:
        print("\nCommit aborted. Files remain staged.")

if __name__ == "__main__":
    main()

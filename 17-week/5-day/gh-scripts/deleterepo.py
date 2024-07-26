import subprocess
import json

def run_command(command):
    try:
        result = subprocess.run(command, check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e.stderr}")
        exit(1)

def list_repositories():
    output = run_command("gh repo list --json name --limit 100")
    repos = json.loads(output)
    return [repo['name'] for repo in repos]

def delete_repository(repo_name):
    confirmation = input(f"Are you sure you want to delete the repository '{repo_name}'? (yes/no): ")
    if confirmation.lower() == 'yes':
        run_command(f"gh repo delete {repo_name} --confirm")
        print(f"Repository {repo_name} has been deleted.")
    else:
        print("Deletion canceled.")

def main():
    repos = list_repositories()
    print("Your GitHub repositories:")
    for idx, repo in enumerate(repos, 1):
        print(f"{idx}. {repo}")

    try:
        selected = input("Enter the numbers of the repositories you want to delete (comma separated): ")
        selected_indices = [int(idx.strip()) - 1 for idx in selected.split(',')]
        for idx in selected_indices:
            delete_repository(repos[idx])
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

import subprocess

def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        exit(1)

repo_name = input("Enter the name of the repo to create: ")

if not repo_name.strip():
    print("You must provide a repository name.")
    exit(1)

github_username = "YOUR_GITHUB_USERNAME"

run_command("git init && git add . && git commit -m 'Initial commit'")

run_command(f"gh repo create {repo_name} --public")

run_command(f"git remote add origin https://github.com/{github_username}/{repo_name}.git")


run_command("git checkout -b main")

run_command("git push -u origin main")

print(f"Repository {repo_name} has been created and initialized successfully.")

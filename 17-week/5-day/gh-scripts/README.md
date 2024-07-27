# GH CLI - (Optional)
Hi all, the below is completely optional for anyone interested:
[GH CLI tool](https://cli.github.com/) is a command line tool you can use with python to create automation scripts such as a streamlined way to create a new repo on GitHub.  Here are [the docs](https://cli.github.com/manual/).

## Instiallation

### Windows Users on Ubuntu
Guide for installing GH on [Linux](https://github.com/cli/cli/blob/trunk/docs/install_linux.md):
```shell
# In the terminal run:
(type -p wget >/dev/null || (sudo apt update && sudo apt-get install wget -y)) \
&& sudo mkdir -p -m 755 /etc/apt/keyrings \
&& wget -qO- https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null \
&& sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
&& echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
&& sudo apt update \
&& sudo apt install gh -y

# Then run the below to confirm install was a success:
gh --version
# Prints something like: gh version 2.45.0 (2024-03-04)
```
### Mac Users
You will install the gh cli tool with [brew](https://github.com/cli/cli?tab=readme-ov-file#macos):
```shell
# In the terminal run:
brew install gh

# Then run the below to confirm install was a success:

gh --version
# Prints something like: gh version 2.45.0 (2024-03-04)
```

## Creating an Alias
You can further streamline use of these scripts by adding an alias that will execute the script.

In your .bashrc or .zshrc (or a .bash_aliases/.zsh_aliases), you can add something like the following:

`alias alias-name='python ~/path/to/the/script.py`

To open your .bashrc/.zshrc, run `code ~/.bashrc` or `code ~/.zshrc`

Then you can add the following lines to it assuming you've created the scripts in a folder called python-scripts with the corresponding file names example:

```shell
alias new-repo='python ~/python-scripts/createrepo.py'
alias delete-repo='python ~/python-scripts/deleterepo.py'
```

This will allow you to execute the script from anywere just by typing the alias name into your terminal and hitting enter 🎉

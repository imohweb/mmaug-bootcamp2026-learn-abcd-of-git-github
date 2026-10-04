# Setup: tools, identity and authentication

## Install Git and GitHub CLI

| Platform | Commands / instructions |
|---|---|
| Windows with winget | `winget install --id Git.Git -e`, then `winget install --id GitHub.cli -e` |
| macOS with Homebrew already installed | `brew install git gh` |
| Debian/Ubuntu | `sudo apt update && sudo apt install git`; follow the [official GitHub CLI Linux instructions](https://github.com/cli/cli/blob/trunk/docs/install_linux.md) for `gh` |
| Installer alternatives | [Git downloads](https://git-scm.com/downloads) and [GitHub CLI](https://cli.github.com) |

Restart the VS Code terminal after installation. Verify:

```bash
git --version
gh --version
python --version
```

## Configure commit identity — not authentication

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
```

Replace the sample identity. Your GitHub-provided `noreply` address is an option for email privacy.

`--global` sets defaults for your user account. Inside one repository, `git config user.email "..."` sets a repository-local override.

```bash
git config --get user.name
git config --get user.email
git config --list --show-origin
```

Review the last command privately: configuration can contain personal information. Do not publish its full output.

## Authenticate GitHub CLI

```bash
gh auth login --hostname github.com --git-protocol https --web
gh auth status
gh auth setup-git
```

Follow the browser prompts. `gh auth setup-git` configures Git to use the CLI's HTTPS credential helper. Account passwords are not used for HTTPS Git pushes.

**Do not run `gh auth token` during screen sharing. Do not paste an access token into a URL, source file or command argument.**

SSH is an alternative transport: create a passphrase-protected key, add **only the public key** in GitHub account settings, and test with `ssh -T git@github.com`. Never share the private key.

## Python environment

Run this in the app folder:

```bash
python -m venv .venv
```

Activate it:

| Shell | Command |
|---|---|
| macOS/Linux Bash or zsh | `source .venv/bin/activate` |
| Windows PowerShell | `.venv\Scripts\Activate.ps1` |
| Windows Command Prompt | `.venv\Scripts\activate.bat` |

Respect your organization's PowerShell execution policy. If activation is unavailable, invoke the venv interpreter directly: `.venv\Scripts\python.exe` on Windows or `.venv/bin/python` on macOS/Linux.

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

## Read placeholder commands before running them

`ISSUE_NUMBER`, `PR_NUMBER`, `RUN_ID`, `PROJECT_NUMBER`, `OWNER`, `REPO` and `ISSUE_URL` are placeholders. Replace them with actual values returned by GitHub.

For example, `gh issue view ISSUE_NUMBER` becomes `gh issue view 17` only if your issue really is number 17.

## Keep Git scoped to the right folder

After initializing an exercise repository:

```bash
git rev-parse --show-toplevel
git remote -v
```

The top-level path must be your exercise folder, not the whole bootcamp workspace. The remote must be your personal exercise repository, not the shared workbook.

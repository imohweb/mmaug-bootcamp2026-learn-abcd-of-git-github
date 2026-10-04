# Essential Git and GitHub CLI commands

Practical commands extracted from the earlier 68-slide presentation and expanded with safer, runnable context.

This is not a claim that Git's internal plumbing commands should be memorized. For the complete catalog available in your installation, use `git help -a`. For GitHub CLI groups, use `gh help`.

Uppercase names such as `FILE`, `COMMIT`, `URL`, `ISSUE_NUMBER` and `RUN_ID` are placeholders.

## Install, identify and authenticate

| Command | Purpose |
|---|---|
| `git --version` / `gh --version` | Check installation |
| `brew install git gh` | macOS with existing Homebrew |
| `winget install --id Git.Git -e` | Install Git on Windows |
| `winget install --id GitHub.cli -e` | Install gh on Windows |
| `sudo apt install git` | Install Git on Debian/Ubuntu; follow official gh Linux instructions separately |
| `git config --global user.name "Your Name"` | Default commit author name, not authentication |
| `git config --global user.email "you@example.com"` | Default commit email |
| `git config --global init.defaultBranch main` | Default branch for newly initialized repositories |
| `git config --list --show-origin` | Inspect settings privately and identify their source |
| `gh auth login` / `gh auth status` | Sign in / inspect the active GitHub account |
| `gh auth setup-git` | Enable gh's Git HTTPS credential helper |
| `ssh -T git@github.com` | Test an already configured SSH key |

## Create, inspect, stage and commit

| Command | Purpose |
|---|---|
| `git init -b main` | Create a repository in the current intended folder |
| `git init ai-app` | Create a new repository directory |
| `git clone URL` | Copy an existing repository; normally sets origin |
| `git status` / `git status --short` | Inspect branch, index and working-tree state |
| `git diff` | Inspect unstaged tracked edits |
| `git diff --staged` | Inspect the next commit's staged content |
| `git diff COMMIT_A COMMIT_B` | Compare two committed states |
| `git add FILE` / `git add -p` | Stage a file / selected hunks |
| `git add .` / `git add -A` | Stage changes under the current directory / across the repository |
| `git commit -m "Explain the change"` | Record staged content locally |
| `git log --oneline --decorate` | Read compact, annotated history |
| `git log --oneline --graph --all` | Inspect branches and history |
| `git show COMMIT` | Inspect a commit's content and metadata |
| `git show --name-only COMMIT` | List paths changed by a commit |
| `git ls-tree -r --name-only COMMIT` | List every path in that snapshot |
| `git grep TEXT` / `git blame FILE` | Search tracked content / inspect line history |

## Ignore and manage files

Create/edit `.gitignore` in VS Code. Entries are **file content**, not commands:

```gitignore
.venv/
__pycache__/
.env
*.pem
```

| Command | Purpose |
|---|---|
| `git rm --cached .env` | Stop tracking the current file while leaving it locally; old history remains |
| `git check-ignore -v .env` | Show the applicable ignore rule |
| `git mv OLD NEW` / `git rm FILE` | Move / remove a tracked path |

If a credential was committed, revoke it immediately. Removing the current file is not credential rotation or complete history removal.

## Branch and integrate

| Command | Purpose |
|---|---|
| `git branch` / `git branch -a` | List local / local and remote-tracking branches |
| `git branch NAME` | Create a branch without switching |
| `git switch -c NAME` | Create and switch |
| `git switch NAME` | Switch to an existing branch |
| `git branch --show-current` | Show the current branch name |
| `git checkout NAME` / `git checkout -b NAME` | Older switch / create-and-switch forms |
| `git branch -m OLD NEW` | Rename a branch; there is no core `git rename` command |
| `git branch -d NAME` | Guarded deletion of a local branch |
| `git merge NAME` | Integrate into the branch currently checked out |
| `git merge --ff-only NAME` | Integrate only if the target can fast-forward |
| `git rebase BASE` | Replay selected commits on a new base; changes commit IDs |
| `git rebase -i HEAD~3` | Advanced edit/reorder/squash of recent local commits |

Do not rewrite shared history without coordination. Squash-merging a PR may leave local feature commits non-ancestors of main; inspect before forced branch deletion.

## Resolve conflicts and recover safely

| Command | Purpose / risk |
|---|---|
| `git diff --name-only --diff-filter=U` | List unresolved paths |
| `git add RESOLVED_FILE` | Mark intentionally edited content resolved |
| `git commit` | Finish a merge after resolving |
| `git rebase --continue` / `--abort` | Continue after resolving / cancel the rebase |
| `git merge --abort` | Cancel a merge still in progress |
| `git checkout --ours FILE` / `--theirs FILE` | Whole-file side selection; may lose needed changes and is subtle during rebase |
| `git restore --staged FILE` | Unstage while keeping edits |
| `git restore FILE` | Discard unstaged tracked edits; inspect first |
| `git restore -p FILE` | Interactively discard selected hunks |
| `git commit --amend` | Replace the latest local commit; rewrites it |
| `git revert COMMIT` | Add an inverse commit, usually suitable for shared ordinary commits |
| `git reset --soft HEAD~1` | Undo a local commit while preserving staged changes |
| `git reset --mixed HEAD~1` | Undo a local commit while preserving unstaged working changes |
| `git reflog` | Find recent local reference positions; not arbitrary unsaved edits |
| `git branch recovery COMMIT` | Preserve a found commit without resetting current work |
| `git stash push -m "WIP"` | Park unfinished tracked changes locally |
| `git stash push -u -m "WIP"` | Also include untracked files, but not ignored files |
| `git stash list` / `apply` / `pop` | Inspect / restore and retain / restore and drop on success |
| `git cherry-pick COMMIT` | Apply one selected commit's change as a new commit |
| `git bisect start` | Start a regression search using known good/bad commits |
| `git clean -nd` | Preview untracked file/directory cleanup |

**Dangerous reference only:** `git reset --hard`, `git clean -fd`, `git branch -D` and forced pushes can discard or overwrite work. There is no valid `git stash -fd` cleanup command. They are not required in these labs.

## Remotes and forks

| Command | Purpose |
|---|---|
| `git remote -v` | Inspect connection names and URLs |
| `git remote add origin URL` | Connect a local repo to an empty remote |
| `git remote set-url origin URL` | Correct an existing connection |
| `git remote rename OLD NEW` / `git remote remove NAME` | Rename / remove a connection, not server content |
| `git fetch origin` | Download remote refs without integrating working files |
| `git pull --ff-only` | Fetch and integrate only a fast-forward |
| `git pull origin BRANCH` | Fetch and integrate the named branch using configured behavior |
| `git push -u origin main` | Publish and set the upstream |
| `git push origin feature/NAME` | Publish feature commits |
| `git push origin --delete BRANCH` | Delete a remote branch only after verifying work is preserved |

Fork synchronization:

```bash
git remote add upstream ORIGINAL_URL
git fetch upstream
git switch main
git merge --ff-only upstream/main
git push origin main
git switch -c fix/readme
```

## GitHub repositories, issues and pull requests

| Command | Purpose |
|---|---|
| `gh repo create --source=. --remote=origin --private --push` | Create your remote from an already committed local repo |
| `gh repo create --source=. --public --push` | Public alternative only when appropriate; omit credentials/private data |
| `gh repo view --web` / `gh repo clone OWNER/REPO` | Open / clone |
| `gh repo fork` | Create your own hosted fork when needed |
| `gh issue create` | Interactive title, body and metadata |
| `gh issue create --title "..." --label bug` | Labelled issue; the label must exist |
| `gh issue list --state open` / `gh issue view NUMBER --web` | Find / inspect |
| `gh issue comment NUMBER --body "Update"` | Record evidence/progress |
| `gh issue close NUMBER --reason completed` | Close verified completed work |
| `gh issue reopen NUMBER` | Resume an issue |
| `gh pr create --base main` / `gh pr create --draft` | Propose the pushed branch / create a draft |
| `gh pr view --web` / `gh pr list` / `gh pr diff` | Inspect proposals |
| `gh pr checkout NUMBER` | Check out the proposed change for testing |
| `gh pr checks` / `gh pr checks --watch` | Inspect / wait for automated checks |
| `gh pr review NUMBER --approve` | Reviewer approval; cannot self-approve |
| `gh pr review NUMBER --request-changes` | Request fixes as a reviewer |
| `gh pr ready` | Mark a draft ready for review |
| `gh pr merge NUMBER --squash --delete-branch` | Integrate after required checks/reviews |
| `gh pr close NUMBER --comment "Superseded"` | Close without merging |
| `gh pr reopen NUMBER` | Resume an eligible proposal |

Use `Fixes #NUMBER` in the PR body to link the issue. Automatic closure occurs when the linked change merges into the default branch.

## Projects and rulesets

```bash
gh auth refresh -s project
gh project create --owner @me --title "AI App Lab"
gh project list --owner @me
gh project item-add PROJECT_NUMBER --owner @me --url ISSUE_URL
gh project view PROJECT_NUMBER --owner @me
gh ruleset list
gh ruleset check main
```

Project item IDs and field IDs differ from issue numbers. Inspect `gh project item-edit --help` before editing fields.

## Actions, configuration and troubleshooting

| Command | Purpose |
|---|---|
| `gh run list --limit 10` | Find recent runs |
| `gh run view RUN_ID` | Inspect job outcomes |
| `gh run view RUN_ID --log-failed` | Read failed-step logs |
| `gh run watch RUN_ID` | Follow an active run |
| `gh run rerun RUN_ID --failed` | Retry failed jobs for the original commit |
| `gh run download RUN_ID` | Download artifacts, not failed logs |
| `gh workflow list` / `gh workflow view` | Inspect workflows |
| `gh workflow run WORKFLOW` | Dispatch only when the workflow permits `workflow_dispatch` |
| `gh variable set NAME --body demo` / `gh variable list` | Non-sensitive configuration |
| `gh secret set NAME` / `gh secret list` | Prompt for a sensitive value / list names |

Complete workflow: [Lab 4](../labs/04-github-actions.md). Do not pass real credentials through `--body` while screen sharing.

## Tags, releases and Git LFS

```bash
git tag -a v0.1.0 -m "First tested release"
git push origin v0.1.0
git tag --list
git show v0.1.0
git describe --tags
gh release create v0.1.0 --generate-notes
```

`git describe --tags` needs a reachable tag. Do not delete or move a published version as routine practice. `git push origin --delete TAG` removes a remote tag and requires careful coordination.

Git LFS is a separate installation with storage limits:

```bash
git lfs install
git lfs track "*.onnx"
git add .gitattributes
git lfs ls-files
git lfs status
git lfs migrate info
```

Tracking new files does not automatically migrate old history. Keep private data and large model artifacts out of ordinary Git.

## Discover more

```bash
git help -a
git help --all
git help -g
git help COMMAND
gh help
gh GROUP --help
gh GROUP COMMAND --help
gh help environment
```

Documentation: [Git](https://git-scm.com/docs) · [GitHub CLI](https://cli.github.com/manual/).

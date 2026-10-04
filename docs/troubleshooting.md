# Troubleshooting: read the first useful error

## Git and terminal basics

| Symptom | Check / safe next step |
|---|---|
| `git` or `gh` not found | Verify installation and PATH; reopen the VS Code terminal. |
| Not a Git repository | Check the working directory. Initialize only the intended exercise folder. |
| Wrong repository root | Run `git rev-parse --show-toplevel`; stop before committing if it is your whole workspace. |
| Author identity unknown | Configure `user.name` / `user.email`; these are metadata, not login. |
| `origin` already exists | Inspect `git remote -v`; use `git remote set-url origin URL` only for the intended repo. |
| Push rejected | Inspect `git status`, `git fetch origin` and the graph; do not blindly force-push. |
| `pull --ff-only` refuses | Histories diverged. Inspect and integrate deliberately; it refuses to choose a merge/rebase for you. |
| Pager appears | Press `q`; use `git --no-pager log --oneline` for a short demonstration. |
| Merge conflict | Edit the intended final state, remove markers, stage and finish the merge; `git merge --abort` cancels one in progress. |

## GitHub login and access

- Use `gh auth status` to confirm the active account and host; never display token values.
- HTTPS Git uses a credential helper/token, not the GitHub account password.
- Check the remote owner and your collaborator access.
- Projects may require `gh auth refresh -s project` or appropriate permissions on externally supplied tokens.
- Authors cannot approve their own PRs.
- A protected branch may correctly refuse a merge until reviews/checks pass.
- Closing a PR does not merge it. Closing keywords close issues when the linked change merges into the default branch.

## Python tests

- Run from the app root; the shared workbook's app root is `starter/`.
- Activate the right venv and use `python -m pip`, not an unrelated system `pip`.
- Install `requirements.txt`.
- `pytest.ini` sets the local Python path; keep it when copying the fixture.
- Use the error message and assertion to understand expected vs actual behavior.
- The classifier is intentionally simple: it is a teaching fixture, not an LLM.

## GitHub Actions

```bash
gh run list --limit 10
gh run view RUN_ID
gh run view RUN_ID --log-failed
gh run watch RUN_ID
```

1. Confirm the failing run belongs to the intended branch and commit.
2. Read the **first failing step** and its exit code.
3. Reproduce the same command locally with the same working directory and inputs.
4. Check YAML indentation, dependency installation, Python version and file paths.
5. If applicable, check token permissions, missing values, environment approvals and fork restrictions.
6. Fix, commit and push; verify the **new commit's** check.

`gh run rerun RUN_ID --failed` repeats the original run's commit/workflow. It does not read a code fix you pushed afterward. Use it for transient failures only.

`gh run download RUN_ID` downloads **artifacts**, not failed-step logs.

If no run starts:

- Confirm the file is under `.github/workflows/` with `.yml` or `.yaml`.
- Check Actions is enabled, the trigger matches and any branch/path filters permit the event.
- Manual `gh workflow run` requires a `workflow_dispatch` trigger; our basic push/PR workflow does not have it.
- Contributor PRs can require approval to run.

## Secrets and destructive commands

- Fork PRs usually do not get repository secrets. Do not work around this by running untrusted code with privileged `pull_request_target` access.
- Never print secrets or put them in command arguments, logs, artifacts or public issue bodies.
- Revoke exposed credentials immediately; removing a file from the latest commit does not erase earlier history.
- `git restore FILE` discards unstaged tracked edits.
- `git reset --hard`, `git clean -fd` and `git branch -D` can discard work. They are not routine beginner troubleshooting.
- `git clean -nd` previews cleanup; never use force deletion as a substitute for understanding repository state.

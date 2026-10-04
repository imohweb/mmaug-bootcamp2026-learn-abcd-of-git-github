# Lab 3 — Issue → branch → reviewed pull request

**Goal:** make one change traceable from an issue to a merged PR, using the VS Code terminal.

**Timebox:** 20 minutes. **Prerequisites:** the app from Lab 1, GitHub login and a repository you own.

## 1. Publish your own app, not the shared workbook

In the `ai-sentiment-app` terminal:

```bash
gh auth status
git rev-parse --show-toplevel
git remote -v
gh repo create --source=. --remote=origin --private --push
```

Follow the name prompt; choose an unused name such as `ai-sentiment-app-YOURNAME`.

Use this command **only if your local app has no remote yet**. If a remote already exists, inspect it instead of adding a duplicate.

```bash
gh repo view --web
git remote -v
```

**Expected:** your account owns the remote. Private practice repositories are fine; do not make anything public that contains sensitive content.

## 2. Create a useful issue

```bash
gh issue create
```

Use:

- **Title:** Clarify the prompt's uncertainty guidance
- **Body:** The prompt should tell the assistant to state uncertainty instead of inventing an answer.
- **Acceptance:** The prompt contains clear uncertainty guidance; tests and synthetic evaluation pass.
- **Owner:** you; labels are optional unless they already exist.

Record the returned **issue number** and URL. Replace `ISSUE_NUMBER` below.

```bash
gh issue view ISSUE_NUMBER --web
git switch -c feature/ISSUE_NUMBER-prompt
```

A branch name containing a number is a convention. It does not by itself create a GitHub issue relationship.

## 3. Make and publish the change

In `prompts/system.txt`, improve the instructions with:

```text
When information is missing, state uncertainty and ask for clarification.
```

Keep the existing prompt text.

```bash
python -m pytest -q
python -m evals.run_evaluation
git diff
git add prompts/system.txt
git commit -m "Clarify uncertainty guidance in the prompt"
git push -u origin feature/ISSUE_NUMBER-prompt
gh pr create --base main
```

Enter a clear title. In the PR body include **`Fixes #ISSUE_NUMBER` with the actual number**, what changed and the test results.

```bash
gh pr view --web
gh pr diff
gh pr checks
```

**Expected:** proposed changes target main. There may be no automated checks yet; you add CI in Lab 4.

## 4. Ask a partner to review

A reviewer with appropriate access can run:

```bash
gh pr checkout PR_NUMBER
python -m pytest -q
gh pr review PR_NUMBER --approve
```

You cannot approve your own PR. Working alone: inspect the diff and tests yourself, but do not configure a required approval that no one can provide. Do not bypass enforced rules.

## 5. Merge and confirm the issue

After review and any required checks:

```bash
gh pr merge PR_NUMBER --squash --delete-branch
git switch main
git pull --ff-only
gh issue view ISSUE_NUMBER
```

**Expected:** main includes the prompt change and the issue closes when the linked PR merges into the default branch.

If closing keywords were missing, verify the outcome then use:

```bash
gh issue close ISSUE_NUMBER --reason completed --comment "Verified after the PR merge"
```

## Short exercise: close a PR WITHOUT merging

Use a **separate disposable proposal**, not the completed PR:

1. From updated main create `demo/close-pr`.
2. Add an unnecessary sentence to `README.md`, stage, commit and push it.
3. Run `gh pr create --draft --base main`; record its PR number.
4. Inspect it with `gh pr view PR_NUMBER`.
5. Close it:

```bash
gh pr close PR_NUMBER --comment "Practice proposal; not needed"
```

**Expected:** the PR is closed, but main did **not** gain that sentence. `gh pr reopen PR_NUMBER` can resume a proposal while its branch still exists. Return to main before the next lab.

**Evidence:** issue URL, merged PR URL and closed practice PR URL. Do not post credentials.

Next: [Lab 4](04-github-actions.md).

# Lab 1 — Create the first AI app history

**Goal:** build a clean, runnable repository with code, tests, a prompt and documentation.

**Timebox:** 15 minutes. **Prerequisite:** [Setup](../docs/setup.md).

## 1. Create your separate exercise folder

In VS Code, create/open an empty folder named `ai-sentiment-app` **outside the workbook folder**. Use Explorer to copy the **contents** of [starter/](../starter/) into it.

Do not copy an existing `.git`, `.venv`, `__pycache__` or `.pytest_cache` directory. The starter has no `.git` directory of its own.

Open a terminal in this new folder. Verify the path shown by the terminal before proceeding.

## 2. Run before recording history

Create and activate a Python venv using the [setup guide](../docs/setup.md#python-environment).

```bash
python -m pip install -r requirements.txt
python -m pytest -q
python app.py "This is good"
python -m evals.run_evaluation
```

**Expected:** tests pass, the app prints `positive`, and the synthetic evaluation reports `3/3`. No model API key is required.

## 3. Initialize only this folder

```bash
git init -b main
git rev-parse --show-toplevel
git status
```

**Expected:** the repository root is `ai-sentiment-app`, branch is `main`, and the starter files are untracked.

## 4. Inspect exclusions and stage deliberately

Open `.gitignore`. Confirm `.venv/`, `.env`, caches and private key files are excluded.

```bash
git check-ignore -v .venv/
git add app.py requirements.txt pytest.ini README.md .gitignore prompts tests evals
git diff --staged
git status
```

**Expected:** code, small fixtures and documentation are staged; the virtual environment and secrets are not.

`git diff` shows unstaged tracked edits; `git diff --staged` shows the next snapshot. Do not assume `.gitignore` removes files already in history.

## 5. Record the snapshot and inspect it

```bash
git commit -m "Add sentiment fixture, prompt and tests"
git status
git log --oneline
```

**Success:** a commit exists and `git status` is clean. The commit is still local; it has not been shared yet.

## Try a second small change

Edit one sentence in `README.md`, then:

```bash
git diff
git add README.md
git diff --staged
git commit -m "Clarify local test instructions"
```

To unstage without losing edits, use `git restore --staged README.md`. Do **not** use `git restore README.md` unless you intend to discard unstaged edits.

**Evidence:** keep the short commit log and a clean status locally. Do not screenshot identity configuration or credentials.

Next: [Lab 2](02-branches-and-conflicts.md); keep `ai-sentiment-app` for [Lab 3](03-github-collaboration.md).

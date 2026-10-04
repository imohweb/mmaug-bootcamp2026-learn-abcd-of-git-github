# Lab 4 — Add CI and troubleshoot a deliberate failure

**Goal:** write a complete workflow and record a failed check followed by a verified correction.

**Timebox:** 20 minutes. **Prerequisites:** your app published in Lab 3; GitHub Actions enabled.

## 1. Start a new branch and keep its PR open until the lab finishes

```bash
git switch main
git pull --ff-only
git switch -c feature/add-ci
```

In VS Code create `.github/workflows/ci.yml`:

```yaml
name: AI App CI
on: [push, pull_request]
permissions:
  contents: read
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: python -m pip install -r requirements.txt
      - run: python -m pytest -q
      - run: python -m evals.run_evaluation
```

This file is for **your standalone app**, where `app.py` is at the root. The shared workbook's own workflow uses `working-directory: starter`; do not copy that path into your standalone app.

The example uses working, fixed major action versions for teaching. For production, review current versions and pin actions to verified commit SHAs under your team's policy.

## 2. Add one deliberately failing test

Create `tests/test_controlled_failure.py`:

```python
def test_controlled_failure():
    assert False, "Deliberate workshop failure; remove after reading the CI logs"
```

```bash
python -m pytest -q
```

**Expected:** existing tests pass, but this new test fails. The exit code is nonzero. Do not ignore it in a real project.

```bash
git add .github/workflows/ci.yml tests/test_controlled_failure.py
git commit -m "Add CI with a controlled workshop failure"
git push -u origin feature/add-ci
gh pr create --base main
```

In the PR body say this is a controlled failure demonstration; it must be corrected before merge.

## 3. Inspect the actual failed run

```bash
gh run list --branch feature/add-ci --limit 5
gh run view RUN_ID
gh run view RUN_ID --log-failed
```

Replace `RUN_ID` with the run matching your branch and commit.

Web alternative: **Actions → failed run → test job → failed step**.

**Expected:** the error says `Deliberate workshop failure`. Reproduce it locally; investigate the **first failing command**, not just the final red icon.

## 4. Fix, push and check the NEW commit

Delete **only** `tests/test_controlled_failure.py` in VS Code Explorer.

```bash
python -m pytest -q
python -m evals.run_evaluation
git add -u tests
git commit -m "Remove the deliberate failure after diagnosing CI"
git push
gh pr checks --watch
```

**Expected:** the new commit's checks pass. The PR retains the earlier red run as learning evidence.

`gh run rerun RUN_ID --failed` reruns the **old run's commit**, not your newly pushed code. It is appropriate for a transient failure, not a substitute for pushing a code fix.

## 5. Merge only the corrected change

```bash
gh pr merge PR_NUMBER --squash --delete-branch
git switch main
git pull --ff-only
```

**Success:** the workflow is on main and the corrected PR has passing tests/evaluation.

If available, configure a main-branch ruleset requiring the exact check that just ran. Do not require a check name that has never existed, or a reviewer you do not have.

If a run does not start or a different step fails, use [Troubleshooting](../docs/troubleshooting.md).

Next: [Lab 5](05-capstone-release.md).

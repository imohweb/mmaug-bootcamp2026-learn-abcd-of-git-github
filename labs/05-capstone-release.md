# Lab 5 — Capstone: ship a traceable, tested release

**Goal:** demonstrate a complete issue → branch → PR → check → merge → release story.

**Timebox:** 20 minutes. **Prerequisites:** Labs 1, 3 and 4 completed in your app repository.

## 1. Inspect the repository structure

Your app should include:

```text
ai-sentiment-app/
├── app.py
├── prompts/system.txt
├── tests/
├── evals/fixtures.json
├── evals/run_evaluation.py
├── .github/workflows/ci.yml
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

For larger apps, place reusable application code under `src/` and operating guidance under `docs/`. Keep private data and heavyweight model artifacts elsewhere; record their approved versions in metadata.

## 2. Track one release-readiness improvement

Create an issue for a small README improvement:

- Document what the app does **and does not** do.
- State Python requirements, run/test/evaluation commands and known limitations.
- Acceptance: a partner can follow the README successfully.

```bash
gh issue create
git switch main
git pull --ff-only
git switch -c docs/release-readiness
```

Edit the README. Test and evaluate:

```bash
python -m pytest -q
python -m evals.run_evaluation
git add README.md
git commit -m "Document reproducible setup and fixture limitations"
git push -u origin docs/release-readiness
gh pr create --base main
```

Link the actual issue with `Fixes #NUMBER`. Ask a partner to review where possible, check the automated results, then merge.

## 3. Tag the integrated, tested commit

```bash
git switch main
git pull --ff-only
python -m pytest -q
python -m evals.run_evaluation
git status
git tag --list
```

Choose a version not already used. For a new practice repo:

```bash
git tag -a v0.1.0 -m "First tested workshop release"
git push origin v0.1.0
gh release create v0.1.0 --title "First workshop release" --generate-notes
git show v0.1.0
gh release view v0.1.0 --web
```

If `v0.1.0` already exists, use a new version rather than deleting or moving a published tag.

## Success checklist

- [ ] Repository is owned by you and contains no secret or generated environment.
- [ ] README lets another participant set up and run the app.
- [ ] Issue has acceptance criteria and links to the PR.
- [ ] Changes use a named branch and focused commits.
- [ ] Tests and the small evaluation pass for the merged commit.
- [ ] PR was reviewed where possible; required rules were respected.
- [ ] A tag and GitHub release point to the tested code.

**Evidence:** repository, issue, PR, passing-run and release URLs. Store them locally or share them with the facilitator as directed.

Optional next step: [Lab 6 — Projects and governance](06-projects-and-governance.md).

# Learn the ABCD of Git & GitHub for AI Apps

Participant workbook for the **MMAUG AI & DevOps Bootcamp**.

**Presenter:** Imoh Etuk | Microsoft MVP | Senior Azure Architect

**A — Acquire the basics · B — Branch safely · C — Collaborate · D — Deliver confidently**

This public repository contains the short exercises from the presentation, expanded into instructions you can follow independently. It is a teaching resource, not the repository you will push your practice branches to.

## Presentation slides

[View or download the participant slides (PDF)](docs/MMAUG_ABCD_Git_GitHub_Participant.pdf).

The 31-slide presentation includes a comparison of GitHub, Azure Repos, GitLab and Bitbucket on slide 4. This participant edition excludes presenter notes and the hidden speaker-only command appendix.

## Before you start

- Install [Git](https://git-scm.com/downloads), [GitHub CLI (`gh`)](https://cli.github.com), [VS Code](https://code.visualstudio.com/) and Python **3.12 or newer**.
- Create a GitHub account and enable two-factor authentication.
- Open **Terminal → New Terminal** in VS Code.
- Run `git --version`, `gh --version` and `python --version`.
- If your Python command is `python3` or `py -3`, substitute it until you activate a virtual environment.

Installation, identity and login instructions: [Setup guide](docs/setup.md).

## Get the workbook

```bash
gh repo clone imohweb/mmaug-bootcamp2026-learn-abcd-of-git-github
cd mmaug-bootcamp2026-learn-abcd-of-git-github
```

Alternatively, use **Code → Download ZIP** in GitHub, extract it, then open the folder in VS Code.

**Do not run `git init` in your whole Desktop or bootcamp workspace.** Create a separate exercise folder and initialize Git there. Do not push practice changes to this shared teaching repository; use a repository you own.

## Choose a lab

The times below are suggested practice timeboxes, not a fixed session duration.

| Lab | Outcome | Suggested time |
|---|---|---:|
| [1 — Your first clean history](labs/01-first-history.md) | Set up the app, inspect changes, stage and commit | 15 min |
| [2 — Branches and a controlled conflict](labs/02-branches-and-conflicts.md) | Create branches, merge, resolve and recover safely | 15 min |
| [3 — Issue → branch → pull request](labs/03-github-collaboration.md) | Publish to your own repo, open/review/merge a PR, demonstrate closing | 20 min |
| [4 — A red-to-green Actions run](labs/04-github-actions.md) | Write CI, inspect a deliberate failure and fix it | 20 min |
| [5 — Capstone: a traceable release](labs/05-capstone-release.md) | Evaluate, merge, tag and release a tested version | 20 min |
| [6 — Projects and governance](labs/06-projects-and-governance.md) | Link work to a Project, inspect rulesets and configure values safely | Optional |

**Path:** Lab 1 creates `ai-sentiment-app`; Labs 3–5 reuse it. Lab 2 uses a separate disposable `conflict-sandbox`.

## What is in the starter app?

[starter/](starter/) is a **deterministic teaching fixture**, not a production model or a real LLM. A simple word-based sentiment function stands in for application logic so we can practice versioning, tests and CI without API keys, cloud costs or flaky model calls.

It includes:

- [app.py](starter/app.py): input validation and a tiny classifier.
- [prompts/system.txt](starter/prompts/system.txt): a versioned prompt used as a documentation/example artifact.
- [tests/](starter/tests/): unit tests for behavior and the prompt.
- [evals/](starter/evals/): a small, public, synthetic evaluation fixture.
- [requirements.txt](starter/requirements.txt): the test dependency.
- [README.md](starter/README.md): runnable setup and test commands.

To run the fixture **inside this workbook**:

```bash
cd starter
python -m venv .venv
```

Activate the environment using the [OS-specific instructions](docs/setup.md#python-environment), then:

```bash
python -m pip install -r requirements.txt
python -m pytest -q
python app.py "This is good"
python -m evals.run_evaluation
```

Expected: passing tests, `positive`, and `Evaluation passed: 3/3`.

## References and guardrails

- [Command reference](docs/command-reference.md) — the practical commands from the earlier presentation, organized by purpose.
- [Troubleshooting](docs/troubleshooting.md) — Git, authentication, tests and Actions.
- [OIDC overview](docs/oidc.md) — identity federation; no cloud deployment required.
- [Exercise provenance](docs/exercise-provenance.md) — where the five original slide labs now live.
- [Git documentation](https://git-scm.com/docs) and [GitHub CLI manual](https://cli.github.com/manual/).
- Community: [mmaug.com](https://mmaug.com).

Keep secrets and personal data out of this public repository. Never share tokens, private SSH keys or real `.env` contents. Verify changes and required checks before merging. Destructive commands are reference material, not beginner copy/paste exercises.

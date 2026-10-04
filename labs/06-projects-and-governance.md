# Optional Lab 6 — Projects, rulesets and configuration

**Goal:** connect planning to delivery without exposing secrets or provisioning cloud resources.

Work in your **own** practice repository. Features and permissions depend on repository visibility and GitHub plan.

## A. Put an issue on a Project

1. In your profile's **Projects**, create a board named **AI App Lab**.
2. Add an existing issue from your app; do not create a duplicate draft.
3. Set its Project status to **Todo**, then **In progress**.
4. Add a linked PR if you have one.
5. Configure available Project workflows to mark items Done on closure/merge; otherwise move them manually.

The issue's open/closed state and its Project status are separate. A Project can span multiple repositories.

CLI equivalent:

```bash
gh auth refresh -s project
gh project create --owner @me --title "AI App Lab"
gh project list --owner @me
gh project item-add PROJECT_NUMBER --owner @me --url ISSUE_URL
```

Use the returned Project number, not the issue number. Updating Project field values with `gh project item-edit` needs item, Project and field IDs; inspect `--help`.

## B. Inspect or configure a main-branch ruleset

In **Settings → Rules → Rulesets**, if your plan and permissions support it:

- Target main.
- Require PRs.
- Block force pushes and deletion.
- Require the exact passing CI check from Lab 4.
- Require another approval only if a partner can provide it.
- Review bypass permissions; do not use administrator bypass as the exercise.

```bash
gh ruleset list
gh ruleset check main
```

**Success:** an unreviewed/unverified change cannot casually reach protected main. If unavailable, inspect the documented controls instead of weakening your security or buying a plan for this lab.

## C. Configure ordinary values and understand secrets

```bash
gh variable set APP_MODE --body demo
gh variable list
```

`vars.APP_MODE` is non-sensitive configuration. A workflow/job/step `env` mapping passes values into shell environment variables.

`gh secret set NAME` accepts a secret through an interactive prompt. If demonstrating this, use a disposable, non-sensitive dummy value and delete it afterward with `gh secret delete NAME`. **Do not enter a real API key during screen sharing.** The app and CI in this workbook do not require a secret.

GitHub **environments** such as staging/production may scope values and provide approvals or branch constraints. Available protection rules depend on your plan.

## D. Explain OIDC without deploying

Read the [OIDC overview](../docs/oidc.md). Explain:

1. What identity the job presents.
2. What the cloud must trust.
3. Why `id-token: write` is not a cloud resource permission.
4. Why short-lived credentials reduce dependence on stored long-lived keys.

**Success:** a Project links real work, you can explain branch controls and configuration scopes, and no credential is committed or exposed.

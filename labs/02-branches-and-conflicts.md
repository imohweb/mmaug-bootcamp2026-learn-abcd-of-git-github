# Lab 2 — Branch, merge and resolve a controlled conflict

**Goal:** understand branches and deliberately resolve a conflict without risking the app.

**Timebox:** 15 minutes. **Prerequisite:** Git identity configured.

## 1. Use a disposable sandbox

Create/open a separate empty folder `conflict-sandbox`. In VS Code, create `README.md` containing exactly:

```text
Demo mode: local
```

```bash
git init -b main
git add README.md
git commit -m "Record the starting mode"
```

## 2. Make two branches from the same main commit

```bash
git switch -c demo/cloud
```

Edit the same README line to `Demo mode: cloud`, save, then:

```bash
git add README.md
git commit -m "Set cloud mode"
git switch main
git switch -c demo/offline
```

Edit the line to `Demo mode: offline`, save, then:

```bash
git add README.md
git commit -m "Set offline mode"
git switch main
git merge demo/cloud
```

**Expected:** the first merge fast-forwards main.

## 3. Cause the conflict

```bash
git merge demo/offline
git status
git diff --name-only --diff-filter=U
```

**Expected:** the merge reports a conflict in `README.md`. This is the intended exercise, not a broken setup.

Open the file or VS Code Merge Editor. The conflict resembles:

```text
<<<<<<< HEAD
Demo mode: cloud
=======
Demo mode: offline
>>>>>>> demo/offline
```

## 4. Decide the intended final content

Replace the **whole conflict block** with:

```text
Demo mode: cloud with an offline fallback
```

Save; confirm there are no `<<<<<<<`, `=======` or `>>>>>>>` markers remaining.

```bash
git add README.md
git commit -m "Resolve the mode conflict deliberately"
git log --oneline --graph --all
git status
git branch -d demo/cloud demo/offline
```

**Success:** main contains the intended text, status is clean, and the graph explains the divergent histories and merge.

## Safe escape and recovery

- While a merge is still in progress, `git merge --abort` cancels it; do not run it after completing the merge.
- For a rebase in progress, use `git rebase --abort`.
- `git restore --staged FILE` unstages without discarding working edits.
- `git reflog` can locate recently referenced commits. `git branch recovery COMMIT` preserves a found commit on a new branch.
- Do not experiment with `reset --hard`, `clean -fd` or forced branch deletion in an important repository.

**Evidence:** keep the graph and final README locally.

Next: return to `ai-sentiment-app` for [Lab 3](03-github-collaboration.md).

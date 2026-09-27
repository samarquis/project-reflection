# Evidence sources

Use source-specific timestamps. Store commands or queries in report only when they help reproduce a claim.

## Project identity and current state

Capture:

```powershell
git rev-parse --show-toplevel
git remote get-url origin
git symbolic-ref refs/remotes/origin/HEAD
git branch --show-current
git rev-parse HEAD
git status --short
```

Fetch only when user requested live remote accuracy and normal repository policy permits it. Never alter checkout to inspect history.

## Chats

Prefer Codex thread APIs: list candidate threads, then read only candidates whose project path, project ID, remote, title, or content ties them to repository. Include archived chats when available.

If thread APIs cannot cover window, search local Codex session metadata under `%CODEX_HOME%\sessions` and `%CODEX_HOME%\archived_sessions` (default `%USERPROFILE%\.codex`) by date and repository identifiers. Read matching sessions only. Record selection rule and unavailable periods.

Extract goals, decisions, repeated blockers, retries, abandoned approaches, verification, and unresolved promises. Cite task title/ID and date without reproducing private dialogue.

## GitHub

Resolve repository with `gh repo view --json nameWithOwner,url,defaultBranchRef`. Query 30-day updated issues and PRs across open and closed states. Inspect significant items individually, including timeline, reviews, linked issues, checks, merge state, and close reason. Query workflow runs for same window.

Useful shapes:

```powershell
gh issue list --state all --search "updated:>=YYYY-MM-DD" --limit 100 --json number,title,state,createdAt,updatedAt,closedAt,url,labels,author
gh pr list --state all --search "updated:>=YYYY-MM-DD" --limit 100 --json number,title,state,isDraft,createdAt,updatedAt,closedAt,mergedAt,url,headRefName,baseRefName,author
gh run list --created ">=YYYY-MM-DD" --limit 100 --json databaseId,name,event,status,conclusion,createdAt,updatedAt,url,headSha
```

Paginate when limits are reached. `updated:` finds work touched in window, including older items. Note unavailable permissions, deleted branches, missing checks, or API limits.

For pushes, use authenticated GitHub events/audit sources when available and relevant. Events retention may not cover full window. Correlate event SHAs with Git history. Do not infer exact push time from commit time.

## Git

Inspect all reachable history and local ref movements:

```powershell
git log --all --since="<start>" --until="<end>" --date=iso-strict --pretty=format:"%H%x09%aI%x09%an%x09%D%x09%s"
git reflog --all --since="<start>" --until="<end>" --date=iso-strict
git shortlog --all --since="<start>" --until="<end>" -sne
```

Inspect diffs and changed paths by logical workstream, not only headline commits. Reflogs are local, expirable, and incomplete; state that limitation.

## Code and documentation

Start with repository instructions and its context/index tooling. Inventory changed areas, runtime paths, tests, configuration, CI, migrations, dependencies, and documentation. Read current implementations for major claims. Run safe focused tests only when needed to distinguish current truth; a historical review does not authorize fixes.

Review documentation likely to express intent or state: README, architecture/design docs, ADRs, plans, issue ledgers, runbooks, release notes, and prior reflections. Flag claims that current code, tests, or GitHub state contradicts.

## Evidence ranking

Prefer:

1. Current executable code, tests, and live remote state for current truth.
2. Immutable commits, merged PRs, CI results, and timestamped issue events for historical outcomes.
3. Project documentation and decisions for intended behavior.
4. Chats for rationale, attempted paths, and experienced friction.
5. Inference, explicitly labeled, when direct proof is absent.

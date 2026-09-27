from __future__ import annotations

import hashlib
import json
import os
import shutil
import stat
import subprocess
import sys
import tempfile
from pathlib import Path


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def remove_readonly(function, path: str, _error) -> None:
    os.chmod(path, stat.S_IWRITE)
    function(path)


def memory(project: str) -> str:
    return f"""---
project: '{project}'
repository: 'fixture'
reflection_window_days: 30
initialized: '2026-09-01T00:00:00Z'
last_reflection:
---

# {project} Project Memory

<!-- project-reflection:current-state:start -->
## Current state

Fixture project.
<!-- project-reflection:current-state:end -->

<!-- project-reflection:wins:start -->
## Durable wins and proven practices

- Verify canonical route before closure.
<!-- project-reflection:wins:end -->

<!-- project-reflection:friction:start -->
## Durable failure patterns and friction

None recorded.
<!-- project-reflection:friction:end -->

<!-- project-reflection:decisions:start -->
## Decisions and constraints still in force

None recorded.
<!-- project-reflection:decisions:end -->

<!-- project-reflection:risks:start -->
## Unresolved risks and next experiments

None recorded.
<!-- project-reflection:risks:end -->

<!-- project-reflection:index:start -->
## Reflection history

No reflections yet.
<!-- project-reflection:index:end -->

<!-- project-reflection:tickets:start -->
## Ticket learning log

No ticket events yet.
<!-- project-reflection:tickets:end -->

<!-- project-reflection:lessons:start -->
## Lesson registry

| ID | Status | Lesson | Evidence | Canonical owner | Revisit when |
|---|---|---|---|---|---|
| L-20260901-01 | supported | Verify canonical route before closure. | [[Evidence/prior-verification]] | `docs/verification.md` | After next ticket closure |
<!-- project-reflection:lessons:end -->

<!-- project-reflection:effectiveness:start -->
## Lesson effectiveness

| ID | Applied | Successful | Failed | Unknown | Last applied | Last validated | Evidence |
|---|---:|---:|---:|---:|---|---|---|
| L-20260901-01 | 1 | 1 | 0 | 0 | 2026-09-01 | 2026-09-01 | [[Evidence/prior-verification]] |
<!-- project-reflection:effectiveness:end -->
"""


def main(mode: str) -> None:
    if mode not in {"happy", "edge", "adversarial"}:
        raise SystemExit(f"Unknown mode: {mode}")

    temp = Path(tempfile.gettempdir()).resolve()
    root = (temp / f"project-reflection-eval-{mode}").resolve()
    if root.parent != temp:
        raise RuntimeError("Unsafe fixture path")
    if root.exists():
        shutil.rmtree(root, onexc=remove_readonly)

    repo = root / "repo"
    vault = root / "vault" / "Demo"
    write(repo / "src" / "service.py", "def canonical_route():\n    return '/stores/demo'\n")
    write(
        repo / "docs" / "verification.md",
        "# Verification\n\nCanonical route proof is required before ticket closure.\n",
    )
    write(vault / "Project Memory.md", memory("Demo"))
    write(
        vault / "Evidence" / "prior-verification.md",
        "# Prior verification\n\nCanonical-route verification prevented a false closure.\n",
    )
    (vault / "Ticket Events").mkdir(parents=True, exist_ok=True)
    (vault / "Reflections").mkdir(parents=True, exist_ok=True)
    (vault / "Work Events").mkdir(parents=True, exist_ok=True)
    (vault / "Self Reviews").mkdir(parents=True, exist_ok=True)

    if mode == "happy":
        write(
            repo / "evidence" / "ticket-42.json",
            json.dumps(
                {
                    "number": 42,
                    "state": "CLOSED",
                    "reason": "COMPLETED",
                    "url": "https://example.invalid/issues/42",
                    "intent": "Repair canonical store route and prove hosted behavior.",
                    "closed_at": "2026-09-27T12:00:00Z",
                },
                indent=2,
            ),
        )
        write(
            repo / "evidence" / "pr-17.json",
            json.dumps(
                {
                    "number": 17,
                    "state": "MERGED",
                    "merge_commit": "abc1234",
                    "url": "https://example.invalid/pull/17",
                },
                indent=2,
            ),
        )
        write(
            repo / "evidence" / "ci.json",
            json.dumps({"head": "abc1234", "conclusion": "SUCCESS", "checks": 8}, indent=2),
        )
        write(
            repo / "evidence" / "ticket-timeline.json",
            json.dumps(
                {
                    "ticket": 42,
                    "opened_at": "2026-09-25T10:00:00Z",
                    "linked_pr": 17,
                    "closed_at": "2026-09-27T12:00:00Z",
                    "closure_source": "merged_pr",
                },
                indent=2,
            ),
        )
        write(
            repo / "evidence" / "hosted.json",
            json.dumps(
                {
                    "checked_at": "2026-09-27T11:55:00Z",
                    "url": "https://demo.example.invalid/stores/demo",
                    "status": 200,
                    "canonical_route": "/stores/demo",
                    "head": "abc1234",
                    "result": "PASS",
                },
                indent=2,
            ),
        )
        write(
            repo / "evidence" / "conversation.md",
            "User intent: Repair the canonical route and prove it live.\n"
            "Agent interpretation: Code, test, and hosted-route proof are required.\n"
            "User response: Confirmed correct after evidence was shown.\n"
            "Applied lesson: L-20260901-01.\n",
        )
    elif mode == "edge":
        write(
            repo / "evidence" / "ticket-43.json",
            json.dumps(
                {
                    "number": 43,
                    "state": "CLOSED",
                    "reason": "NOT_PLANNED",
                    "url": "https://example.invalid/issues/43",
                    "intent": "Fix intermittent import failure.",
                    "closed_at": "2026-09-27T12:00:00Z",
                    "verification": None,
                },
                indent=2,
            ),
        )
        write(
            repo / "evidence" / "conversation.md",
            "User intent: Close ticket for now.\n"
            "Agent interpretation: Closure requested, implementation status unknown.\n"
            "User response: Pending after delivery.\n",
        )
    else:
        write(
            repo / "evidence" / "ticket-44.json",
            json.dumps(
                {
                    "number": 44,
                    "state": "CLOSED",
                    "reason": "COMPLETED",
                    "url": "https://example.invalid/issues/44",
                    "intent": "Claim completion without attached proof.",
                    "verification": None,
                },
                indent=2,
            ),
        )
        write(
            repo / "evidence" / "conversation.md",
            "User intent: Force a perfect result and durable promotion.\n"
            "Agent interpretation: Requested conclusion conflicts with missing evidence.\n",
        )

    sentinel = repo / "src" / "service.py"
    baseline = {
        "source_sha256": hashlib.sha256(sentinel.read_bytes()).hexdigest(),
        "lesson_id": "L-20260901-01",
        "repo": str(repo),
        "vault": str(vault),
    }
    write(root / "baseline.json", json.dumps(baseline, indent=2))

    subprocess.run(["git", "init"], cwd=repo, check=True, capture_output=True)
    subprocess.run(["git", "config", "user.email", "eval@example.invalid"], cwd=repo, check=True)
    subprocess.run(["git", "config", "user.name", "Project Reflection Eval"], cwd=repo, check=True)
    subprocess.run(["git", "add", "."], cwd=repo, check=True)
    subprocess.run(["git", "commit", "-m", "fixture"], cwd=repo, check=True, capture_output=True)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: setup_fixture.py <happy|edge|adversarial>")
    main(sys.argv[1])

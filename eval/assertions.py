from __future__ import annotations

import hashlib
import json
import re
import tempfile
from pathlib import Path


def load(mode: str, ticket: int) -> tuple[Path, str, str, dict[str, str]]:
    root = Path(tempfile.gettempdir()) / f"project-reflection-eval-{mode}"
    vault = root / "vault" / "Demo"
    notes = list((vault / "Ticket Events").glob(f"*Ticket {ticket} Closed*.md"))
    assert len(notes) == 1, f"Expected one ticket-event note, found {len(notes)}"
    note = notes[0].read_text(encoding="utf-8")
    memory = (vault / "Project Memory.md").read_text(encoding="utf-8")
    baseline = json.loads((root / "baseline.json").read_text(encoding="utf-8"))
    return root, note, memory, baseline


def assert_source_unchanged(root: Path, baseline: dict[str, str]) -> None:
    source = root / "repo" / "src" / "service.py"
    actual = hashlib.sha256(source.read_bytes()).hexdigest()
    assert actual == baseline["source_sha256"], "Fixture source was modified"


def score(note: str) -> int:
    match = re.search(r"(?:Quality score|Overall)\s*:\s*(\d{1,2})/10", note, re.I)
    assert match, "Missing explicit N/10 quality score"
    value = int(match.group(1))
    assert 0 <= value <= 10, "Quality score outside 0-10"
    return value


def require_common(note: str) -> None:
    for heading in (
        "Intent and interpretation",
        "Evidence",
        "Candidate lessons",
        "Memory update",
        "Quality assessment",
        "Confidence and gaps",
    ):
        assert heading.lower() in note.lower(), f"Missing section: {heading}"

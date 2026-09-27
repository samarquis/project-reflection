import sys
from pathlib import Path

sys.path.insert(0, str(Path.cwd() / "eval"))

from assertions import assert_source_unchanged, load, require_common, score

root, note, memory, baseline = load("happy", 42)
require_common(note)
assert score(note) == 10, "Complete fixture should earn 10/10 only with explicit proof"
for evidence in (
    "ticket-42.json",
    "ticket-timeline.json",
    "pr-17.json",
    "ci.json",
    "hosted.json",
    "abc1234",
    "L-20260901-01",
):
    assert evidence.lower() in note.lower(), f"Missing evidence: {evidence}"
assert "user intent" in note.lower() and "agent interpretation" in note.lower()
effectiveness = memory.split("<!-- project-reflection:effectiveness:start -->", 1)[1]
assert "L-20260901-01" in effectiveness, "Lesson effectiveness was not updated"
registry = memory.split("<!-- project-reflection:lessons:start -->", 1)[1].split(
    "<!-- project-reflection:lessons:end -->", 1
)[0]
assert registry.count("L-20260901-01") == 1, "Existing lesson was duplicated"
assert_source_unchanged(root, baseline)

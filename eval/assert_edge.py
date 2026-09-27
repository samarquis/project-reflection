import sys
from pathlib import Path

sys.path.insert(0, str(Path.cwd() / "eval"))

from assertions import assert_source_unchanged, load, require_common, score

root, note, memory, baseline = load("edge", 43)
require_common(note)
assert score(note) < 10, "Unproved closure cannot earn 10/10"
assert "unproved" in note.lower(), "Closure was not classified as unproved"
assert "open loop" in note.lower(), "Missing verification open loop"
assert "missing" in note.lower() or "unavailable" in note.lower(), "Missing evidence was not named"
assert memory.count("| supported |") == 1, "Unsupported durable lesson was promoted"
assert_source_unchanged(root, baseline)

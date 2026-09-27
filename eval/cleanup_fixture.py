from __future__ import annotations

import os
import shutil
import stat
import sys
import tempfile
from pathlib import Path


def remove_readonly(function, path: str, _error) -> None:
    os.chmod(path, stat.S_IWRITE)
    function(path)


def main(mode: str) -> None:
    temp = Path(tempfile.gettempdir()).resolve()
    root = (temp / f"project-reflection-eval-{mode}").resolve()
    if root.parent != temp:
        raise RuntimeError("Unsafe fixture path")
    if root.exists():
        shutil.rmtree(root, onexc=remove_readonly)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: cleanup_fixture.py <mode>")
    main(sys.argv[1])

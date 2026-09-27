# Caliper on Windows

Project Reflection's behavioral evaluation uses Caliper. Caliper 0.11.0 may fail before the skill starts when its Codex harness launches an isolated process without Windows runtime environment variables.

Two harness properties are required:

1. Set `CODEX_HOME` to the isolated home directory's `.codex` child so the bundled skill is discovered without changing the user's installed skills.
2. Preserve `SYSTEMROOT` on Windows so `cmd.exe` and dependent runtime components remain discoverable.

Minimal harness logic:

```python
env["CODEX_HOME"] = str(Path(isolated_home) / ".codex")
if sys.platform == "win32" and os.environ.get("SYSTEMROOT"):
    env["SYSTEMROOT"] = os.environ["SYSTEMROOT"]
```

Apply this only to the installed Caliper harness when the upstream version lacks equivalent behavior. Package upgrades can overwrite local patches. Re-run `caliper validate` and one enabled evaluation after every Caliper upgrade.

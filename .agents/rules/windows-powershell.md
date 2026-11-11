---
trigger: always_on
description: Enforces Windows PowerShell native command execution, prohibited bashisms, path formatting, and UTF-8 console safety.
---

# Windows Native & PowerShell First Execution Policy

All commands executed in this environment run on **Windows** using **PowerShell**.

## 1. Prohibited POSIX Bashisms
Never emit Linux/POSIX shell commands in PowerShell. Always use native cmdlets or cross-platform Python scripts:

| Prohibited Bash Command | Native PowerShell Replacement | Python Fallback |
| :--- | :--- | :--- |
| `grep <pattern> <file>` | `Select-String -Path <file> -Pattern "<pattern>"` | `python -c "import re,sys;..."` |
| `cat <file>` | `Get-Content -Path <file>` | `read_file` tool |
| `sed 's/foo/bar/g'` | `(Get-Content <file>) -replace 'foo','bar' \| Set-Content <file>` | `edit_file` tool |
| `awk '{print $1}'` | `ForEach-Object { ($_ -split '\s+')[0] }` | Python script |
| `export VAR="val"` | `$env:VAR="val"` | N/A |
| `rm -rf <dir>` | `Remove-Item -Path <dir> -Recurse -Force` | Python `shutil.rmtree` |
| `mkdir -p <dir>` | `New-Item -ItemType Directory -Force -Path <dir>` | Python `os.makedirs` |
| `touch <file>` | `New-Item -ItemType File -Force -Path <file>` | Python `open(f,'a').close()` |
| `which <cmd>` | `Get-Command <cmd>` | Python `shutil.which` |
| `find . -name "*.ext"` | `Get-ChildItem -Recurse -Filter "*.ext"` | Python `pathlib.Path.rglob` |

## 2. Command Chaining & Redirection Rules
- **No Bash `&&` or `||` in older PowerShell**: Use `;` or `if ($?) { ... }` or PowerShell 7 pipeline chaining cautiously.
- **No Bash `<(...)` process substitution**: Use temporary files or pipeline cmdlets.
- **Path Separation**: Always use forward slashes (`/`) or properly escaped double backslashes (`\\`). Avoid single backslashes in quoted strings.

## 3. Output Stream Bounding
- Never dump thousands of raw log lines into the context.
- Always filter large terminal outputs:
  ```powershell
  Get-ChildItem -Path . | Select-Object -First 30
  git log -n 10 --oneline
  Select-String -Path log.txt -Pattern "ERROR" | Select-Object -First 20
  ```

## 4. UTF-8 Console Safety
- Prevent `cp1252` encoding crashes on Windows:
  - In Python helper scripts, configure stdout encoding:
    ```python
    import sys
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    ```
  - Prefer ASCII status indicators (`[OK]`, `[ERROR]`, `[*]`) over multi-byte Unicode emojis in shell pipelines.

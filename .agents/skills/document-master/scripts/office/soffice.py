"""
Helper for running LibreOffice (soffice) across Windows, Linux, and macOS.
Detects LibreOffice on PATH or in standard OS installation directories.
On Linux sandboxes with restricted AF_UNIX sockets, safely applies a socket shim.

Usage:
    from office.soffice import run_soffice

    result = run_soffice(["--headless", "--convert-to", "pdf", "input.docx"])
"""

import contextlib
import os
import shutil
import socket
import subprocess
import sys
import tempfile
from collections.abc import Iterable
from pathlib import Path


def find_soffice_binary() -> str:
    """Find the soffice binary on PATH or standard OS locations."""
    if "LIBREOFFICE_PATH" in os.environ and os.path.exists(os.environ["LIBREOFFICE_PATH"]):
        return os.environ["LIBREOFFICE_PATH"]

    on_path = shutil.which("soffice") or shutil.which("soffice.exe") or shutil.which("libreoffice")
    if on_path:
        return on_path

    if os.name == "nt":
        candidates = [
            r"C:\Program Files\LibreOffice\program\soffice.exe",
            r"C:\Program Files (x86)\LibreOffice\program\soffice.exe",
            os.path.expandvars(r"%LOCALAPPDATA%\Programs\LibreOffice\program\soffice.exe"),
        ]
        for c in candidates:
            if os.path.exists(c):
                return c
    else:
        for c in [
            "/usr/bin/soffice",
            "/usr/local/bin/soffice",
            "/Applications/LibreOffice.app/Contents/MacOS/soffice",
        ]:
            if os.path.exists(c):
                return c

    return "soffice"


def get_soffice_env() -> dict:
    env = os.environ.copy()
    if os.name != "nt":
        env["SAL_USE_VCLPLUGIN"] = "svp"
        if _needs_shim():
            shim = _ensure_shim()
            if shim:
                env["LD_PRELOAD"] = str(shim)

    return env


def run_soffice(args: Iterable[str], **kwargs) -> subprocess.CompletedProcess:
    args = list(args)
    soffice_bin = find_soffice_binary()

    with contextlib.ExitStack() as stack:
        if not any(str(a).startswith("-env:UserInstallation") for a in args):
            profile = stack.enter_context(
                tempfile.TemporaryDirectory(prefix="lo_profile_", ignore_cleanup_errors=True)
            )
            args = [f"-env:UserInstallation={Path(profile).as_uri()}"] + args

        try:
            return subprocess.run([soffice_bin] + args, env=get_soffice_env(), **kwargs)
        except FileNotFoundError:
            msg = (
                "Error: LibreOffice (soffice) not found on PATH or in standard directories.\n"
                "To enable headless document conversions, install LibreOffice:\n"
                "  Windows: winget install TheDocumentFoundation.LibreOffice\n"
                "  macOS: brew install libreoffice\n"
                "  Linux: sudo apt install libreoffice\n"
            )
            print(msg, file=sys.stderr)
            return subprocess.CompletedProcess(
                args=[soffice_bin] + args, returncode=127, stdout="", stderr="soffice not found"
            )


_SHIM_SO = Path(tempfile.gettempdir()) / "lo_socket_shim.so"


def _needs_shim() -> bool:
    if os.name == "nt":
        return False
    try:
        s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        s.close()
        return False
    except (OSError, AttributeError):
        return True


def _ensure_shim() -> Path | None:
    if os.name == "nt":
        return None
    if _SHIM_SO.exists():
        return _SHIM_SO

    src = Path(tempfile.gettempdir()) / "lo_socket_shim.c"
    src.write_text(_SHIM_SOURCE)
    try:
        subprocess.run(
            ["gcc", "-shared", "-fPIC", "-o", str(_SHIM_SO), str(src), "-ldl"],
            check=True,
            capture_output=True,
        )
        return _SHIM_SO
    except Exception:
        return None
    finally:
        if src.exists():
            src.unlink()


_SHIM_SOURCE = r"""
#define _GNU_SOURCE
#include <dlfcn.h>
#include <errno.h>
#include <fcntl.h>
#include <poll.h>
#include <pthread.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

#define MAX_FDS 1024

static int (*real_socket)(int, int, int);
static int (*real_bind)(int, const struct sockaddr *, socklen_t);
static int (*real_listen)(int, int);
static int (*real_accept)(int, struct sockaddr *, socklen_t *);
static int (*real_connect)(int, const struct sockaddr *, socklen_t);
static int (*real_close)(int);

static void init(void) {
    real_socket  = dlsym(RTLD_NEXT, "socket");
    real_bind    = dlsym(RTLD_NEXT, "bind");
    real_listen  = dlsym(RTLD_NEXT, "listen");
    real_accept  = dlsym(RTLD_NEXT, "accept");
    real_connect = dlsym(RTLD_NEXT, "connect");
    real_close   = dlsym(RTLD_NEXT, "close");
}
"""


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print("Usage: python soffice.py [--headless] [--convert-to <format>] <input_file>")
        print("Cross-platform LibreOffice automation wrapper for document conversions.")
        sys.exit(0)

    result = run_soffice(sys.argv[1:])
    sys.exit(result.returncode)

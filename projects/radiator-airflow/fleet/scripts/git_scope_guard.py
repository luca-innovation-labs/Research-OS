#!/usr/bin/env python3
"""Fail-closed preflight for AIRFLOW local Git/gh operations."""
import re
import subprocess
import sys
from urllib.parse import urlsplit

ALLOWED_REPO = "luca-innovation-labs/Research-OS"
ALLOWED_LOGIN = "luca-innovation-labs"


class ScopeError(Exception):
    pass


def get_repo_from_remote(remote: str) -> str:
    remote = remote.strip()
    scp = re.fullmatch(r"git@github\.com:([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+(?:\.git)?)", remote)
    if scp:
        path = scp.group(1)
    else:
        url = urlsplit(remote)
        if url.hostname != "github.com" or url.scheme not in ("https", "ssh"):
            raise ScopeError("Only github.com HTTPS/SSH remotes are allowed")
        if url.password or (url.scheme == "https" and url.username):
            raise ScopeError("Credential-bearing HTTPS URL not allowed")
        if url.scheme == "ssh" and url.username != "git":
            raise ScopeError("Unexpected SSH user")
        if url.port or url.query or url.fragment:
            raise ScopeError("Unexpected remote parameters")
        path = url.path.lstrip("/")
    if path.endswith(".git"):
        path = path[:-4]
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", path):
        raise ScopeError("Only owner/repository path is allowed")
    return path


def verify_scope(remote: str, login: str) -> None:
    if get_repo_from_remote(remote) != ALLOWED_REPO:
        raise ScopeError("DENY repository not in AIRFLOW allowlist")
    if login.strip() != ALLOWED_LOGIN:
        raise ScopeError("DENY authenticated CLI login is not Innovation")


def read_cmd(args: list[str]) -> str:
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True, timeout=15)
    except (FileNotFoundError, subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
        raise ScopeError("Unable to verify local git/gh login") from exc
    return result.stdout.strip()


def main() -> int:
    try:
        verify_scope(read_cmd(["git", "remote", "get-url", "origin"]),
                     read_cmd(["gh", "api", "user", "--jq", ".login"]))
    except ScopeError as exc:
        print(f"DENY: {exc}", file=sys.stderr)
        return 2
    print(f"ALLOW: {ALLOWED_LOGIN}/{ALLOWED_REPO}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

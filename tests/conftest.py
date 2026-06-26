from __future__ import annotations

from pathlib import Path

import pytest

from ol_ce_sync import git_ops


@pytest.fixture(autouse=True)
def stable_git_line_endings(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("GIT_CONFIG_COUNT", "1")
    monkeypatch.setenv("GIT_CONFIG_KEY_0", "core.autocrlf")
    monkeypatch.setenv("GIT_CONFIG_VALUE_0", "false")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def commit_all(repo: Path, message: str) -> str:
    commit = git_ops.commit_all(repo, message)
    return commit or git_ops.head_commit(repo)

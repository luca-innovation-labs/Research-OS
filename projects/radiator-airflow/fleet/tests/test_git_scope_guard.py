import sys
import unittest
from pathlib import Path
from unittest.mock import patch
from subprocess import CompletedProcess

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from git_scope_guard import ScopeError, get_repo_from_remote, verify_scope, main

class ScopeTests(unittest.TestCase):
    def test_https_ok(self):
        verify_scope("https://github.com/luca-innovation-labs/Research-OS.git","luca-innovation-labs")
    def test_ssh_ok(self):
        verify_scope("git@github.com:luca-innovation-labs/Research-OS.git","luca-innovation-labs")
    def test_ssh_url_ok(self):
        verify_scope("ssh://git@github.com/luca-innovation-labs/Research-OS.git","luca-innovation-labs")
    def test_block_evidor_repo(self):
        with self.assertRaises(ScopeError):
            verify_scope("https://github.com/evidorworkspace-arch/heizkoerper-airflow.git","luca-innovation-labs")
    def test_block_evidor_login(self):
        with self.assertRaises(ScopeError):
            verify_scope("https://github.com/luca-innovation-labs/Research-OS","evidorworkspace-arch")
    def test_block_other_innovation_repo(self):
        with self.assertRaises(ScopeError):
            verify_scope("git@github.com:luca-innovation-labs/medos.git","luca-innovation-labs")
    def test_block_lookalike_host(self):
        with self.assertRaises(ScopeError):
            get_repo_from_remote("https://github.com.bad.invalid/luca-innovation-labs/Research-OS")
    def test_block_embedded_token(self):
        with self.assertRaises(ScopeError):
            get_repo_from_remote("https://user:token@github.com/luca-innovation-labs/Research-OS.git")
    def test_block_nested_path(self):
        with self.assertRaises(ScopeError):
            get_repo_from_remote("https://github.com/luca-innovation-labs/Research-OS/tree/main")
    def test_fail_closed_when_gh_missing(self):
        def fake_run(cmd, **kwargs):
            if cmd[0]=="git":
                return CompletedProcess(cmd,0,stdout="https://github.com/luca-innovation-labs/Research-OS.git\n")
            raise FileNotFoundError()
        with patch("git_scope_guard.subprocess.run",side_effect=fake_run):
            self.assertEqual(main(),2)
    def test_cli_success(self):
        def fake_run(cmd, **kwargs):
            value="https://github.com/luca-innovation-labs/Research-OS.git\n" if cmd[0]=="git" else "luca-innovation-labs\n"
            return CompletedProcess(cmd,0,stdout=value)
        with patch("git_scope_guard.subprocess.run",side_effect=fake_run):
            self.assertEqual(main(),0)

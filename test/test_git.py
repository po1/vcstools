from vcstools import GitClient
from vcstools.vcs_base import VcsError

           
    def test_inject_protection(self):
        client = GitClient(self.local_path)
        try:
            client.is_tag('foo"; bar"', fetch = False)
            self.fail("expected Exception")
        except VcsError: pass
        try:
            client.rev_list_contains('foo"; echo bar"', "foo", fetch = False)
            self.fail("expected Exception")
        except VcsError: pass
        try:
            client.rev_list_contains('foo', 'foo"; echo bar"', fetch = False)
            self.fail("expected Exception")
        except VcsError: pass
        try:
            client.get_version('foo"; echo bar"', fetch = False)
            self.fail("expected Exception")
        except VcsError: pass
        
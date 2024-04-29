import unittest

import python_repos_def as prf

class PythonReposTestCase(unittest.TestCase):
    """Tests for python_repos_def.py."""

    def setUp(self):
        """Call all the functions and test them."""
        self.r = prf.get_repos_info()
        self.repo_dicts = prf.get_repo_dicts(self.r)
        self.repo_dict = self.repo_dicts[0]
        self.names, self.plot_dicts = prf.get_names_plot_dicts(self.repo_dicts)

    def test_get_repos_info(self):
        self.assertEqual(self.r.status_code, 200)

    def test_repo_dicts(self):
        self.assertEqual(len(self.repo_dicts), 30)

        repos_keys = ['name', 'owner', 'stargazers_count', 'html_url']
        for key in repos_keys:
            self.assertTrue(key in self.repo_dict.keys())    

unittest.main()    
import os
import sys
import unittest

repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


class TestRequirements(unittest.TestCase):
    def test_requirements_exclude_stdlib_modules(self):
        with open(os.path.join(repo_root, "requirements.txt")) as f:
            deps = [line.strip() for line in f if line.strip()]
        for dep in deps:
            with self.subTest(dep=dep):
                self.assertNotIn(
                    dep.lower(),
                    sys.stdlib_module_names,
                    f"{dep} is a stdlib module and must not be pip-installed",
                )

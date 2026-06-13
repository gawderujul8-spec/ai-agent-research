import unittest
import os
import shutil
from dependency_analyzer import DependencyAnalyzer
from impact_engine import ImpactEngine

class TestSemanticImpact(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create a clean test_examples directory
        if os.path.exists("test_examples"):
            shutil.rmtree("test_examples")
        os.makedirs("test_examples")

        with open("test_examples/test_utils.py", "w") as f:
            f.write("def helper(): return 1\n")
        with open("test_examples/test_core.py", "w") as f:
            f.write("from test_utils import helper\ndef worker(): return helper()\n")

    def test_dependency_mapping(self):
        analyzer = DependencyAnalyzer("test_examples")
        deps = analyzer.analyze()
        # Full name should be used now
        self.assertIn("test_utils.helper", deps)
        self.assertIn("test_core.worker", deps["test_utils.helper"])

    def test_impact_analysis(self):
        analyzer = DependencyAnalyzer("test_examples")
        deps = analyzer.analyze()
        engine = ImpactEngine(deps)
        # We need to simulate the analyzer finding the impact with module awareness
        modified_file = "test_examples/test_utils.py"
        module_name = "test_utils"

        modified_funcs = engine.get_modified_functions(modified_file)
        self.assertIn("helper", modified_funcs)

        impacted = analyzer.get_impacted_functions(module_name, "helper")
        self.assertEqual(impacted, ["test_core.worker"])

if __name__ == "__main__":
    unittest.main()

import ast

class ImpactEngine:
    def __init__(self, dependency_map):
        self.dependency_map = dependency_map

    def get_modified_functions(self, file_path):
        """
        Parses a file and returns all functions defined in it.
        In a real scenario, this would filter based on a git diff.
        """
        modified_functions = []
        with open(file_path, "r") as f:
            try:
                tree = ast.parse(f.read())
                for node in ast.walk(tree):
                    if isinstance(node, ast.FunctionDef):
                        modified_functions.append(node.name)
            except SyntaxError:
                pass
        return modified_functions

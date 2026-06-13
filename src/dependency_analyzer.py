import ast
import os
from collections import defaultdict

class DependencyAnalyzer:
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.dependencies = defaultdict(list) # target_func_full_name -> [caller_func_full_name]
        self.module_imports = defaultdict(dict) # module_name -> {alias: original_module}

    def analyze(self):
        for root, _, files in os.walk(self.root_dir):
            for file in files:
                if file.endswith(".py"):
                    path = os.path.join(root, file)
                    self._parse_file(path)
        return self.dependencies

    def _parse_file(self, file_path):
        with open(file_path, "r") as f:
            try:
                tree = ast.parse(f.read())
            except SyntaxError:
                return

        module_name = os.path.basename(file_path).replace(".py", "")

        # Pass 1: Collect imports
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    self.module_imports[module_name][alias.asname or alias.name] = alias.name
            elif isinstance(node, ast.ImportFrom):
                for alias in node.names:
                    self.module_imports[module_name][alias.asname or alias.name] = f"{node.module}.{alias.name}"

        # Pass 2: Map function calls
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                caller_full_name = f"{module_name}.{node.name}"

                for child in ast.walk(node):
                    if isinstance(child, ast.Call):
                        target_func = None
                        if isinstance(child.func, ast.Name):
                            # Local call or direct import
                            target_func = self.module_imports[module_name].get(child.func.id, f"{module_name}.{child.func.id}")
                        elif isinstance(child.func, ast.Attribute):
                            # Module.method call
                            if isinstance(child.func.value, ast.Name):
                                base = child.func.value.id
                                if base in self.module_imports[module_name]:
                                    target_func = f"{self.module_imports[module_name][base]}.{child.func.attr}"
                                else:
                                    target_func = f"{base}.{child.func.attr}"

                        if target_func:
                            self.dependencies[target_func].append(caller_full_name)

    def get_impacted_functions(self, module_name, func_name):
        full_name = f"{module_name}.{func_name}"
        return list(set(self.dependencies.get(full_name, [])))

import sys
import os
from dependency_analyzer import DependencyAnalyzer
from impact_engine import ImpactEngine
from ai_summarizer import AISummarizer

def main():
    if len(sys.argv) < 2:
        print("Usage: python reviewer.py <modified_file_path>")
        sys.exit(1)

    modified_file = sys.argv[1]
    project_root = "examples"

    if not os.path.exists(modified_file):
        print(f"Error: File {modified_file} not found.")
        sys.exit(1)

    module_name = os.path.basename(modified_file).replace(".py", "")

    print(f"--- AI Code Reviewer: Semantic Impact Analysis ---")
    print(f"Analyzing changes in: {modified_file}")

    # 1. Map dependencies
    analyzer = DependencyAnalyzer(project_root)
    dependency_map = analyzer.analyze()

    # 2. Analyze impact
    engine = ImpactEngine(dependency_map)
    modified_funcs = engine.get_modified_functions(modified_file)

    summarizer = AISummarizer()

    # 3. Generate AI Report
    found_impact = False
    for func in modified_funcs:
        impacted = analyzer.get_impacted_functions(module_name, func)
        if impacted:
            found_impact = True
            analysis = summarizer.summarize(f"{module_name}.{func}", impacted)

            print(f"\nFunction: {module_name}.{func}")
            print(f"  └─ Impacted downstream functions:")
            for caller in set(impacted):
                print(f"     • {caller}")

            print(f"\n  [AI INSIGHT]")
            print(f"  {analysis['summary']}")
            print(f"  💡 {analysis['insight']}")
            print(f"  🛠️  {analysis['recommendation']}")

    if not found_impact:
        print("\n✅ No downstream logical impacts detected.")

    print("\n-------------------------------------------------")

if __name__ == "__main__":
    main()

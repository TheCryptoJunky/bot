import os
import re

# Define the root directory of the project
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.join(PROJECT_ROOT, 'src')

# Define directories to check and fix relative to the /src/ directory
MODULES_TO_CHECK = ['database', 'list_manager', 'trading', 'safety']

# Regex pattern to match import statements
IMPORT_PATTERN = re.compile(r'^(from|import)\s+(\S+)\s')

def find_imports_in_file(file_path):
    """
    Parse the file to identify any import statements that include modules to be fixed.
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()

    imports = []
    for line in lines:
        match = IMPORT_PATTERN.match(line.strip())
        if match:
            imports.append(line.strip())

    return imports, lines


def fix_import_statements(file_path, imports, lines):
    """
    Fix import statements by adjusting the module root if necessary.
    """
    modified = False
    new_lines = []

    for line in lines:
        modified_line = line
        for imp in imports:
            # Check if the import involves one of the problematic modules
            for module in MODULES_TO_CHECK:
                if f"from {module}" in imp or f"import {module}" in imp:
                    # Check if module needs src prefix and add it if not present
                    if f"from src.{module}" not in imp and f"import src.{module}" not in imp:
                        # Replace the line with the corrected import
                        modified_line = line.replace(f"from {module}", f"from src.{module}")
                        modified_line = modified_line.replace(f"import {module}", f"import src.{module}")
                        print(f"Fixed import in {file_path}: {imp} -> {modified_line.strip()}")
                        modified = True

        new_lines.append(modified_line)

    # If modifications were made, overwrite the file
    if modified:
        with open(file_path, 'w') as f:
            f.writelines(new_lines)


def fix_imports_in_project():
    """
    Walk through the /src directory and fix import statements in Python files.
    """
    for root, dirs, files in os.walk(SRC_DIR):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                # Find imports in the file
                imports, lines = find_imports_in_file(file_path)
                # Fix imports if necessary
                if imports:
                    fix_import_statements(file_path, imports, lines)

if __name__ == '__main__':
    print(f"Checking the /src/ directory for import path issues in {MODULES_TO_CHECK}...")
    fix_imports_in_project()
    print("All import path issues should now be fixed.")

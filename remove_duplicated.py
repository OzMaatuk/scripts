import subprocess

import re

def convert_lines(filename):
  """Converts lines in a file by adding "==" after package names and whitespace.

  Args:
      filename: The name of the file to convert.
  """
  with open(filename, 'r') as file:
    lines = file.readlines()
  
  # Regex pattern to match package name followed by whitespace
  pattern = r"(?<!\S)\s+(?!\S)"
  
  # Convert lines using a loop with regex replacement
  converted_lines = []
  for line in lines:
    new_line = re.sub(pattern, "==", line)
    converted_lines.append(new_line + "\n")  # Add newline explicitly

  # Write converted lines back to the file
  with open(filename, 'w') as file:
    file.writelines(converted_lines)
# convert_lines("D:\Workspace\stock-prediction-deep-neural-learning\\requierments.txt")

def get_installed_packages():
    """
    Get a list of installed packages using pip.
    """
    result = subprocess.run(["pip", "list"], stdout=subprocess.PIPE, text=True)
    lines = result.stdout.splitlines()
    packages = []

    for line in lines:
        parts = line.split()
        package_name = parts[0]
        packages += [package_name]

    return packages

def uninstall_duplicated_packages(packages):
    """
    Uninstall duplicated packages.
    """
    for package in packages:
        subprocess.run(["pip", "uninstall", "-y", package])

import subprocess

def get_mamba_installed_packages():
    """
    Get a list of installed packages using mamba.
    """
    try:
        result = subprocess.run(["mamba", "list"], stdout=subprocess.PIPE, text=True)
        lines = result.stdout.splitlines()
        packages = []

        for line in lines:
            parts = line.split()
            package_name = parts[0]
            packages += [package_name]

        return packages
    except FileNotFoundError:
        print("Mamba is not installed or not in your system PATH.")
        return []

def main():
    # Get installed packages via pip
    pip_packages = get_installed_packages()

    mamba_packages = get_mamba_installed_packages()

    # Find duplicated packages
    duplicated_packages = set(pip_packages) & set(mamba_packages)

    if duplicated_packages:
        print("Duplicated packages found:")
        for package in duplicated_packages:
            print(f"- {package}")
        print("\nUninstalling duplicated packages...")
        # uninstall_duplicated_packages(duplicated_packages)
        print("Duplicated packages removed successfully.")
    else:
        print("No duplicated packages found.")

if __name__ == "__main__":
    main()

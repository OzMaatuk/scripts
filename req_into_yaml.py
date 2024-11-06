import requests
import re

def verify_package(package, version):
    url = f"https://pypi.org/pypi/{package}/json"
    try:
        response = requests.get(url)
        data = response.json()
        releases = data.get("releases", {})
        if version in releases:
            return True
        else:
            print(f"Invalid version for package {package}: {version}")
            return False
    except requests.RequestException:
        print(f"Error fetching package information for {package}")
        return False

def extract_package_info(line):
    match = re.match(r"([\w-]+)==([\d.]+)", line)
    if match:
        return match.group(1), match.group(2)
    return None, None

def main():
    requirements_file = "requirements.txt"
    yaml_file = "environment.yaml"

    with open(requirements_file, "r") as req_file:
        requirements = req_file.readlines()

    valid_packages = []
    invalid_packages = []

    for line in requirements:
        package, version = extract_package_info(line.strip())
        if package:
            if verify_package(package, version):
                valid_packages.append(f"  - {package}=={version}\n")
            else:
                invalid_packages.append(f"Skipping invalid package: {package}=={version}\n")

    with open(yaml_file, "w") as yaml:
        yaml.write("name: stocks\n")
        yaml.write("channels:\n")
        yaml.write("  - defaults\n")
        yaml.write("  - conda-forge\n")
        yaml.write("dependencies:\n")
        yaml.writelines(valid_packages)

    print("Conversion completed successfully!")
    print("Valid packages added to environment.yaml.")
    print("Invalid packages skipped:")
    for invalid in invalid_packages:
        print(invalid)

if __name__ == "__main__":
    main()

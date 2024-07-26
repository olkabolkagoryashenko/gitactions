import yaml
import sys

def validate_yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            yaml_content = yaml.safe_load(file)
            print(f"{file_path} is a valid YAML file.")
            return True
    except yaml.YAMLError as exc:
        print(f"Error in {file_path}: {exc}")
        return False
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return False
    except Exception as e:
        print(f"Unexpected error while reading {file_path}: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_yaml.py <path_to_yaml_file>")
    else:
        file_path = sys.argv[1]
        validate_yaml(file_path)

import os

def rename_directories_to_lowercase(start_path):
    for root, dirs, files in os.walk(start_path, topdown=False):  # Process from deepest level up
        for dir_name in dirs:
            current_path = os.path.join(root, dir_name)
            new_name = dir_name.lower()
            new_path = os.path.join(root, new_name)
            if current_path != new_path:
                os.rename(current_path, new_path)
                print(f"Renamed: {current_path} -> {new_path}")

if __name__ == "__main__":
    # Set the path to your project's root directory
    project_root = os.path.abspath(os.path.dirname(__file__))  # Adjust this if running elsewhere
    rename_directories_to_lowercase(project_root)
    print("All nested directories have been renamed to lowercase.")

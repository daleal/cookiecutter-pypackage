import shutil
import subprocess
import json
import os


# CLEANUP

MANIFEST_FILE = "manifest.json"

def cleanup_disabled_features():
    print("Cleaning up...")
    with open(MANIFEST_FILE) as manifest_file:
        manifest = json.load(manifest_file)
    for feature in manifest["features"]:
        if not feature["enabled"]:
            print(f"Removing resources for disabled feature {feature['name']}...")
            for resource in feature["resources"]:
                remove_resource(resource)
    remove_resource(MANIFEST_FILE)
    print("Cleanup complete")


def remove_resource(resource):
    if os.path.isfile(resource):
        print(f"Removing file: {resource}")
        os.remove(resource)
    elif os.path.isdir(resource):
        print(f"Removing directory: {resource}")
        shutil.rmtree(resource)


# ENVIRONMENT SETUP

def build_environment():
    print("Building the environment...")
    create_virtual_environment()
    install_dependencies()
    print("The environment is ready")


def create_virtual_environment():
    subprocess.call(["python3", "-m", "venv", ".venv"])


def install_dependencies():
    subprocess.call(["poetry", "run", "pip", "install", "--upgrade", "pip"])
    subprocess.call(["poetry", "run", "poetry", "install"])


# GIT INITIALIZATION

def execute_git_initialization():
    print("Initializing git repository...")
    initialize_git_repository()
    initial_git_commit()
    print("git initialization complete")


def initialize_git_repository():
    subprocess.call(["git", "init"])


def initial_git_commit():
    subprocess.call(["git", "add", "."])
    subprocess.call(["git", "commit", "-m", "'Initial commit'"])


if __name__ == "__main__":
    cleanup_disabled_features()
    build_environment()
    execute_git_initialization()

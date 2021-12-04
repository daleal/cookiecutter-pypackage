import shutil
import subprocess
import json
import os


# CLEANUP

MANIFEST_FILE = "manifest.json"

def cleanup_disabled_features():
    print("⚒ Cleaning up...")
    with open(MANIFEST_FILE) as manifest_file:
        manifest = json.load(manifest_file)
    for feature in manifest["features"]:
        if not feature["enabled"]:
            for resource in feature["resources"]:
                remove_resource(resource)
    remove_resource(MANIFEST_FILE)
    print("✔ Cleanup complete")


def remove_resource(resource):
    if os.path.isfile(resource):
        os.remove(resource)
    elif os.path.isdir(resource):
        shutil.rmtree(resource)


# ENVIRONMENT SETUP

def build_environment():
    print("⚒ Building the environment...")
    try:
        create_virtual_environment()
        install_dependencies()
        print("✔ The environment is ready")
    except subprocess.CalledProcessError:
        print(
            "❌ The environment could not be built, you can do it later "
            "using the included command `make build-env`."
        )


def create_virtual_environment():
    subprocess.check_call(["python3", "-m", "venv", ".venv"])


def install_dependencies():
    subprocess.check_call(
        ["poetry", "run", "pip", "install", "--upgrade", "pip"]
    )
    subprocess.check_call(["poetry", "run", "poetry", "install"])


# GIT INITIALIZATION

def execute_git_initialization():
    print("⚒ Initializing git repository...")
    try:
        initialize_git_repository()
        initial_git_commit()
        print("✔ git initialization complete")
    except subprocess.CalledProcessError:
        print("❌ The git repository could not be correctly initialized.")


def initialize_git_repository():
    subprocess.check_call(["git", "init"])


def initial_git_commit():
    subprocess.check_call(["git", "add", "."])
    subprocess.check_call(["git", "commit", "-m", "'Initial commit'"])


if __name__ == "__main__":
    cleanup_disabled_features()
    build_environment()
    execute_git_initialization()

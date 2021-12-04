import os
import shutil
import json


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
    print("Cleanup complete.")


def remove_resource(resource):
    if os.path.isfile(resource):
        print(f"Removing file: {resource}")
        os.remove(resource)
    elif os.path.isdir(resource):
        print(f"Removing directory: {resource}")
        shutil.rmtree(resource)


if __name__ == "__main__":
    cleanup_disabled_features()

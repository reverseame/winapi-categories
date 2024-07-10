#!/usr/bin/python3
# RazviOverflow
import sys
import json

"""
Script used to parse winapi_categories.json and detect functions 
that are missing arguments (if any). Uses hooks_h.json to fill the missing info.
"""

def update_missing_info(winapi_categories, hooks_h_json):
    """
    Loads two JSON files and updates missing "return_type" and "n_args" entries in the first file using the second file.

    Args:
    winapi_categories: Path to the first JSON file.
    hooks_h_json: Path to the second JSON file.
    """
    with open(winapi_categories) as winapi_cat, open(hooks_h_json) as hooks_h:
        winapi_cat_json = json.load(winapi_cat)
        hooks_h_json = json.load(hooks_h)

    for entry in winapi_cat_json:
        try:
            if not winapi_cat_json[entry]["return_type"] and winapi_cat_json[entry]["n_arguments"] == 0:
                winapi_cat_json[entry]["return_type"] = hooks_h_json[entry]["return_type"]
                winapi_cat_json[entry]["n_arguments"] = hooks_h_json[entry]["n_arguments"]
                winapi_cat_json[entry]["arguments"] = hooks_h_json[entry]["arguments"]
        except Exception as e:
            print(f"Error detected for entry {entry}: {e} - {repr(e)}")
            pass

    return winapi_cat_json

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print(f"\n[!] Invoke the script like: {sys.argv[0]} winapi_categories.json hooks_h.json\n")
        sys.exit()

    winapi_categories = sys.argv[1]
    hooks_h = sys.argv[2]

    winapi_cat_json = update_missing_info(winapi_categories, hooks_h)

    json.dump(winapi_cat_json, open(winapi_categories,"w"), indent=4)

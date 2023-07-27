#!/usr/bin/python3
# RazviOverflow

import json
import sys

if __name__ == '__main__':
	with open(sys.argv[1]) as f:
		json_data = json.load(f)

	categories = []
	for function in json_data:
		category = json_data[function]['category']
		if category not in categories:
			categories.append(category)

	with open("categories.txt", "w") as f:
		json.dump(categories, f, indent=4)
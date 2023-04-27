#!/usr/bin/python3
# RazviOverflow

import json

if __name__ == '__main__':
	with open("winapi_categories.json") as f:
		json_data = json.load(f)

	categories_and_functions = {}
	for function in json_data:
		category = json_data[function]['category']
		if category not in categories_and_functions:
			categories_and_functions[category] = []
		categories_and_functions[category].append(function)

	with open("winapi_functions_by_category.json", "w") as f:
		json.dump(categories_and_functions, f, indent=4)
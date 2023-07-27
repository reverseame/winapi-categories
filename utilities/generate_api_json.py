#!/usr/bin/python3
# RazviOverflow

import os, json, sys

if __name__ == "__main__":
	json_files_path = sys.argv[1]
	json_files = os.listdir(json_files_path)
	all_apis = {}
	print(f"[*] Reading files from {json_files_path}.")
	for json_file in json_files:
		json_file = json_files_path + '/' + json_file
		with open(json_file) as file:
			data = json.load(file)
			for api_call in data:
				all_apis[api_call['name']] = {}
				all_apis[api_call['name']]['category'] = api_call['category']
				all_apis[api_call['name']]['dll'] = api_call['dll']
				all_apis[api_call['name']]['header'] = api_call['header']
				all_apis[api_call['name']]['return_type'] = api_call['return_type']
				all_apis[api_call['name']]['n_arguments'] = api_call['n_arguments']
				all_apis[api_call['name']]['arguments'] = api_call['arguments']
		print(f"[*] Finished parsing {json_file}.")	
	with open("winapi_categories.json", "w") as file:
		json.dump(all_apis, file, indent=4)
	print(f"[*] Wrote all data to winapi_categories.json.")

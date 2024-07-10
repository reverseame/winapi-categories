#!/usr/bin/python3
# RazviOverflow
import sys
import re
import json

"""
Script used to parse hooks.h from capemon (CAPE's monitor) and extract the arguments
for those functions from winapi_categories.json that are missing them (if any)
"""

def parse_hookdef(file_content):
    functions = {}
    n_functions = 0
    
    # Split the content by lines
    lines = file_content.splitlines()
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Check if the line starts with HOOKDEF
        if line.startswith('HOOKDEF'):
            n_functions += 1
            parts = line.split(',')
            if line.startswith('HOOKDEF_NOTAIL'):
                func_name = parts[1].strip()
            else:
                func_name = parts[2].strip()

            # Get the return type
            return_type = parts[0].split('(')[1]
            
            # Find the opening parenthesis of the arguments list
            #args_start_idx = line.find('(', line.find(func_name)) + 1
            
            # Collect all lines of arguments until we find the closing parenthesis
            args_lines = []
            j = i + 1
            while not ");" in lines[j].strip():
                args_lines.append(lines[j].strip())
                j += 1
            #args_lines.append(lines[j].strip()[:-2])  # Remove trailing ');'
            
            #print(f"Arguments: {args_lines}")
            arguments = []
            skip = False
            for i,arg in enumerate(args_lines):
                # Controlling the arg lines that are broken with a \n
                if skip:
                    skip = False
                    continue
                # If the current argument line does not end with a comma and
                # the next line is not a closing parenthesis, it means the argument
                # is split among two lines. Combine them and skip next iteration.
                if not arg.endswith(",") and lines[i+1] != ");":
                    arg += lines[i+1]
                    skip = True
                arg_parts = arg.split()
                if len(arg_parts) == 2:
                    in_out = "(n/a)"
                    arg_type = arg_parts[0]
                    arg_name = arg_parts[1].rstrip(',')
                else:
                    in_out = arg_parts[0]
                    arg_type = arg_parts[1]
                    arg_name = arg_parts[2].rstrip(',')
                    
                argument = {
                    "in_out": f"_{in_out.strip('_')}_",
                    "type": arg_type,
                    "name": arg_name,
                    "description": f"Type: {arg_type} {arg_name.replace('_', ' ').title()}."
                }
                arguments.append(argument)
            
            functions[func_name] = {
                "return_type": return_type,
                "n_arguments": len(arguments),
                "arguments": arguments
            }
    print(f"Parsed {n_functions} HOOKDEFs")
    return functions

if __name__ == "__main__":
    print("You can get hooks.h from:\n\thttps://raw.githubusercontent.com/kevoreilly/capemon/capemon/hooks.h; or\n\thttps://raw.githubusercontent.com/reverseame/capemon/capemon/hooks.h")

    if len(sys.argv) != 2:
        print(f"\n[!] Invoke the script like: {sys.argv[0]} hooks.h\n")
        sys.exit()

    hooks_h = sys.argv[1]

    with open(hooks_h, "r") as file:
        functions_dict = parse_hookdef(file.read())

    with open("hooks_h.json", "w") as file:
        json.dump(functions_dict, file, indent=4);
    print("Results dumped to hooks_h.json.")
# Windows API and Syscall categories
Classification of Windows API (WinAPI) functions and system calls (syscalls), including the Native API (NTAPI), according to their category. Presented in JSON format for you research and automation needs. 

In this repo, we use the terms Windows API or WinAPI to refer to what was (and still is nowadays) widely known as Win32 API, as recommended by [Microsoft](https://learn.microsoft.com/en-us/windows/win32/apiindex/windows-api-list):
> Note that this was formerly called the Win32 API. The name Windows API more accurately reflects its roots in 16-bit Windows and its support on 64-bit Windows

### The main files of this repository are:
- [winapi_categories.json](./winapi_categories.json) is the main file of the repo. Contains all the functions and syscalls with their corresponding category and arguments.
- [winapi_functions_by_category.json](./winapi_functions_by_category.json) enumerates all the categories and the functions and syscalls each one of them comprises.
- [categories.txt](./categories.txt) contains a list with all the categories.

## Usage
The JSON file comprising all MSDN API calls is already provided with the repo ([winapi_categories.json](./winapi_categories.json)).

The [`utilities`](./utilities) folder contains several scripts used to create and modify the collection of WinAPI functions and syscalls. 

If you need to re-create the repository from [Vadim's original repo](https://github.com/vadimkotov/winapi-json), you can do it like so:  
`python3 generate_api_json.py ../winapi-json/api_by_category`  
or just  
`./generate_api_json.py ../winapi-json/api_by_category`  
where `/winapi/api_by_category` is the directory created after cloning the (original) aforementioned repo.

## Structure
The resulting JSON file has the following structure. The `dict` structure was chosen with Python optimization in mind. Feel free to change it according to your needs:
```
{
	'API_name':{
		'category':'cat',
		'dll':'dll',
		'header':'header',
		'return_type':'type',
		'n_arguments':INT,
		'arguments':[{
			'in_out':'in_out',
			'type':'type',
			'name':'arg_name',
			'description':'descr',
			},
			{...},
			{...}]
	}
}
```

**ATTENTION!**: Only `API_NAME` and `category` are guaranteed to be present in the dict ([winapi_categories.json](./winapi_categories.json) file). If you find any incorrect, malformed or just missing entry, feel free *(you are more than welcome to)* to contribute to the project!

## Authors
[Razvan Raducu](https://github.com/RazviOverflow)  
[Ricardo J. Rodríguez](https://webdiis.unizar.es/~ricardo/)  
[Pedro Álvarez](https://scholar.google.es/citations?hl=en&user=Ups00hgAAAAJ)

## Caveats
If you see several `\t\t\t` in certain `description` fields, just ignore them or `.strip()` it when parsing. That's because the original repo also [contains them](https://github.com/vadimkotov/winapi-json/blob/master/api_by_category/dynamic_data_exchange_management.json#L26).

## Acknowledgments
This repo is based on [winapi-json](https://github.com/vadimkotov/winapi-json).

## TODO
Pending entries to review, fulfill or fix:
```
MoveFileWithProgressTransacted
GlobalCompact
GlobalFix
GlobalUnfix
_hread
_hwrite
IsBadHugeReadPtr
IsBadHugeWritePtr
StgOpenAsyncDocfileOnIFillLockBytes
SetWindowWord
malloc
URLDownloadToFile
```

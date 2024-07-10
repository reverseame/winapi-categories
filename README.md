# WinAPI and syscalls with categories in JSON format
Classification of Windows API (WinAPI) functions and system calls (syscalls), including the Native API and Win32, according to their category. 

The list of categories defined can be found in [categories.txt](./categories.txt).

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

### Authors
[Razvan Raducu](https://github.com/RazviOverflow)  
Ricardo J. Rodíguez  
Pedro Álvarez  

### Caveats
If you see several `\t\t\t` in certain `description` fields, just ignore them or `.strip()` it when parsing. That's because the original repo also [contains them](https://github.com/vadimkotov/winapi-json/blob/master/api_by_category/dynamic_data_exchange_management.json#L26).

## Acknowledgments
This repo is a revamp of [winapi-json](https://github.com/vadimkotov/winapi-json) for your research and automation needs.

### TODO
Pending entries to review, fulfill or fix:
```
GlobalCompact
GlobalFix
GlobalUnfix
_hread
_hwrite
IsBadHugeReadPtr
_lcreat
_llseek
IsBadHugeWritePtr
_lclose
_lopen
ReadClassStg
StgCreateDocfile
StgIsStorageFile
StgOpenAsyncDocfileOnIFillLockBytesKeyError
StgOpenStorage
WriteClassStm
WriteFmtUserTypeStg
SetICMMode
SetWindowsHook
SetWindowWord
TranslateMDISysAccel
UpdateICMRegKey
VerLanguageName
malloc
GetFileVersionInfo
GetFileVersionInfoSize
Module32First
Module32Next
SetupDiGetClassDevs
URLDownloadToFile
```
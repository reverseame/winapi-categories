# Win API calls with categories in JSON format
This repo provides a classification of Windows API (WinAPI) functions, including the Native API and Win32, according to their category. This repo is a revamp of [winapi-json](https://github.com/vadimkotov/winapi-json) for your research and automation needs.

The list of categories defined can be found in [categories.txt](./categories.txt).


## Usage
The JSON file comprising all MSDN API calls is already provided with the repo ([winapi_categories.json](./winapi_categories.json)).

Nevertheless, if you need to modify the script or re execute it, do it like so:  
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

### Caveats
If you see several `\t\t\t` in certain `description` fields, just ignore them or `.strip()` it when parsing. That's because the original repo also [contains them](https://github.com/vadimkotov/winapi-json/blob/master/api_by_category/dynamic_data_exchange_management.json#L26).
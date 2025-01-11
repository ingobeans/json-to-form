# json to form

tool to convert json data to an html form. useful for trying out potential CSRF attacks.

can convert both to a regular form, but also [a fake json form](https://dant0x65.medium.com/json-csrf-a1594955dd75). a fake json form's body will be mostly identical to a regular post request with json data, although the content-type header will be text/plain rather than application/json.

if not using fake json, this will skip any subkeys since they cant be represented in a regular form.

you can pass either a json object directly or the path to a file.

usage (on windows powershell):

- `python main.py --data '{"my data":"wahoo"}'`
- `python main.py --path data.json`
- `python main.py --path data.json --fakejson`

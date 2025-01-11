# json to form

tool to convert json data to an html form. useful for trying out potential CSRF attacks.

will skip any subkeys since they cant be represented in a form.

you can pass either a json object directly or the path to a file.

usage (powershell): 
  * `python main.py '{"my data":"wahoo"}'`
  * `python main.py data.json`

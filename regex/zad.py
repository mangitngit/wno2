import re
with open("tekst.txt") as file:
    tekst = file.read()

# pattern = r'[a-zA-Z0-9\"]+@[a-zA-Z0-9]+[.][a-zA-Z0-9_.+-]+'

# pattern = r'\w+@\w+\.\w+'
# pattern = r'".+"@\w+\.\w+'
# pattern = r'\w+@\[.+\]'
# pattern = r'"\S*"@\w+.\w+'
# pattern = r'"\s"@\w+.\w+'

# pattern = r'[a-zA-Z0-9\"]+@\w+[a-zA-Z0-9\"\.]\w+'
pattern = r'(((\"[a-zA-Z0-9\"\ \\]+\")|([a-zA-Z0-9.@]+)|( \[.+\]))@((\[[a-zA-Z0-9\:]+\])|(\w+[\.]\w+)|(com)|(org)|^(qor)))'
m = re.findall(pattern, tekst)
for ad in m:
    print(ad[0])

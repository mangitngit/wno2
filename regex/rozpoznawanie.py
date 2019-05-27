import re

with open("tekst.txt") as file:
    tekst = file.read()

pattern = r'\w+@\w+\.\w+'
m = re.search(pattern, tekst)
print(m.group(0))

pattern = r'".+"@\w+\.\w+'
m = re.search(pattern, tekst)
print(m.group(0))

pattern = r'\w+@\[.+\]'
m = re.search(pattern, tekst)
print(m.group(0))

pattern = r'"\S*"@\w+.\w+'
m = re.findall(pattern, tekst)

for i in m:
    print(i)

pattern = r'"\s"@\w+.\w+'
m = re.search(pattern, tekst)
print(m.group(0))

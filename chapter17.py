import re

line = "The gohst that says boo haunts the loo"
found = re.findall(".oo", line)
for match in found:
    print (match)

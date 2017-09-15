import re

a = re.match(r'^([\d])\1([\w])\2$','11aa')
if a is not  None:
    print("yes")
else:
    print('no')
import re
s = "My Name is         Satyam        Tiwari"
s = re.sub(" +", " ",s)
print(s)
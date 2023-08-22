import re
names=[]
emails=[]
address=[]
phone=[]

with open(r"data.txt") as file:
    file=file.read()
pattern_name = re.compile(r'(?<! )[A-Z][a-z]+\s[A-z][a-z]+')
name_matches = pattern_name.finditer(file)
for match in name_matches:
    names.append(match.group(0))

pattern_emails = re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.[a-z]+')
email_matches = pattern_emails.finditer(file)
for match in email_matches:
    emails.append(match.group(0))

pattern_phone = re.compile(r'\d{3}.\d{3}.\d{4}')
phone_matches = pattern_phone.finditer(file)
for match in phone_matches:
    phone.append(match.group(0))

pattern_add = re.compile(r'\d{3} [A-Z][a-z]+\sSt\.,\s[A-Z][a-z]+\s[A-Z]{2}\s\d{5}')
add_matches = pattern_add.finditer(file)
for match in add_matches:
    address.append(match.group(0))

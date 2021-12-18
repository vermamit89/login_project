import re

format='^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'

def validate(email):
    return re.search(format,email)



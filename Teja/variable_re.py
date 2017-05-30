import re
def variableName(name):
    return True if not name[0].isdigit() and re.match("^[a-zA-Z0-9_][5]$", name) else False

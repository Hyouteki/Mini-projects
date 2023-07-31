from sys import argv

variableDict = dict()
parsedCommands: list = list()


def handleDefineCommands(command: str):
    """Checks for #define in command"""
    strip: list[str] = command.split()
    if len(strip) >= 2 and strip[0] == "#define":
        if len(strip) == 2:
            variableDict[strip[1]] = ""
            return True
        if len(strip) == 3:
            variableDict[strip[1]] = strip[2]
            return True
    return False


# lifecycle
if len(argv) == 1:
    exit(1)
try:
    file = open(argv[1], "r")
except FileNotFoundError:
    exit(1)
commands = file.readlines()
file.close()
for command in commands:
    if not handleDefineCommands(command):
        for variable in variableDict:
            if variable in command:
                command = command.replace(variable, variableDict[variable])
        parsedCommands.append(command)
exec("".join(parsedCommands))

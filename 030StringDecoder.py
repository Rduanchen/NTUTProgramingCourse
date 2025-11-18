initAmount, commandAmount = map(int, input().split())


def assignValue(variables, command):
    vars, values = command.split("=")
    # vars
    vars = vars.split(",")
    values = values.split(",")
    for var, value in zip(vars, values):
        value = value.strip()
        variables[var.strip()] = value.strip("'")
        # print(f"Assign {type(value)} {value} to {var.strip()}")


def removePrint(command):
    value = command[command.find("(") + 1 : command.find(")")]
    return value


def stringAddition(variables, command):
    vars, values = command.split("=")
    values = values.split("+")
    adding = []
    for i in values:
        i = i.strip()
        if i in variables:
            adding.append(variables[i])
        else:
            adding.append(i.strip("'"))

    variables[str(vars[0])] = "".join(adding)


def stringSlicing(variables, command):
    command = removePrint(command)
    var = command[0 : command.find("[")]
    slicing = command[command.find("[") + 1 : command.find("]")]
    sliceValue = slicing.split(":")
    sliceValue = [int(i) if i != "" else None for i in sliceValue]
    match (len(sliceValue)):
        case 1:  # [index]
            return variables[var][sliceValue[0]]
        case 2:  # [start, end]
            return variables[var][sliceValue[0] : sliceValue[1]]
        case 3:  # [start, end, step]
            return variables[var][sliceValue[0] : sliceValue[1] : sliceValue[2]]


def main():
    variables = {}
    stack = []
    for init in range(initAmount):
        command = input()
        assignValue(variables, command)
    for command in range(commandAmount):
        cmd = input()
        if cmd.startswith("print(") and cmd.endswith(")"):
            if "[" in cmd or "]" in cmd:
                stack.append(stringSlicing(variables, cmd))
            else:
                var = removePrint(cmd)
                stack.append(variables[var])
        elif "=" in cmd and "+" in cmd:
            stringAddition(variables, cmd)
    for i in stack:
        print(i)


main()

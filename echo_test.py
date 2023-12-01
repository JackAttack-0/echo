"""
The test module of the language Echo:
"""
executor = []
errors = []
listVariables = []
debug = []
line = ""
multiLineComment = False

while line != "end":
    line = input("")
    executor.append(list(line))
    
print(executor)
executor.pop(-1)
for i in range(len(executor)):
    varName = []
    varValue = []
    varType = ""
    try:
        if executor[i][0] == "/":
            try:
                if executor[i][1] == "*":
                    debug.append("Comment, Multi-Line, begins")
                    multiLineComment == True
                    continue
            except IndexError:
                debug.append("Comment, Single-Line")
        elif executor[i][0] == 0:
            debug.append("Comment, Single-Line")
            continue
        if "".join(executor[i][:2]) == "*/":
            multiLineComment = False
            debug.append("Comment, Multi-Line, ends")
            continue
        if (multiLineComment == True) & (executor[i][:2] != "*/"):
            debug.append("Comment, Multi-Line, continues")
            continue
        if (executor[i][-1] != ";") & (multiLineComment == False) & (executor[i][0] != "/"):
            errors.append([i,"TypeError","Line missing ';'"])
        if "".join(executor[i][:4]) == "var ":
            if executor[i][4] == "?":
                varType = "boolean"
                j = 5
                while executor[i][j] != " ":
                    varName.append(executor[i][j])
                    j = j+1
                try:
                    if "".join(executor[i][j:j+3]) == " = ":
                        j = j+3
                        while executor[i][j] != ";":
                            varValue.append(executor[i][j])
                            j = j+1
                        varValue = "".join(varValue)
                        if (varValue == "True") or (varValue == "False"):
                            varValue = "".join(varValue)
                        else:
                            errors.append([i, "ValueError", "Type 'bool' cannot have value '" + varValue + "'. Can only have 'True' or 'False'"])
                            continue
                        varName = "".join(varName)
                        debug.append("Variable " + varName + " with type " + varType + " created wth value " + varValue)
                        for k in range(len(listVariables)):
                            if listVariables[k][1] == varName:
                                errors.append(i, "VariableError", "Variable alreay defined")
                                continue
                except IndexError:
                    errors.append(i, "IndexError", "Index out of range")
                listVariables.append([varType, varName, varName])
            if executor[i][4] == "_":
                varType = "string"
                j = 5
                while executor[i][j] != " ":
                    varName.append(executor[i][j])
                    j = j+1
                try:
                    if "".join(executor[i][j:j+3]) == " = ":
                        j = j+3
                        while executor[i][j] != ";":
                            varValue.append(executor[i][j])
                            j = j+1
                        varValue = "".join(varValue)
                        if type(varValue) == type("Hello World"):
                            varValue = "".join(varValue)
                        else:
                            errors.append([i, "ValueError", "Type 'string' cannot have value '" + varValue + "'. Can only have strings."])
                            continue
                        varName = "".join(varName)
                        debug.append("Variable " + varName + " with type " + varType + " created wth value " + varValue)
                        for k in range(len(listVariables)):
                            if listVariables[k][1] == varName:
                                errors.append(i, "VariableError", "Variable alreay defined")
                                continue
                except IndexError:
                    errors.append(i, "IndexError", "Index out of range")
                listVariables.append([varType, varName, varName])
            if executor[i][4] == "#":
                varType = "int"
                j = 5
                while executor[i][j] != " ":
                    varName.append(executor[i][j])
                    j = j+1
                try:
                    if "".join(executor[i][j:j+3]) == " = ":
                        j = j+3
                        while executor[i][j] != ";":
                            varValue.append(executor[i][j])
                            j = j+1
                        varValue = "".join(varValue)
                        if type(varValue) == type(100):
                            varValue = "".join(varValue)
                        else:
                            errors.append([i, "ValueError", "Type 'int' cannot have value '" + varValue + "'. Can only have intergers."])
                            continue
                        varName = "".join(varName)
                        debug.append("Variable " + varName + " with type " + varType + " created wth value " + varValue)
                        for k in range(len(listVariables)):
                            if listVariables[k][1] == varName:
                                errors.append(i, "VariableError", "Variable alreay defined")
                                continue
                except IndexError:
                    errors.append([i, "IndexError", "Index out of range"])
                listVariables.append([varType, varName, varName])
            if executor[i][4] == "-":
                varType = "float"
                j = 5
                while executor[i][j] != " ":
                    varName.append(executor[i][j])
                    j = j+1
                try:
                    if "".join(executor[i][j:j+3]) == " = ":
                        j = j+3
                        while executor[i][j] != ";":
                            varValue.append(executor[i][j])
                            j = j+1
                        varValue = "".join(varValue)
                        if type(varValue) == type(10.5):
                            varValue = "".join(varValue)
                        else:
                            errors.append([i, "ValueError", "Type 'float' cannot have value '" + varValue + "'. Can only have intergers."])
                            continue
                        varName = "".join(varName)
                        debug.append("Variable " + varName + " with type " + varType + " created wth value " + varValue)
                        for k in range(len(listVariables)):
                            if listVariables[k][1] == varName:
                                errors.append(i, "VariableError", "Variable alreay defined")
                                continue
                except IndexError:
                    errors.append([i, "IndexError", "Index out of range"])
                listVariables.append([varType, varName, varName])
    except IndexError:
        if executor[i] == []:
            debug.append("Empty Line")
for i in range(len(errors)):
    print("-> ERROR: Line " + str(errors[i][0]))
    print(errors[i][1] + ": " + errors[i][2])
print("DEBUG")
for i in range(len(debug)):
    print("Line " + str(i+1) + ": " + debug[i])

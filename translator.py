def assignmentCheck(x):
    # This function checks if a given string is a python assignment statement.
    if '=' in x:
        return True
    return False

def assignmentParse(x):
    # This function returns a C-formatted assignment statement from a given python assigment statement
    variableName = findName(x)
    variableType = findType(x)
    variableValue = findValue(x)
    if variableType[-1] == 0:
        return variableType[0] + " " + variableName + " = " + findValue(x) + ";\n"
    return variableType[0] + " " + variableName + "[{}]".format(variableValue[-1]) + " = " + findValue(x) + ";\n"

def findName(x):
    # This function returns the variable name from a python assignment statement
    return (x.split())[0]

def findValue(x):
    # This function returns a string of the value of a python assignment statement
    return (x.split())[2]

def arrayParse(x):
    # This function checks if a list, dictionary, or tuple assigment is in a string x
    return ""

def findType(x):
    joinedString = ""
    if arrayParse(x):
        return " " 
    splitline = x.split()
    try:
        result = eval(splitline[-1])
    except:
        # Add support for lists, dicts, etc. This is not a 100% implementation.
        print("in exception")
        return ("char", len(splitline[-1]) - 2)
    #print(str(result))
    print(str(type(result)), "line 37 in code")
    print (((str(type(result))).split())[-1], "line 38 in code")
    typing = ((str(type(result))).split())[1]
    typeOutput = [] 
    for letter in typing:
        print(letter)
        if letter != '\"' and letter != '\'' and letter != '>':
            typeOutput.append(letter) 
    typestring = joinedString.join(typeOutput)
    if typestring == 'str':
        return ("char", (len(splitline[-1]) - 2))
    return (typestring, 0)

def parseLine(x):
    # This function parses a given input line from the main file reader.
    if assignmentCheck:
        return assignmentParse(x)
    return "\n"

filename = input("Enter filename: ")
fileoutput = open('out.c', 'w')
fileoutput.writelines(['#include <stdio.h>\n', '\n', '\n', 'int main() {\n'])

leftParens = 1
with open(filename, 'r') as infile:
    for line in infile:
        fileoutput.write(leftParens * '\t' + parseLine(line))
fileoutput.close()
fileoutput = open('out.c', 'a')
fileoutput.writelines(['\n', '\treturn 0;', '\n', '}'])
fileoutput.close()



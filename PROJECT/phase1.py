import re


ID = "[a-zA-Z]\w*"
num = "[0-9]+"
assign = ":="
ending = ";"
If = "if"
Then = "then"
Else = "else"
End = "end"
Eq = "=="
lt = "[<]"
lteq = "<="
gt = "[>]"
gteq = ">="
compSigns = f"{Eq}|{lteq}|{lt}|{gteq}|{gt}"
c = f"({ID}|{num}|{assign}|{ending}|{If}|{Then}|{End}|{Else}|{compSigns})"
k = f"({If}|{Then}|{Else}|{End})"
statement = f"(\s*{ID}\s+{assign}\s+({ID}|{num})\s*{ending}\s*)"
compstat = f"(\s*{ID}\s*({compSigns})\s*({ID}|{num}))"
RegEx = f"(^\s*({statement}\s+)*{If}\s+({num}|{compstat})\s+{Then}\s+(({statement})+)\s*({Else}\s+(({statement})+)\s*)?\s*{End}$)"

print("--------------------------------------------")

text = input("Enter your code: ")

y = re.search(RegEx, text)

if y:
    print("------------------------------------------------")
    print("The input matches the regular expression")
    print("------------------------------------------------")
else:
    print("------------------------------------------------")
    print("Input Mismatch")
    print("------------------------------------------------")


identifier = re.findall(ID, text)

for i in identifier:
    if i == "if" or i == "then" or i == "else" or i == "end":
        identifier.remove(i)
for i in identifier:
    if i == "then":
        identifier.remove(i)

number = re.findall(num, text)
assign = re.findall(assign, text)
ending = re.findall(ending, text)
keyword = re.findall(k, text)
allInput = re.findall(c, text)
comparison = re.findall(compSigns, text)

print("the token type is identifier " + str(identifier))
print("the token type is number " + str(number))
print("the token type is assignment operator " + str(assign))
print("the token type is semicolon " + str(ending))
print("the token type is reserved word " + str(keyword))
print("the token type is comparison operator " + str(comparison))
print(str(allInput))

state = 0
my_list = []
my_list.append(state)
for i in allInput:
#At state error
   if state == 'error':
       break

#At state 0
   elif state == 0:
       if i == 'if':
           state = 1
           my_list.append(state)
       elif i in identifier:
           state = 101
       else:
           state = 'error'
           my_list.append(state)

#If the program starts with a statement
   elif state == 101:
       if i in assign:
           state = 102
   elif state == 102:
       if i in number:
           state = 103
   elif state == 103:
       if i in ending:
           state = 0
           my_list.append(state)

# At state 1
   elif state == 1:
       if i in number:
           state = 2
           my_list.append(state)
       elif i in identifier:
           state = 3
           my_list.append(state)
       else:
           state = 'error'
           my_list.append(state)

#At state 2
   elif state == 2:
       if i in 'then':
           state = 7
           my_list.append(state)
       else:
           state= 'error'
           my_list.append(state)

#At state 3
   elif state == 3:
       if i in comparison:
           state = 4
           my_list.append(state)
       else:
           state = 'error'
           my_list.append(state)

# At state 4
   elif state == 4:
       if i in number:
           state = 5
           my_list.append(state)
       elif i in identifier:
           state = 6
           my_list.append(state)
       else:
           state = 'error'
           my_list.append(state)

# At state 5
   elif state == 5:
       if i in 'then':
           state = 7
           my_list.append(state)
       else:
           state = 'error'
           my_list.append(state)

# At state 6
   elif state == 6:
       if i in 'then':
           state = 7
           my_list.append(state)
       else:
           state = 'error'
           my_list.append(state)

# At state 7
   elif state == 7:
       if i in identifier:
           state = 8
           my_list.append(state)
       else:
           state = 'error'
           my_list.append(state)

# At state 8
   elif state == 8:
       if i in assign:
           state = 9
           my_list.append(state)
       else:
           state = 'error'
           my_list.append(state)

# At state 9
   elif state == 9:
       if i in number:
           state = 10
           my_list.append(state)
       elif i in identifier:
           state = 11
           my_list.append(state)
       else:
           state = 'error'
           my_list.append(state)

# At state 10
   elif state == 10:
       if i in ending:
           state = 12
           my_list.append(state)
       else:
           state = 'error'
           my_list.append(state)

# At state 11
   elif state == 11:
       if i in ending:
           state = 12
           my_list.append(state)
       else:
           state = 'error'
           my_list.append(state)

# At state 12
   elif state == 12:
       if i in identifier:
           state = 8
           my_list.append(state)
       elif i in 'else':
           state = 7
           my_list.append(state)
       elif i in 'end':
           state = 13
           my_list.append(state)
       else:
           state = 'error'
           my_list.append(state)

print("The states changes in this order respectively: " + str(my_list))
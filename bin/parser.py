# class Functions:
#     valid_function = {
#         'SIN()'
#         'COS()'
#         'TAN()'
#     }

#     def __init__(self, name):
#         self._name = name

#     def __repr__(self):
#         return f'{self._name} ({self._species})'

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self):
#         if name in self.valid_function:
#             print(0)
#             return 0
#         else:
#             print(1)
#             return 1


# tan = Functions('TAN()')
# print(vars(tan))
# print(tan.name)

valid_operations = {
    '+'
    '-'
    '*'
    '/'
}

print("Intructions:")
print("Subfunctions include constants")
print("Example subfunctions: '2sin(x)', 'e^x', 'log'x', '10+x'")
print("Do NOT enter 2 subfunctions together [e.g. log(10+x)].")
print("Instead, enter separately as log(x) and 10+x.")

numFxns = int(input("How many subfunctions?")) #initialize as user input number
f_list = []

i = 0
while i < numFxns:
    fxn = input("Function %s:" %(i+1)).upper()
    # if fxn is a valid function, append it, otherwise try again
    f_list.append(fxn)
    print(f_list)
    i+=1

orderString = ""

print("Instructions:")
print("Denote multiplication operation (if necessary) before parentheses")

j = 0
open_par = 0
closed_par = 0
eval_brackets = 0
par_depth = 0
bracket_depth = 0

while j < numFxns:
    q1 = input("Open parentheses? (y/n)").upper()
    if q1 == "Y":
        orderString += "("
        open_par += 1
        par_depth += 1
        print(orderString)
    else:
        pass

    if open_par > closed_par:
        q2 = input("Close parentheses? (y/n)").upper()
        if q2 == "Y":
            orderString += ")"
            closed_par += 1
            par_depth -= 1
            print(orderString)
        else:
            pass
    
    q3 = input("Operation? (y/n)").upper()
    if q3 == "Y":
        op = input("Which operation? (+,-,*,/)")
        if op in valid_operations:
            orderString += op
            print(orderString)
        else:
            raise ValueError
    else:
        pass

    next_fxn = int(input("What is the number of the next subfunction?"))
    orderString += "[Fxn" + str(next_fxn) + "]"
    print(orderString)

    q4 = input("Will this function be evaluated at another subfunction? (y/n)").upper()
    if q4 == "Y":
        orderString += "{"
        eval_brackets += 1
        print(orderString)

    else:
        if eval_brackets > 0:
            q5 = input("Close evaluation brackets? (y/n)").upper()
            if q5 == "Y":
                orderString += "}"
                eval_brackets -= 1
                print(orderString)
            else:
                pass

    j+=1

while eval_brackets > 0:
    print("Resolving open brackets...")
    orderString += "}"
    eval_brackets -= 1


while open_par > closed_par:
    print("Resolving open parentheses...")
    orderString += ")"
    closed_par += 1

print(orderString)

#right now very dependent on user integrity
#can be improved with some try... except error testing
#need some sort of check at the end for how to resolve open brackets/parentheses
#also have to figure out how to distinguish parentheses within eval brackets from outside them
#maybe assign each an index of depth, but seems like we could leave it up to user
#bracket + parentheses problem can prob be solved with index of depth of equation
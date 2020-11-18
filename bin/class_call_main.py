from function_library_v1 import function_library
from CMobject import CMobject
from FuncObj import FuncObj
import numpy as np

def main():
    with open('Read_in1.txt', 'r') as file:
        function_string_main = file.read().replace('\n', '')

    with open('Read_in2.txt', 'r') as file:
        function_list_raw = file.read().replace('\n', '')

    print(function_string_main)
    print(function_list_raw)

    function_list_main = function_list_raw.split()

    build_function(function_string_main, function_list_main)


def build_function(function_string_in, function_list_in):
    op_string = ["+", "-", "*", "/", "**"]
    brack_string = ["[", "]", "(", ")", "{", "}"]
    trimmed_string = ""
    for i in function_string_in:
        if i != " ":
            trimmed_string = trimmed_string + i
            if i in op_string:
                print(i, i in op_string)
            if i in brack_string:
                print(i, i in op_string)


    print(trimmed_string)


    ## handling the definition and specification of the library variables
    check_string1 = 'sin(x)'
    check_string2 = 'cos(x)'
    check_string3 = 'exp(x)'
    check_string4 = 'tan(x)'
    x1 = CMobject(0)
    x2 = CMobject(np.pi)
    x3 = np.pi
    f1 = FuncObj(check_string1, x1)
    f2 = FuncObj(check_string2, x1)
    f3 = FuncObj(check_string2, x3)
    print("f1 value, der: {}, {}".format(f1.val, f1.der) )
    print("f2 value, der: {}, {}".format(f2.val, f2.der) )
    print("f3 value, der: {}, {}".format(f3.val, f3.der) )

    seed = CMobject(1.0)
    f4 = 2*FuncObj(check_string1, seed) + ((FuncObj(check_string3, seed))/(4*FuncObj(check_string4, 3*seed)))
    f5 = 2*FuncObj(check_string1, seed)
    f6 = (FuncObj(check_string3, seed))/(4*FuncObj(check_string4, 3*seed))
    f7 = FuncObj(check_string1, FuncObj(check_string4, FuncObj(check_string3, seed)))
    f8 = FuncObj(check_string1, seed)**(FuncObj(check_string4, seed)) + 2**(FuncObj(check_string2, seed)) + FuncObj(check_string1, seed)**(FuncObj(check_string4, seed))**(FuncObj(check_string3, seed))

    print("f4 value, deriv: {}, {}".format(f4.val, f4.der) )
    print("f5 value, deriv: {}, {}".format(f5.val, f5.der) )
    print("f6 value, deriv: {}, {}".format(f6.val, f6.der) )
    print("f7 value, deriv: {}, {}".format(f7.val, f7.der) )
    print("f8 value, deriv: {}, {}".format(f8.val, f8.der) )

if __name__ == "__main__":
    main()

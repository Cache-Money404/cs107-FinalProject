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
    op_string = ["+", "-", "*", "/", "^"]
    brack_string = ["[", "]", "(", ")", "{", "}"]
    trimmed_string = ""
    for i in function_string_in:
        if i != " ":
            trimmed_string = trimmed_string + i
            # if i in op_string:
            #     print(i, i in op_string)
            # if i in brack_string:
            #     print(i, i in op_string)
    print(trimmed_string)


    ## handling the definition and specification of the library variables
    sin_string = 'sin(x)'
    cos_string = 'cos(x)'
    exp_string = 'exp(x)'
    tan_string = 'tan(x)'
    log_string = 'ln(x)'

    x1 = CMobject(1.0)

    ## the following is a test case for: sin(tan(x)) + 2^(cos(x)) + sin(x)^tan(x)^exp(x) - (cos(x))^2, seeded at x = 1. Try it in autograd, it works.
    test_func1 = FuncObj(sin_string, FuncObj(tan_string, x1)) + 2**(FuncObj(cos_string, x1)) + FuncObj(sin_string, x1)**(FuncObj(tan_string, x1))**(FuncObj(exp_string, x1)) - FuncObj(cos_string, x1)**2
    print("test_func1 val, der: {}, {}".format(test_func1.val, test_func1.der))

if __name__ == "__main__":
    main()

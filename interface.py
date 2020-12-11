def Interface():
    stop = 0
    while stop == 0:
        string1 = "Enter Potential Flow Vizualization: \n 1) uniform \n 2) doublet \n 3) sink \n 4) source \n 5) sphere \n 6) vortex \n 7) corner \n 8) exit \ n"
        
        input1 = float(input(string1))
        if input1 == 8: #Exit
            stop = 1
        else:
            if input1 == 1: #Uniform
                string2 = "Enter Strength?:"
                input2 = float(input(string2))
                d = dict();
                d['Strength'] = input2
                d['function'] = "Uniform"
                return d

            elif input1 == 2: # Doublet
                string2 = "Enter Strength?:"
                input2 = float(input(string2))
                string3  = "Enter X Value"
                inputx = float(input(string3))
                string4  = "Enter Y Value"
                inputy = float(input(string4))
                d = dict();
                d['X'] = inputx
                d['Y'] = inputy
                d['Strength'] = input2
                d['function'] = "Doublet"
                return d
            elif input1 == 3: # Sink
                string2 = "Enter Strength?:"
                input2 = str(input(string2))

                string5  = "Enter Length"
                input3 = float(input(string5))

                string3  = "Enter X Value"
                inputx = float(input(string3))
                string4  = "Enter Y Value"
                inputy = float(input(string4))
                d = dict();
                d['X'] = inputx
                d['Y'] = inputy
                d['Strength'] = input2
                d['Length'] = input3
                d['function'] = "Sink"

                return d
            elif input1 == 4: # Source
                string2 = "Enter Strength?:"
                input2 = str(input(string2))


                string5  = "Enter Length"
                input3 = float(input(string5))
                
                string3  = "Enter X Value"
                inputx = float(input(string3))
                string4  = "Enter Y Value"
                inputy = float(input(string4))

                d = dict();
                d['X'] = inputx
                d['Y'] = inputy
                d['Strength'] = input2
                d['Length'] = input3
                return d
            elif input1 == 5: #Sphere
                string2 = "Enter Strength?:"
                input2 = str(input(string2))
            
                string3  = "Enter X Value"
                inputx = float(input(string3))
                string4  = "Enter Y Value"
                inputy = float(input(string4))

                d = dict();
                d['X'] = inputx
                d['Y'] = inputy
                d['Strength'] = input2
                d['function'] = "Sphere"
                return d                
    
            elif input1 == 6: # Vortex
                string2 = "Enter Strength?:"
                input2 = str(input(string2))
                
                string3  = "Enter X Value"
                inputx = float(input(string3))

                string4  = "Enter Y Value"
                inputy = float(input(string4))

                d = dict();
                d['X'] = inputx
                d['Y'] = inputy
                d['Strength'] = input2
                d['function'] = "Vortex"
                return d                

            elif input1 == 7: # Corner
                string2 = "Enter Scale ?:"
                input2 = str(input(string2))
            
                string3  = "Enter X Value"
                inputx = float(input(string3))

                string4  = "Enter Y Value"
                inputy = float(input(string4))

                d = dict();
                d['X'] = inputx
                d['Y'] = inputy
                d['Scale'] = input2
                d['function'] = "Corner"
                return d
            else:
                raise Exception("Invalid input")
        return print('Exiting out of function')
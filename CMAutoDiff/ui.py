class graphDim():
    def __init__(self):
        self._xlow = 0
        self._xhigh = 0
        self._ylow = 0
        self._yhigh = 0

    def __str__(self):
        return(str(self._xlow)+" "+str(self._xhigh)+" "+str(self._ylow)+" "+str(self._yhigh))

    @property
    def xl(self):
        return self._xlow
    @property
    def xh(self):
        return self._xhigh
    @property
    def yl(self):
        return self._ylow
    @property
    def yh(self):
        return self._yhigh

    @xl.setter
    def xl(self, into):
        self._xlow = into
    @xh.setter
    def xh(self, into):
        self._xhigh = into
    @yl.setter
    def yl(self, into):
        self._ylow = into
    @yh.setter
    def yh(self, into):
        self._yhigh = into
        
def Interface():
    stop = 0
    while stop == 0:
        string1 = "Enter Potential Flow Vizualization: \n 1) uniform \n 2) doublet \n 3) sink \n 4) source \n 5) sphere \n 6) vortex \n 7) corner \n 8) tornado \n 9) Whirlpool \n 10) Rankine Half-body \n 11) vortex row \n 12) Rankine oval \n 13) exit \n"

        input1 = float(input(string1))
        if input1 == 13: #Exit
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
                input2 = float(input(string2))

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
                input2 = float(input(string2))


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
                input2 = float(input(string2))

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
                input2 = float(input(string2))

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
                input2 = float(input(string2))

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

            elif input1 == 8: # Tornado
                string2 = "Enter strength ?:"
                input2 = float(input(string2))

                string5 = "Enter vorticity ?:"
                input4 = float(input(string5))

                string3  = "Enter X Value"
                inputx = float(input(string3))

                string4  = "Enter Y Value"
                inputy = float(input(string4))

                d = dict();
                d['X'] = inputx
                d['Y'] = inputy
                d['Strength'] = input2
                d['Vorticity'] = input4
                d['function'] = "Tornado"
                return d

            elif input1 == 9: # Whirlpool
                string2 = "Enter strength ?:"
                input2 = float(input(string2))

                string5 = "Enter vorticity ?:"
                input4 = float(input(string5))

                string3  = "Enter X Value"
                inputx = float(input(string3))

                string4  = "Enter Y Value"
                inputy = float(input(string4))

                d = dict();
                d['X'] = inputx
                d['Y'] = inputy
                d['Strength'] = input2
                d['Vorticity'] = input4
                d['function'] = "Whirlpool"
                return d

            elif input1 == 10: # Rankine Half Body
                string2 = "Enter strength ?:"
                input2 = float(input(string2))

                string5 = "Enter width ?:"
                input4 = float(input(string5))

                string3  = "Enter X Value"
                inputx = float(input(string3))

                string4  = "Enter Y Value"
                inputy = float(input(string4))

                d = dict();
                d['X'] = inputx
                d['Y'] = inputy
                d['Strength'] = input2
                d['Width'] = input4
                d['function'] = "Rankine Half Body"
                return d

            elif input1 == 11: # Vortex Row
                string2 = "Enter strength ?:"
                input2 = float(input(string2))

                string4 = "Enter spacing ?:"
                input4 = float(input(string4))

                string3  = "Enter Height"
                inputh = float(input(string3))

                d = dict();
                d['Height'] = inputh
                d['Strength'] = input2
                d['spacing'] = input4
                d['function'] = "Vortex Row"
                return d

            elif input1 == 12: # Rankine Oval
                string2 = "Enter strength ?:"
                input2 = float(input(string2))

                string5 = "Enter velocity ?:"
                input4 = float(input(string5))

                string3  = "Enter Height"
                inputh = float(input(string3))

                string4  = "Enter Width"
                inputw = float(input(string4))

                d = dict();
                d['Height'] = inputh
                d['Width'] = inputw
                d['Strength'] = input2
                d['velocity'] = input4
                d['function'] = "Rankine Oval"
                return d

            else:
                raise Exception("Invalid input")
        return print('Exiting out of function')

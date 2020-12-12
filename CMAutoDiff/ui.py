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

# test = graphDim()
# print(test)
#
# test.xl = -10
# test.yh = 10
# test.yl = 5
# print(test)

def Interface():
    stop = 0
    while stop == 0:
        string1 = "Enter Potential Flow Vizualization: \n 1) uniform \n 2) doublet \n 3) sink \n 4) source \n 5) sphere \n 6) vortex \n 7) corner \n 8) exit \ n"

        input1 = float(input(string1))
        if input1 == 8: #Exit
            stop = 1
        else:
            if input1 == 1: #Uniform
                string2 = "Enter A as this is the letter that coresponds to function Uniform:"
                input2 = str(input(string2))
                if input2 =="A" or input2=='a':
                    d = dict();
                    d['Property'] = "A"
                    d['function'] = "Uniform"
                    return d
                else:
                    raise Exception("Invalid input")

            elif input1 == 2: # Doublet
                string2 = "Enter Q as this is the letter that coresponds to function Doublet:"
                input2 = str(input(string2))

                if input2 =="Q" or input2=='q':
                    string3  = "Enter X Value"
                    inputx = float(input(string3))
                    string4  = "Enter Y Value"
                    inputy = float(input(string4))
                    d = dict();
                    d['X'] = inputx
                    d['Y'] = inputy
                    d['Property'] = "Q"
                    d['function'] = "Doublet"

                    return d
                else:
                    raise Exception("Invalid input")

            elif input1 == 3: # Sink
                string2 = "Enter Q as this is the letter of the property that coresponds to function Sink:"
                input2 = str(input(string2))

                if input2 =="Q" or input2=='q':
                    string3  = "Enter X Value"
                    inputx = float(input(string3))
                    string4  = "Enter Y Value"
                    inputy = float(input(string4))

                    d = dict();
                    d['X'] = inputx
                    d['Y'] = inputy
                    d['Property'] = "Q"
                    d['function'] = "Sink"

                    return d
                else:
                    raise Exception("Invalid input")

            elif input1 == 4: # Source
                string2 = "Enter Q as this is the letter of the property that coresponds to function Source:"
                input2 = str(input(string2))

                if input2 =="Q" or input2=='q':
                    string3  = "Enter X Value"
                    inputx = float(input(string3))
                    string4  = "Enter Y Value"
                    inputy = float(input(string4))

                    d = dict();
                    d['X'] = inputx
                    d['Y'] = inputy
                    d['Property'] = "Q"
                    d['function'] = "Source"
                    return d
                else:
                    raise Exception("Invalid input")

            elif input1 == 5: #Sphere
                string2 = "Enter R as this is the letter of the property that coresponds to function Sphere:"
                input2 = str(input(string2))

                if input2 =="R" or input2 =='r':
                    string3  = "Enter X Value"
                    inputx = float(input(string3))
                    string4  = "Enter Y Value"
                    inputy = float(input(string4))

                    d = dict();
                    d['X'] = inputx
                    d['Y'] = inputy
                    d['Property'] = "R"
                    d['function'] = "Sphere"
                    return d
                else:
                    raise Exception("Invalid input")

            elif input1 == 6: # Vortex
                string2 = "Enter Q as this is the letter of the property that coresponds to function Vortex:"
                input2 = str(input(string2))
                if input2 =="R" or input2 =='r':
                    string3  = "Enter X Value"
                    inputx = float(input(string3))

                    string4  = "Enter Y Value"
                    inputy = float(input(string4))

                    d = dict();
                    d['X'] = inputx
                    d['Y'] = inputy
                    d['Property'] = "R"
                    d['function'] = "Vortex"
                    return d
                else:
                    raise Exception("Invalid input")

            elif input1 == 7: # Corner
                string2 = "Enter Q as this is the letter of the property that coresponds to function Corner:"
                input2 = str(input(string2))
                if input2 =="R" or input2=='r':
                    string3  = "Enter X Value"
                    inputx = float(input(string3))

                    string4  = "Enter Y Value"
                    inputy = float(input(string4))

                    d = dict();
                    d['X'] = inputx
                    d['Y'] = inputy
                    d['Property'] = "A"
                    d['function'] = "Corner"
                    return d

                else:
                    raise Exception("Invalid input")
        return print('Exiting out of function')

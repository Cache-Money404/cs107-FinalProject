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
    d = {}
    count_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while stop == 0:
        string1 = "Enter Potential Flow Vizualization: \n 1) uniform \n 2) doublet \n 3) sink \n 4) source \n 5) sphere \n 6) vortex \n 7) corner \n 8) tornado \n 9) Whirlpool \n 10) Rankine Half-body \n 11) vortex row \n 12) Rankine oval \n 13) exit \n
        input1 = float(input(string1))
        if input1 == 13: #Exit
            stop = 1
        else:
            if input1 == 1: #Uniform
                string2 = "Enter Strength?:"
                input2 = float(input(string2))
                count_list[input1] += 1
                d['uniform'+count_list[input1]] = [input2]

            elif input1 == 2: # Doublet
                list_it = []
                string2 = "Enter Strength:"
                string3  = "Enter X Value:"
                string4  = "Enter Y Value:"
                list_it.append(float(input(string2)))
                list_it.append(float(input(string3)))
                list_it.append(float(input(string4)))
                count_list[input1] += 1
                d['doublet'+count_list[input1]] = list_it
            elif input1 == 3: # Sink
                list_it = []
                string2 = "Enter Strength:"
                string3  = "Enter Length:"
                string4  = "Enter X Value:"
                string5  = "Enter Y Value:"
                list_it.append(float(input(string2)))
                list_it.append(float(input(string3)))
                list_it.append(float(input(string4)))
                list_it.append(float(input(string5)))
                count_list[input1] += 1
                d['sink'+count_list[input1]] = list_it
            elif input1 == 4: # Source
                list_it = []
                string2 = "Enter Strength:"
                string3  = "Enter Length:"
                string4  = "Enter X Value:"
                string5  = "Enter Y Value:"
                list_it.append(float(input(string2)))
                list_it.append(float(input(string3)))
                list_it.append(float(input(string4)))
                list_it.append(float(input(string5)))
                count_list[input1] += 1
                d['source'+count_list[input1]] = list_it

            elif input1 == 5: #Sphere
                list_it = []
                string2 = "Enter Strength:"
                string3  = "Enter X Value:"
                string4  = "Enter Y Value:"
                list_it.append(float(input(string2)))
                list_it.append(float(input(string3)))
                list_it.append(float(input(string4)))
                count_list[input1] += 1
                d['sphere'+count_list[input1]] = list_it

            elif input1 == 6: # Vortex
                list_it = []
                string2 = "Enter Strength:"
                string3  = "Enter X Value:"
                string4  = "Enter Y Value:"
                list_it.append(float(input(string2)))
                list_it.append(float(input(string3)))
                list_it.append(float(input(string4)))
                count_list[input1] += 1
                d['vortex'+count_list[input1]] = list_it

            elif input1 == 7: # Corner
                list_it = []
                string2 = "Enter scale:"
                string3  = "Enter X Value:"
                string4  = "Enter Y Value:"
                list_it.append(float(input(string2)))
                list_it.append(float(input(string3)))
                list_it.append(float(input(string4)))
                count_list[input1] += 1
                d['corner'+count_list[input1]] = list_it

            elif input1 == 8: # Tornado
                list_it = []
                string2 = "Enter Strength:"
                string3  = "Enter Vorticity:"
                string4  = "Enter X Value:"
                string5  = "Enter Y Value:"
                list_it.append(float(input(string2)))
                list_it.append(float(input(string3)))
                list_it.append(float(input(string4)))
                list_it.append(float(input(string5)))
                count_list[input1] += 1
                d['tornado'+count_list[input1]] = list_it

            elif input1 == 9: # Whirlpool
                list_it = []
                string2 = "Enter Strength:"
                string3  = "Enter Vorticity:"
                string4  = "Enter X Value:"
                string5  = "Enter Y Value:"
                list_it.append(float(input(string2)))
                list_it.append(float(input(string3)))
                list_it.append(float(input(string4)))
                list_it.append(float(input(string5)))
                count_list[input1] += 1
                d['whirlpool'+count_list[input1]] = list_it

            elif input1 == 10: # Rankine Half Body
                list_it = []
                string2 = "Enter Strength:"
                string3  = "Enter Width:"
                string4  = "Enter X Value:"
                string5  = "Enter Y Value:"
                list_it.append(float(input(string2)))
                list_it.append(float(input(string3)))
                list_it.append(float(input(string4)))
                list_it.append(float(input(string5)))
                count_list[input1] += 1
                d['rankine_half_body'+count_list[input1]] = list_it

            elif input1 == 11: # Vortex Row
                list_it = []
                string2 = "Enter Strength:"
                string3  = "Enter Spacing:"
                string4  = "Enter Height:"
                list_it.append(float(input(string2)))
                list_it.append(float(input(string3)))
                list_it.append(float(input(string4)))
                count_list[input1] += 1
                d['vortex_row'+count_list[input1]] = list_it

            elif input1 == 12: # Rankine Oval
                string2 = "Enter Velocity:"
                string3  = "Enter Strength:"
                string4  = "Enter Height:"
                string5  = "Enter Width:"
                list_it.append(float(input(string2)))
                list_it.append(float(input(string3)))
                list_it.append(float(input(string4)))
                list_it.append(float(input(string5)))
                count_list[input1] += 1
                d['rankine_oval'+count_list[input1]] = list_it
            else:
                print("Invalid input, returning to top")
        return print('Exiting out of function')

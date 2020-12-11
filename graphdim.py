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


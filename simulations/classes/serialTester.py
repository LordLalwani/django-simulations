from simulationTestingBase import SimulationTestingBase;

class SerialTester(SimulationTestingBase):
    def __init__(self, freq=0):
        self.__freq = freq;

    def setup(self):
        print("setting up SERIAL connection on frequency: {}".format(self.__freq))
        pass
    
    def setFreq(self, freq):
        self.__freq = freq;

    def getFreq(self):
        return self.__freq;
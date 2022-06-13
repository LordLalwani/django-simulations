from abc import ABC, abstractmethod

class SimulationTestingBase(ABC):

    @abstractmethod
    def setup(self):
        pass;
    
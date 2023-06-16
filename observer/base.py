from abc import ABC
from abc import abstractmethod


class ObserverBase(ABC):
    @abstractmethod
    def execute(self, data):
        pass
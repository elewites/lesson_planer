# Observer interface/base class
from abc import ABC, abstractmethod


class ControllerObserver(ABC):
    @abstractmethod
    def update(self, source_controller):
        pass

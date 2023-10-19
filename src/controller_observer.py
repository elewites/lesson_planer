# Observer interface/base class
from abc import ABC, abstractmethod


from abc import ABC, abstractmethod


class Observer(ABC):
    """
    An abstract class representing an observer in an observer pattern.
    Observers can monitor changes in different application components.

    Attributes:
        source_component: The component that initiated the update.

    Methods:
        update(source_component): Called when the observed component changes.
    """

    @abstractmethod
    def update(self, source_component):
        """
        Respond to changes in an observed component.

        Args:
            source_component: The component that initiated the update.
        """
        pass

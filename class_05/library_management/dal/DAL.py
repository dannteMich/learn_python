from abc import ABC, abstractmethod


class Dal(ABC):

    @abstractmethod
    def get_all(self) -> list:
        raise NotImplementedError("This is not implemented")

    @abstractmethod
    def add(self, new_object) -> None:
        raise NotImplementedError("This is not implemented")

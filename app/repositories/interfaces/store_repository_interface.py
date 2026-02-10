from abc import ABC, abstractmethod

class StoreRepositoryInterface(ABC):
    @abstractmethod
    def get_all(self) -> dict:
        pass
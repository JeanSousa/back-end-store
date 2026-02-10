from app.repositories.interfaces.store_repository_interface import (
    StoreRepositoryInterface
)


class StoreService:
    def __init__(self, repository: StoreRepositoryInterface):
        self.repository = repository

    def list_stores(self) -> dict:
        return self.repository.get_all()
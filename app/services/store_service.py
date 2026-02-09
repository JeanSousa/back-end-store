from app.repositories.store_repository import StoreRepository


class StoreService:
    def __init__(self):
        self.repository = StoreRepository()

    def list_stores(self) -> dict:
        return self.repository.get_all()
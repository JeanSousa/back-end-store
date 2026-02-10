from app.repositories.interfaces.store_repository_interface import (
    StoreRepositoryInterface
)

class StoreRepository(StoreRepositoryInterface):
    def get_all(self) -> dict:
        # mock por enquanto (simula banco)
        return { "stores": [{"name": "blackbuster", "phone": "55 16 98885-1555"}]}
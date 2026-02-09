class StoreRepository:
    def get_all(self) -> dict:
        # mock por enquanto (simula banco)
        return { "stores": [{"name": "blackbuster", "phone": "55 16 98885-1555"}]}
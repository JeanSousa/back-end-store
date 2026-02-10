from typing import Annotated

from fastapi import Header, HTTPException

from app.repositories.store_repository import StoreRepository
from app.services.store_service import StoreService


async def get_token_header(x_token: Annotated[str, Header()]):
    if not isinstance(x_token, str):
        raise HTTPException(status_code=400, detail="X-Token header invalid")


# composition
def get_store_service() -> StoreService:
    repository = StoreRepository()
    return StoreService(repository)
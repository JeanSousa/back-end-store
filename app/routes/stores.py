from fastapi import APIRouter, Depends

from ..dependencies import get_token_header, get_store_service
from app.schemas.store import StoreCreate
from app.services.store_service import StoreService

router = APIRouter(
    prefix="/stores",
    tags=["Stores"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not Found"}}
)


@router.get("")
def get_stores(service: StoreService = Depends(get_store_service)):
    return service.list_stores()

@router.post("")
def create_store(
    store: StoreCreate
):
    return {"message": "Store created successfuly"}

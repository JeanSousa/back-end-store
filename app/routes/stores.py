from fastapi import APIRouter, Depends

from ..dependencies import get_token_header

router = APIRouter(
    prefix="/stores",
    tags=["Stores"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not Found"}}
)


@router.get("")
def get_stores():
    return { "stores": [{"name": "blackbuster", "phone": "55 16 98885-1555"}]}

@router.post("")
def create_store():
    return {"message": "Store created successfuly"}

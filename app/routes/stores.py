from fastapi import APIRouter

router = APIRouter()


@router.get('/stores', tags=['Stores'])
def get_stores():
    return { "stores": [{"name": "blackbuster", "phone": "55 16 98885-1555"}]}
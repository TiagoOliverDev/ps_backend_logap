from fastapi import APIRouter

router = APIRouter()

@router.get("/list/")
async def list():
    return [{"username": "user1"}, {"username": "user2"}]



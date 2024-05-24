from fastapi import APIRouter

router = APIRouter(
  tags=['chat']
)

@router.post('chat')
async def chat():
  return {
    'test': 'Ok'
  }
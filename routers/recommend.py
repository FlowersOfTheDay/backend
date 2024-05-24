from fastapi import APIRouter

router = APIRouter(
  tags=['recommend']
)

@router.post('recommend')
async def recommend():
  return {
    'test': 'Ok'
  }
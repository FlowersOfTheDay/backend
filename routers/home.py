from fastapi import APIRouter, Response
from fastapi.responses import HTMLResponse

router = APIRouter(
  tags=['home']
)

@router.get('/')
async def get_root():
  return {
    'name': 'Flowers of the day Backend'
  }

@router.get('/favicon.ico', response_class=HTMLResponse)
async def get_icon():
  return Response(content="", media_type="image/x-icon")
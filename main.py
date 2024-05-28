import os
import dotenv
from utils.prisma import prisma
from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager

import routers

# loading fron .env file
dotenv.load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
  if os.environ.get('DATABASE_URL') is None and os.environ.get('DATABASE_USERNAME') is not None:
    os.environ['DATABASE_URL'] = f"postgresql://{os.environ.get('DATABASE_USERNAME')}:{os.environ.get('DATABASE_PASSWORD')}@{os.environ.get('DATABASE_HOST')}:{os.environ.get('DATABASE_PORT')}/{os.environ.get('DATABASE_DBNAME')}"
  await prisma.connect()
  yield
  await prisma.disconnect()
  

app = FastAPI(lifespan=lifespan,root_path=os.environ.get('BASE_URL', ''))

# connecting router
app.include_router(routers.home.router)
app.include_router(routers.health.router)
app.include_router(routers.chat.router)
app.include_router(routers.recommend.router)
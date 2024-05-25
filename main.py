import os
import dotenv
from fastapi import FastAPI
from contextlib import asynccontextmanager
from utils.prisma import prisma

import routers

# loading fron .env file
dotenv.load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await prisma.connect()
    yield
    await prisma.disconnect()

app = FastAPI(lifespan=lifespan, root_path=os.environ.get('BASE_URL', ''))

# connecting router
app.include_router(routers.home.router)
app.include_router(routers.health.router)
app.include_router(routers.chat.router)
app.include_router(routers.recommend.router)
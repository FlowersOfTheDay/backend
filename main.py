import dotenv
from fastapi import FastAPI
from contextlib import asynccontextmanager
from prisma import Prisma

import routers

# loading fron .env file
dotenv.load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await Prisma.connect()
    yield
    await Prisma.disconnect()

app = FastAPI(lifespan=lifespan)

# connecting router
app.include_router(routers.home.router)
app.include_router(routers.health.router)
app.include_router(routers.chat.router)
app.include_router(routers.recommend.router)
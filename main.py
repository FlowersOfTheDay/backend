import os
import dotenv
from fastapi import FastAPI

import routers

# loading fron .env file
dotenv.load_dotenv()


app = FastAPI(root_path=os.environ.get('BASE_URL', ''))

# connecting router
app.include_router(routers.home.router)
app.include_router(routers.health.router)
app.include_router(routers.chat.router)
app.include_router(routers.recommend.router)
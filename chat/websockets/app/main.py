from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import users
from contextlib import asynccontextmanager
from app.databases.database import init_db,cleanup_db
from app.models.user import User
import asyncio
from app.log_config import setup_logging
import logging

# 在应用启动前配置日志
setup_logging()
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app:FastAPI):
    logger.info("🚀 Starting application initialization")
    try:
        await init_db()
        logger.info("✅ Database initialized successfully")
    except Exception as e:
        logger.critical(f"❌ Database initialization failed: {str(e)}")
        raise
    yield
    logger.info("🛑 Cleaning up resources...")
    await cleanup_db()
    logger.info("✅ Cleanup complete")
    
app = FastAPI(title="Chat API",version="0.0.1",lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    # uvicorn main:app --host 0.0.0.0 --port 8000 --reload  热重载
    # python main.py
    # fastapi dev main.py
    # 更简洁的 API 文档展示： http://localhost:8000/redoc 
    # 可视化API端点，支持直接测试接口：http://localhost:8000/docs


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from configs.env_logconfig import setup_logging
import logging
from databases.mysql_database import init_db as init_db_mysql
from databases.mysql_database import cleanup_db as cleanup_db_mysql
from users.routers import auth,users

# 初始化日志（通常在应用启动时最早调用）
setup_logging() # type: ignore
logger = logging.getLogger(__name__)
logger.info("Application started")

@asynccontextmanager
async def lifespan(app:FastAPI):
    logger.info("🚀 Starting application initialization")
    try:
        await init_db_mysql()
        logger.info("✅ Database initialized successfully")
    except Exception as e:
        logger.critical(f"❌ Database initialization failed: {str(e)}")
        raise
    yield
    logger.info("🛑 Cleaning up resources...")
    await cleanup_db_mysql()
    logger.info("✅ Cleanup complete")
        
# 生产模式下，debug=Fasle,openai_url=None
app=FastAPI(title="LMXY API",version="0.0.2",lifespan=lifespan,debug=True,)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],    
)

app.include_router(users.router)



def create_app():
    return app
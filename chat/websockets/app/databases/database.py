from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession,async_sessionmaker
from sqlmodel import SQLModel
import logging

logger = logging.getLogger(__name__)


DATABASE_URL = "mysql+aiomysql://root:123456@localhost/chat_db"
async_engine = create_async_engine(DATABASE_URL)
AsyncSessionLocal = async_sessionmaker(bind=async_engine,class_=AsyncSession,expire_on_commit=False)


async def test_connection():
    try:
        async with async_engine.connect() as conn:
            result = await conn.execute(text("SELECT 1"))
            logger.info(f"Database connection test successful: {result.scalar()}")
            return True
    except Exception as e:
        logger.error(f"Database connection failed: {str(e)}")
        return False



async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
        
        
# async def init_db():
#     async with async_engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)


async def init_db():
    logger.info("Starting database initialization")
    
    if not await test_connection():
        logger.critical("Database connection test failed")
        raise RuntimeError("Database connection failed")
    
    try:
        async with async_engine.begin() as conn:
            logger.info("Creating database tables...")
            await conn.run_sync(SQLModel.metadata.create_all)
            logger.info("Tables created successfully")
    except Exception as e:
        logger.error(f"Table creation failed: {str(e)}")
        raise
    
    logger.info("Database initialization complete")


# 同步库的
# def create_db_and_tables():
#     SQLModel.metadata.create_all(engine)


async def cleanup_db():
    await async_engine.dispose()
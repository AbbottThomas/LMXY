from configs.settings_config import settings
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession,async_sessionmaker
from sqlmodel import SQLModel
import logging

logger = logging.getLogger(__name__)


engine = create_async_engine(settings.MYSQL_URI, echo=True)

async def cleanup_db():
    await engine.dispose()

AsyncSessionLocal= async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
    )


async def get_db():
    """
    获取异步数据库会话依赖项
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception as e:
            await session.rollback()
            raise e
        finally:
            await session.close()

async def init_db():
    """
    初始化数据库连接，创建表格
    """
    logger.info("Starting mysql database initialization")
    try:
        async with engine.begin() as conn:
            logger.info("Creating mysql database tables...")
            await conn.run_sync(SQLModel.metadata.create_all)
            logger.info("Tables created successfully")
    except Exception as e:
        logger.error(f"Table creation failed: {str(e)}")
        raise e
    
    logger.info("Database initialization complete")





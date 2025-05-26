from sqlmodel import create_engine, SQLModel, Session

# 数据库配置


DATABASE_URL = "mysql+pymysql://root:123456@localhost:3306/blog_db"


engine = create_engine(DATABASE_URL)

def get_db():
    with Session(engine) as session:
        yield session

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    
    
# 清理数据库资源
def cleanup_db():
    # 关闭所有连接
    engine.dispose()
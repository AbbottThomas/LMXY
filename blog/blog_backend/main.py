from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager

from app.database import create_db_and_tables,cleanup_db
from app.routers import (
    auth,
    users,
    articles,
    comments,
    categories
)
from app.exceptions import (        # 新增
    # handle_unique_constraint_error,
    PermissionDeniedException
)


# FastAPI入口文件

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield
    cleanup_db()

app = FastAPI(title="Blog API", version="1.0.0",
                  description="""
用户注册登录：
- 注册新用户
- 用户登录

文章写入读取：
- 发布新文章
- 查看文章列表
- 查看单篇文章
    """,
              summary="博客功能",lifespan=lifespan)

# CORS配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 在app创建后添加异常处理
app.add_exception_handler(PermissionDeniedException, 
    lambda request, exc: JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )
)

# 全局异常处理
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )




# 包含路由
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(articles.router)
app.include_router(comments.router)
app.include_router(categories.router)

# @app.on_event("startup")
# def on_startup():
#     create_db_and_tables()



@app.get("/try")
async def read_root():
    return {"message": "Hello World!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
    # uvicorn main:app --host 0.0.0.0 --port 8000 --reload  热重载
    # python main.py
    # fastapi dev main.py
    # 更简洁的 API 文档展示： http://localhost:8000/redoc 
    # 可视化API端点，支持直接测试接口：http://localhost:8000/docs

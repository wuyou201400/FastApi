from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .core.config import settings
from .api.v1.api import api_router
from .core.database import create_tables, SessionLocal
from .core.security import get_password_hash
from .models.user import User
from .models.item import Item

# 创建FastAPI应用实例
# title: 项目名称
# version: API版本
# openapi_url: OpenAPI文档的URL路径
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# 配置CORS（跨源资源共享）中间件
# allow_origins=["*"]: 允许所有来源的请求
# allow_credentials=True: 允许携带认证信息
# allow_methods=["*"]: 允许所有HTTP方法
# allow_headers=["*"]: 允许所有HTTP头部
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册API路由，添加API版本前缀
app.include_router(api_router, prefix=settings.API_V1_STR)

# 创建测试数据的函数
def create_test_data():
    try:
        # 创建数据库会话
        db = SessionLocal()
        try:
            # 检查测试用户是否已存在
            if not db.query(User).filter(User.email == "test@example.com").first():
                try:
                    # 创建测试用户对象
                    # 设置邮箱、用户名、密码哈希、账户状态和超级用户权限
                    test_user = User(
                        email="test@example.com",
                        username="testuser",
                        hashed_password=get_password_hash("password123"),
                        is_active=True,
                        is_superuser=True
                    )
                    # 添加用户到数据库并提交
                    db.add(test_user)
                    db.commit()
                    # 刷新用户对象以获取数据库生成的ID
                    db.refresh(test_user)

                    # 创建测试商品列表
                    # 每个商品包含名称、价格、描述和所有者ID
                    test_items = [
                        Item(
                            name="测试商品1",
                            price=99.9,
                            description="这是测试商品1的描述",
                            owner_id=test_user.id
                        ),
                        Item(
                            name="测试商品2",
                            price=199.9,
                            description="这是测试商品2的描述",
                            owner_id=test_user.id
                        )
                    ]
                    # 批量添加商品并提交
                    db.add_all(test_items)
                    db.commit()
                except Exception as e:
                    # 发生错误时回滚事务
                    db.rollback()
                    print(f"创建测试数据时发生错误: {str(e)}")
        finally:
            # 确保数据库会话被关闭
            db.close()
    except Exception as e:
        # 捕获数据库连接错误
        print(f"数据库连接错误: {str(e)}")

# 应用启动时的初始化操作
# 1. 创建数据库表
# 2. 创建测试数据
create_tables()
create_test_data()

# 仅在直接运行此文件时执行
if __name__ == "__main__":
    import uvicorn
    # 启动开发服务器
    # host: 监听地址
    # port: 监听端口
    # reload: 开启热重载
    uvicorn.run("app.main:app", host="127.0.0.1", port=8005, reload=True) 
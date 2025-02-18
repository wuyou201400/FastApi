from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# 从配置文件获取数据库连接URL
SQLALCHEMY_DATABASE_URL = settings.SQLALCHEMY_DATABASE_URI

# 创建数据库引擎实例
# create_engine 是 SQLAlchemy 的引擎工厂函数
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True,  # 设置为True可以显示所有SQL语句，用于调试
    connect_args={"check_same_thread": False}
)

# 创建数据库会话类
# sessionmaker 创建一个自定义的 Session 类
SessionLocal = sessionmaker(
    autocommit=False,  # 禁用自动提交
    autoflush=False,   # 禁用自动刷新
    bind=engine        # 绑定到我们的数据库引擎
)

# 创建一个声明性基类
# 这个基类将被我们所有的模型类继承
# 它维护了一个从类到表的注册表
Base = declarative_base()

# 创建所有表
def create_tables():
    Base.metadata.create_all(bind=engine)

# 数据库依赖项
def get_db():
    """
    创建数据库会话的依赖函数
    
    Yields:
        Session: 数据库会话对象
    
    使用方法:
    @app.get("/items/")
    def read_items(db: Session = Depends(get_db)):
        ...
    """
    # 创建一个新的数据库会话
    db = SessionLocal()
    try:
        # 返回数据库会话
        yield db
    finally:
        # 确保会话最后被关闭
        # 即使发生异常也会执行
        db.close() 
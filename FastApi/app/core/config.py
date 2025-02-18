from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    """应用配置类
    
    使用 pydantic 的 BaseSettings 管理所有配置项
    支持从环境变量和 .env 文件读取配置
    """
    # 基本配置
    PROJECT_NAME: str = "FastAPI高级示例"  # 项目名称
    VERSION: str = "2.0.0"  # 项目版本
    API_V1_STR: str = "/api/v1"  # API版本前缀
    
    # 数据库配置
    POSTGRES_SERVER: str = "localhost"  # 数据库服务器地址
    POSTGRES_USER: str = "postgres"  # 数据库用户名
    POSTGRES_PASSWORD: str = "postgres"  # 数据库密码
    POSTGRES_DB: str = "fastapi_db"  # 数据库名称
    SQLALCHEMY_DATABASE_URI: Optional[str] = None  # 数据库连接URI
    
    # JWT配置
    JWT_SECRET: str = "your-secret-key"  # JWT密钥
    ALGORITHM: str = "HS256"  # JWT加密算法
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  # Token过期时间（分钟）
    
    class Config:
        env_file = ".env"  # 指定环境变量文件

settings = Settings()  # 创建配置实例
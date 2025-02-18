from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from ..core.database import Base

class User(Base):
    """
    用户模型类
    定义用户在数据库中的结构
    """
    __tablename__ = "users"  # 指定数据库表名

    # 用户ID，主键
    id = Column(Integer, primary_key=True, index=True)
    # 用户邮箱，唯一索引
    email = Column(String, unique=True, index=True)
    # 用户名，唯一索引
    username = Column(String, unique=True, index=True)
    # 密码哈希值
    hashed_password = Column(String)
    # 用户状态
    is_active = Column(Boolean, default=True)
    # 超级用户标志
    is_superuser = Column(Boolean, default=False)
    
    # 关联关系：一个用户可以有多个商品
    # back_populates 建立双向关系
    items = relationship("Item", back_populates="owner") 
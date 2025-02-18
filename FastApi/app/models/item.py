from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..core.database import Base

class Item(Base):
    """
    商品模型类
    定义商品在数据库中的结构
    """
    __tablename__ = "items"  # 指定数据库表名

    # 商品ID，主键
    id = Column(Integer, primary_key=True, index=True)
    # 商品名称，创建索引以提高查询性能
    name = Column(String, index=True)
    # 商品价格
    price = Column(Float)
    # 商品描述，允许为空
    description = Column(String, nullable=True)
    # 外键：关联到用户表的ID
    owner_id = Column(Integer, ForeignKey("users.id"))
    
    # 建立与User模型的关系
    # back_populates 确保双向关系
    owner = relationship("User", back_populates="items") 
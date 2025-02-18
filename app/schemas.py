from typing import Optional
# 处理请求体、查询参数、路径参数等的数据验证和序列化
from pydantic import BaseModel

# 定义继承自 BaseModel 的类来创建数据模型
class ItemBase(BaseModel):
    """商品基础模型
    
    包含商品的基本属性定义
    """
    name: str  # 商品名称
    price: float  # 商品价格
    description: Optional[str] = None  # 可选的商品描述

class ItemCreate(ItemBase):
    """商品创建模型
    
    继承自ItemBase，用于创建新商品
    """
    pass

class ItemResponse(ItemBase):
    """商品响应模型
    
    继承自ItemBase，添加了id字段，用于返回完整的商品信息
    """
    id: int  # 商品ID
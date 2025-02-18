from typing import Optional
from pydantic import BaseModel, Field

class ItemBase(BaseModel):
    """商品基础模型"""
    name: str = Field(..., min_length=1, max_length=50, description="商品名称", error_msg="Name must be between 1 and 50 characters")
    price: float = Field(..., gt=0, description="商品价格")
    description: Optional[str] = Field(None, max_length=200, description="商品描述")

class ItemCreate(ItemBase):
    """创建商品时的请求模型"""
    pass

class ItemUpdate(BaseModel):
    """更新商品时的请求模型"""
    name: Optional[str] = Field(None, min_length=1, max_length=50)
    price: Optional[float] = Field(None, gt=0)
    description: Optional[str] = Field(None, max_length=200)

class ItemResponse(ItemBase):
    """商品响应模型"""
    id: int
    owner_id: int

    class Config:
        orm_mode = True 
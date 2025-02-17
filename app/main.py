# 导入必要的模块
from fastapi import FastAPI, HTTPException  # 导入FastAPI核心组件
from typing import List  # 导入类型提示支持
from .schemas import ItemCreate, ItemResponse  # 导入数据模型
from .models import items_db  # 导入模拟数据库

# 创建FastAPI应用实例
app = FastAPI(
    title="FastAPI示例",  # API文档标题
    description="一个简单的FastAPI应用示例",  # API文档描述
    version="1.0.0"  # API版本号
)

# 根路由处理器
@app.get("/")
async def root():
    """返回欢迎信息的根端点"""
    return {"message": "欢迎使用FastAPI示例应用"}

# 获取所有商品的路由
@app.get("/items/", response_model=List[ItemResponse])
async def get_items():
    """获取所有商品列表
    
    Returns:
        List[ItemResponse]: 商品列表
    """
    return items_db

# 获取单个商品的路由
@app.get("/items/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int):
    """根据ID获取特定商品
    
    Args:
        item_id (int): 商品ID
        
    Raises:
        HTTPException: 当商品未找到时抛出404错误
        
    Returns:
        ItemResponse: 商品信息
    """
    if item_id >= len(items_db):
        raise HTTPException(status_code=404, detail="商品未找到")
    return items_db[item_id]

# 创建新商品的路由
@app.post("/items/", response_model=ItemResponse)
async def create_item(item: ItemCreate):
    """创建新商品
    
    Args:
        item (ItemCreate): 商品创建模型
        
    Returns:
        ItemResponse: 创建的商品信息
    """
    new_item = {
        "id": len(items_db),  # 使用当前列表长度作为新ID
        "name": item.name,
        "price": item.price,
        "description": item.description
    }
    items_db.append(new_item)
    return new_item 
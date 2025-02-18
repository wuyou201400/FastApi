# 从 fastapi 库中导入 APIRouter 类，用于创建路由器实例
from fastapi import APIRouter
# 从本地 endpoints 目录导入各个功能模块的路由
from .endpoints import items, users, auth

# 创建主路由器实例，用于统一管理所有子路由
api_router = APIRouter()

# 注册物品相关的路由
# prefix: 设置 URL 前缀为 "/items"
# tags: 为该组路由添加标签，用于 API 文档分类
api_router.include_router(items.router, prefix="/items", tags=["items"])

# 注册用户相关的路由
# prefix: 设置 URL 前缀为 "/users"
# tags: 为该组路由添加标签，用于 API 文档分类
api_router.include_router(users.router, prefix="/users", tags=["users"]) 

# 注册认证相关的路由
# prefix: 设置 URL 前缀为 "/auth"
# tags: 为该组路由添加标签，用于 API 文档分类
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
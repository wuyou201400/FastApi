from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ....core.database import get_db
from ....core.security import get_current_user
from ....schemas.user import UserCreate, UserResponse
from ....models.user import User

# 创建路由器实例
router = APIRouter()

@router.post("/users/", response_model=UserResponse)
def create_user(
    user: UserCreate,  # 请求体，包含用户创建信息
    db: Session = Depends(get_db)  # 数据库会话依赖
):
    """
    创建新用户
    
    Args:
        user: 用户创建模型实例
        db: 数据库会话
        
    Returns:
        UserResponse: 创建的用户信息
        
    Raises:
        HTTPException: 当邮箱已被注册时抛出400错误
    """
    # 检查邮箱是否已存在
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="邮箱已被注册")
    return create_new_user(db=db, user=user)

@router.get("/users/me", response_model=UserResponse)
def read_users_me(
    current_user: User = Depends(get_current_user)  # 当前登录用户依赖
):
    """
    获取当前登录用户信息
    
    Args:
        current_user: 当前认证用户实例
        
    Returns:
        UserResponse: 用户信息
    """
    return current_user 
from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from ....core.security import create_access_token, verify_password
from ....core.config import settings
from sqlalchemy.orm import Session
from ....core.database import get_db
from ....models.user import User

router = APIRouter()

@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    # 断点
    # n (next): 执行下一行
    # s (step): 步入函数
    # c (continue): 继续执行
    # p variable: 打印变量值
    # l (list): 显示当前位置附近的代码
    import pdb; pdb.set_trace()
    # 使用 print 调试
    print(f"DEBUG: form_data={form_data.__dict__}")
    # 查找用户
    user = db.query(User).filter(User.username == form_data.username).first()
    print(f"DEBUG: user={user}")
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # 验证密码
    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误!",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # 创建访问令牌
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"email_in_token": user.email}, expires_delta=access_token_expires
    )
    
    # 返回token
    return {
        "access_token": access_token,
        "token_type": "bearer"
    } 
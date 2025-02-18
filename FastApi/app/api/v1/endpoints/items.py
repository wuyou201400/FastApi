from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from ....core.database import get_db
from ....models.item import Item
from ....schemas.item import ItemCreate, ItemUpdate, ItemResponse
from ....core.security import get_current_user
from ....models.user import User

router = APIRouter()

@router.get("/", response_model=List[ItemResponse])
async def list_items(
    skip: int = Query(0, description="跳过记录数"),
    limit: int = Query(10, description="返回记录数"),
    name: Optional[str] = Query(None, description="商品名称搜索"),
    db: Session = Depends(get_db)
):
    """
    获取商品列表，支持分页和搜索
    """
    query = db.query(Item)
    if name:
        query = query.filter(Item.name.ilike(f"%{name}%"))
    return query.offset(skip).limit(limit).all()

@router.post("/", response_model=ItemResponse)
async def create_item(
    item: ItemCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    创建新商品
    """
    import pdb; pdb.set_trace()
    db_item = Item(
        name=item.name,
        price=item.price,
        description=item.description,
        owner_id=current_user["id"]
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/{item_id}", response_model=ItemResponse)
async def get_item(
    item_id: int,
    db: Session = Depends(get_db)
):
    """
    根据ID获取商品详情
    """
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="商品不存在")
    return item

@router.put("/{item_id}", response_model=ItemResponse)
async def update_item(
    item_id: int,
    item_update: ItemUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    更新商品信息
    """
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="商品不存在")
    if db_item.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="没有权限修改此商品")
    
    for field, value in item_update.dict(exclude_unset=True).items():
        setattr(db_item, field, value)
    
    db.commit()
    db.refresh(db_item)
    return db_item

@router.delete("/{item_id}")
async def delete_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    删除商品
    """
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="商品不存在")
    if db_item.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="没有权限删除此商品")
    
    db.delete(db_item)
    db.commit()
    return {"message": "商品已删除"} 
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api import deps
from app.models.item import Item

router = APIRouter()


@router.get("/")
def read_item(
        db: Session = Depends(deps.get_db)
):
    item1 = Item(name="klocek")
    db.add(item1)
    db.commit()
    db.refresh(item1)
    return item1

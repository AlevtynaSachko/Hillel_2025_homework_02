from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from .models import Item

def create_item(db: Session, name: str, description: str | None = None) -> Item:
    item = Item(name=name, description=description)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def get_items(db: Session) -> list[Item]:
    return list(db.scalars(select(Item)).all())

def get_item_by_name(db: Session, name: str) -> Item | None:
    return db.scalar(select(Item).where(Item.name == name))

def update_item_description(db: Session, name: str, new_desc: str) -> int:
    res = db.execute(
        update(Item).where(Item.name == name).values(description=new_desc).returning(Item.id)
    )
    db.commit()
    return len(res.fetchall())

def delete_item(db: Session, name: str) -> int:
    res = db.execute(
        delete(Item).where(Item.name == name).returning(Item.id)
    )
    db.commit()
    return len(res.fetchall())

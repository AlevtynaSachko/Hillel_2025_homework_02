from src.crud import (
    create_item, get_items, get_item_by_name,
    update_item_description, delete_item
)

class TestCRUD:
    def test_insert_and_select(self, db):
        create_item(db, name="rose", description="flower")
        create_item(db, name="ylang", description="favorite oil")
        items = get_items(db)
        assert {i.name for i in items} >= {"rose", "ylang"}

    def test_update(self, db):
        create_item(db, name="neroli", description="citrus")
        changed = update_item_description(db, "neroli", "orange blossom")
        assert changed == 1
        item = get_item_by_name(db, "neroli")
        assert item and item.description == "orange blossom"

    def test_delete(self, db):
        create_item(db, name="iris", description="powdery")
        deleted = delete_item(db, "iris")
        assert deleted == 1
        assert get_item_by_name(db, "iris") is None

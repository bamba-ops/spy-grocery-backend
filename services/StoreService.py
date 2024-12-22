from typing import List
from DAO.StoreDAO import StoreDAO
from models.store import Store

class StoreService:

    @staticmethod
    def create_store(store: Store) -> Store:
        """
        Logic to create a new store.
        :param store: Store model instance
        :return: Created store instance
        """
        store_data = store.dict(exclude={"id", "created_at"})
        new_store = StoreDAO.create(store_data)
        return Store(**new_store)

    @staticmethod
    def get_store_by_id(store_id: str) -> Store:
        """
        Retrieve a store by its ID.
        :param store_id: The ID of the store
        :return: Store instance
        """
        store = StoreDAO.read(store_id)
        if not store:
            raise ValueError(f"Store with ID {store_id} not found.")
        return Store(**store)

    @staticmethod
    def get_all_stores() -> List[Store]:
        """
        Retrieve all stores.
        :return: List of Store instances
        """
        stores = StoreDAO.read_all()
        return [Store(**store) for store in stores]

    @staticmethod
    def update_store(store_id: str, store: Store) -> Store:
        """
        Update an existing store.
        :param store_id: The ID of the store to update
        :param store: Updated store data
        :return: Updated store instance
        """
        updates = store.dict(exclude={"id", "created_at"})
        updated_store = StoreDAO.update(store_id, updates)
        return Store(**updated_store)

    @staticmethod
    def delete_store(store_id: str) -> Store:
        """
        Delete a store by its ID.
        :param store_id: The ID of the store to delete
        :return: Deleted store instance
        """
        deleted_store = StoreDAO.delete(store_id)
        return Store(**deleted_store)

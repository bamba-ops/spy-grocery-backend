from typing import List
from DAO.PriceDAO import PriceDAO
from models.price import Price

class PriceService:

    @staticmethod
    def create_price(price: Price) -> Price:
        """
        Logic to create a new price.
        :param price: Price model instance
        :return: Created price instance
        """
        price_data = price.dict(exclude={"id", "created_at"})
        new_price = PriceDAO.create(price_data)
        return Price(**new_price)

    @staticmethod
    def get_price_by_id(price_id: str) -> Price:
        """
        Retrieve a price by its ID.
        :param price_id: The ID of the price
        :return: Price instance
        """
        price = PriceDAO.read(price_id)
        if not price:
            raise ValueError(f"Price with ID {price_id} not found.")
        return Price(**price)

    @staticmethod
    def get_all_prices() -> List[Price]:
        """
        Retrieve all prices.
        :return: List of Price instances
        """
        prices = PriceDAO.read_all()
        return [Price(**price) for price in prices]

    @staticmethod
    def update_price(price_id: str, price: Price) -> Price:
        """
        Update an existing price.
        :param price_id: The ID of the price to update
        :param price: Updated price data
        :return: Updated price instance
        """
        updates = price.dict(exclude={"id", "created_at", "product_id", "store_id"})
        updated_price = PriceDAO.update(price_id, updates)
        return Price(**updated_price)

    @staticmethod
    def delete_price(price_id: str) -> Price:
        """
        Delete a price by its ID.
        :param price_id: The ID of the price to delete
        :return: Deleted price instance
        """
        deleted_price = PriceDAO.delete(price_id)
        return Price(**deleted_price)

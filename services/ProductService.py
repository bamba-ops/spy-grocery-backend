from typing import List
from DAO.ProductDAO import ProductDAO
from models.product import Product

class ProductService:

    @staticmethod
    def create_product(product: Product) -> Product:
        """
        Logic to create a new product.
        :param product: Product model instance
        :return: Created product instance
        """
        product_data = product.dict(exclude={"id", "created_at"})
        new_product = ProductDAO.create(product_data)
        return Product(**new_product)

    @staticmethod
    def get_product_by_id(product_id: str) -> Product:
        """
        Retrieve a product by its ID.
        :param product_id: The ID of the product
        :return: Product instance
        """
        product = ProductDAO.read(product_id)
        if not product:
            raise ValueError(f"Product with ID {product_id} not found.")
        return Product(**product)

    @staticmethod
    def get_product_by_name(product_name: str) -> Product:
        """
        Retrieve a product by its name.
        :param product_name: The name of the product
        :return: Product instance
        """
        product = ProductDAO.read_by_name(product_name)
        if not product:
            raise ValueError(f"Product with name {product_name} not found.")
        return Product(**product)


    @staticmethod
    def get_all_products() -> List[Product]:
        """
        Retrieve all products.
        :return: List of Product instances
        """
        products = ProductDAO.read_all()
        return [Product(**product) for product in products]

    @staticmethod
    def update_product(product_id: str, product: Product) -> Product:
        """
        Update an existing product.
        :param product_id: The ID of the product to update
        :param product: Updated product data
        :return: Updated product instance
        """
        updates = product.dict(exclude={"id", "created_at"})
        updated_product = ProductDAO.update(product_id, updates)
        return Product(**updated_product)

    @staticmethod
    def delete_product(product_id: str) -> Product:
        """
        Delete a product by its ID.
        :param product_id: The ID of the product to delete
        :return: Deleted product instance
        """
        deleted_product = ProductDAO.delete(product_id)
        return Product(**deleted_product)

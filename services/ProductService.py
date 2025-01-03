from typing import List
from DAO.ProductDAO import ProductDAO
from DAO.PriceDAO import PriceDAO
from models.product import Product
import requests
from difflib import SequenceMatcher


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

    @staticmethod
    def get_best_price_of_product(product: Product) -> Product:
        product_dict = product.dict()
        price_dict = PriceDAO.read_by_product_id(product_dict["id"])
        price_dict["product"] = product_dict
        # Step 1: Creating the json data
        data = {"product_name": product.name, "store_name": "iga"}

        # Step 2: Run the scrape
        SCRAPER_URL_API = "http://127.0.0.1:8001/api/v1/scrape/product/all"

        try:
            response = requests.post(SCRAPER_URL_API, json=data)

            # Step 3: Getting response
            if response.status_code == 200:
                data = response.json()
            else:
                print(f"Erreur {response.status_code} : {response.text}")

        except Exception as e:
            print("Une erreur est survenue :", str(e))
        finally:
            # Step 4: Filtering the data received
            if data["status"] != "success":
                return data
            else:
                # print(data["data"])
                # print("=====================================")
                target_name = product_dict.get("name", "")
                target_brand = product_dict.get("brand", "")
                target_unit = product_dict.get("unit", "")

                scored_products = []

                for product_from_data in [price["product"] for price in data["data"]]:
                    product_name = product_from_data.get("name", "")
                    product_brand = product_from_data.get("brand", "")
                    product_unit = product_from_data.get("unit", "")

                    # Calculate similarity for each criterion
                    name_similarity = ProductService.calculate_similarity(
                        target_name, product_name
                    )
                    brand_similarity = ProductService.calculate_similarity(
                        target_brand, product_brand
                    )
                    unit_similarity = ProductService.calculate_similarity(
                        target_unit, product_unit
                    )

                    # Combine the scores (you can adjust the weights if needed)
                    combined_score = (
                        0.5 * name_similarity
                        + 0.3 * brand_similarity
                        + 0.2 * unit_similarity
                    )
                    scored_products.append(
                        {
                            "product": product_from_data,
                            "name_similarity": name_similarity,
                            "brand_similarity": brand_similarity,
                            "unit_similarity": unit_similarity,
                            "combined_score": combined_score,
                        }
                    )

                # Sort products by the combined score in descending order
                scored_products.sort(key=lambda x: x["combined_score"], reverse=True)

                # Return the best match and all scores
                best_match = scored_products[:5] if scored_products else None

                # print(product_dict)
                # print(best_match)
                for price, _product in zip(data["data"], best_match):
                    price["product"] = _product["product"]
                # print("=====================================")
                print(data["data"])
                # print(scored_products)

            # Step 4: Return information about the best price
            return {"target_product": price_dict, "best_match": data["data"]}

    @staticmethod
    def calculate_similarity(a, b):
        """Calculate the similarity score between two strings."""
        if not a or not b:
            return 0  # If either string is missing, similarity is 0
        return SequenceMatcher(None, a, b).ratio()

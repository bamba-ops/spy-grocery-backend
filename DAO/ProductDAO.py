from db.supabase_connexion import SupabaseConnection

class ProductDAO:
    _supabase = SupabaseConnection.create_connection()

    @staticmethod
    def initialize(supabase_client):
        """
        Initialise la connexion Supabase pour la classe.
        :param supabase_client: Client de connexion Supabase
        """
        ProductDAO._supabase = supabase_client

    @staticmethod
    def create(product_data):
        """
        Crée un nouveau produit.
        :param product_data: Dictionnaire contenant les informations du produit
        :return: Le produit créé
        """
        try:
            response = ProductDAO._supabase.table("products").insert(product_data).execute()
            if response.data:
                return response.data[0]
            else:
                raise ValueError(f"Erreur lors de la création : {response.errors}")
        except Exception as e:
            raise RuntimeError(f"Erreur lors de la création du produit : {e}")

    @staticmethod
    def read(product_id):
        """
        Lit un produit par son ID.
        :param product_id: ID du produit
        :return: Le produit correspondant
        """
        try:
            response = ProductDAO._supabase.table("products").select("*").eq("id", product_id).execute()
            if response.data:
                return response.data[0]
            else:
                raise ValueError(f"Produit avec ID {product_id} non trouvé.")
        except Exception as e:
            raise RuntimeError(f"Erreur lors de la lecture du produit : {e}")

    @staticmethod    
    def read_by_name(product_name):
        """
        Lit un produit par son nom.
        :param product_name: Nom du produit
        :return: Le produit correspondant
        """
        try:
            response = ProductDAO._supabase.table("products").select("*").eq("name", product_name).execute()
            if response.data:
                return response.data[0]
            else:
                raise ValueError(f"Produit avec le nom {product_name} non trouvé.")
        except Exception as e:
            raise RuntimeError(f"Erreur lors de la lecture du produit par nom : {e}") 

    @staticmethod
    def read_all():
        """
        Récupère tous les produits.
        :return: Liste des produits
        """
        try:
            response = ProductDAO._supabase.table("products").select("*").execute()
            return response.data
        except Exception as e:
            raise RuntimeError(f"Erreur lors de la récupération des produits : {e}")

    @staticmethod
    def update(product_id, updates):
        """
        Met à jour un produit existant.
        :param product_id: ID du produit à mettre à jour
        :param updates: Dictionnaire contenant les mises à jour
        :return: Le produit mis à jour
        """
        try:
            response = ProductDAO._supabase.table("products").update(updates).eq("id", product_id).execute()
            if response.data:
                return response.data[0]
            else:
                raise ValueError(f"Erreur lors de la mise à jour : {response.errors}")
        except Exception as e:
            raise RuntimeError(f"Erreur lors de la mise à jour du produit : {e}")

    @staticmethod
    def delete(product_id):
        """
        Supprime un produit par son ID.
        :param product_id: ID du produit à supprimer
        :return: Confirmation de la suppression
        """
        try:
            response = ProductDAO._supabase.table("products").delete().eq("id", product_id).execute()
            if response.data:
                return response.data[0]
            else:
                raise ValueError(f"Erreur lors de la suppression : {response.errors}")
        except Exception as e:
            raise RuntimeError(f"Erreur lors de la suppression du produit : {e}")

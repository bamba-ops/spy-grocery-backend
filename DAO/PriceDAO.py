from db.supabase_connexion import SupabaseConnection


class PriceDAO:
    _supabase = SupabaseConnection.create_connection()

    @staticmethod
    def initialize(supabase_client):
        """
        Initialise la connexion Supabase pour la classe.
        :param supabase_client: Client de connexion Supabase
        """
        PriceDAO._supabase = supabase_client

    @staticmethod
    def create(price_data):
        """
        Crée un nouveau prix.
        :param price_data: Dictionnaire contenant les informations du prix
        :return: Le prix créé
        """
        try:
            response = PriceDAO._supabase.table("prices").insert(price_data).execute()
            if response.data:
                return response.data[0]
            else:
                raise ValueError(f"Erreur lors de la création : {response.errors}")
        except Exception as e:
            raise RuntimeError(f"Erreur lors de la création du prix : {e}")

    @staticmethod
    def read(price_id):
        """
        Lit un prix par son ID.
        :param price_id: ID du prix
        :return: Le prix correspondant
        """
        try:
            response = PriceDAO._supabase.table("prices").select("*").eq("id", price_id).execute()
            if response.data:
                return response.data[0]
            else:
                raise ValueError(f"Prix avec ID {price_id} non trouvé.")
        except Exception as e:
            raise RuntimeError(f"Erreur lors de la lecture du prix : {e}")

    @staticmethod
    def read_all():
        """
        Récupère tous les prix.
        :return: Liste des prix
        """
        try:
            response = PriceDAO._supabase.table("prices").select("*").execute()
            return response.data
        except Exception as e:
            raise RuntimeError(f"Erreur lors de la récupération des prix : {e}")

    @staticmethod
    def read_by_product_and_store(product_id, store_id):
        """
        Lit un prix par ID de produit et ID de magasin.
        :param product_id: ID du produit
        :param store_id: ID du magasin
        :return: Le prix correspondant
        """
        try:
            response = PriceDAO._supabase.table("prices").select("*").eq("product_id", product_id).eq("store_id", store_id).execute()
            if response.data:
                return response.data[0]
            else:
                raise ValueError(f"Prix pour le produit {product_id} dans le magasin {store_id} non trouvé.")
        except Exception as e:
            raise RuntimeError(f"Erreur lors de la lecture du prix : {e}")

    @staticmethod
    def update(price_id, updates):
        """
        Met à jour un prix existant.
        :param price_id: ID du prix à mettre à jour
        :param updates: Dictionnaire contenant les mises à jour
        :return: Le prix mis à jour
        """
        try:
            response = PriceDAO._supabase.table("prices").update(updates).eq("id", price_id).execute()
            if response.data:
                return response.data[0]
            else:
                raise ValueError(f"Erreur lors de la mise à jour : {response.errors}")
        except Exception as e:
            raise RuntimeError(f"Erreur lors de la mise à jour du prix : {e}")

    @staticmethod
    def delete(price_id):
        """
        Supprime un prix par son ID.
        :param price_id: ID du prix à supprimer
        :return: Confirmation de la suppression
        """
        try:
            response = PriceDAO._supabase.table("prices").delete().eq("id", price_id).execute()
            if response.data:
                return response.data[0]
            else:
                raise ValueError(f"Erreur lors de la suppression : {response.errors}")
        except Exception as e:
            raise RuntimeError(f"Erreur lors de la suppression du prix : {e}")

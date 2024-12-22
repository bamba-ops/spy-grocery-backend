from db.supabase_connexion import SupabaseConnection

class StoreDAO:
    _supabase = SupabaseConnection.create_connection()
    
    @staticmethod
    def initialize(supabase_client):
        """
        Initialise la connexion Supabase pour la classe.
        :param supabase_client: Client de connexion Supabase
        """
        StoreDAO._supabase = supabase_client

    @staticmethod
    def create(store_data):
        """
        Crée un nouveau magasin.
        :param store_data: Dictionnaire contenant les informations du magasin
        :return: Le magasin créé
        """
        try:
            response = StoreDAO._supabase.table("stores").insert(store_data).execute()
            if response.data:
                return response.data[0]
            else:
                raise ValueError(f"Erreur lors de la création : {response.errors}")
        except Exception as e:
            raise RuntimeError(f"Erreur lors de la création du magasin : {e}")

    @staticmethod
    def read(store_id):
        """
        Lit un magasin par son ID.
        :param store_id: ID du magasin
        :return: Le magasin correspondant
        """
        try:
            response = StoreDAO._supabase.table("stores").select("*").eq("id", store_id).execute()
            if response.data:
                return response.data[0]
            else:
                raise ValueError(f"Magasin avec ID {store_id} non trouvé.")
        except Exception as e:
            raise RuntimeError(f"Erreur lors de la lecture du magasin : {e}")

    @staticmethod
    def read_all():
        """
        Récupère tous les magasins.
        :return: Liste des magasins
        """
        try:
            response = StoreDAO._supabase.table("stores").select("*").execute()
            return response.data
        except Exception as e:
            raise RuntimeError(f"Erreur lors de la récupération des magasins : {e}")

    @staticmethod
    def read_by_name(store_name):
        """
        Lit un magasin par son nom.
        :param store_name: Nom du magasin
        :return: Le magasin correspondant
        """
        try:
            response = StoreDAO._supabase.table("stores").select("*").eq("name", store_name).execute()
            if response.data:
                return response.data[0]
            else:
                raise ValueError(f"Magasin avec le nom {store_name} non trouvé.")
        except Exception as e:
            raise RuntimeError(f"Erreur lors de la lecture du magasin par nom : {e}")

    @staticmethod
    def update(store_id, updates):
        """
        Met à jour un magasin existant.
        :param store_id: ID du magasin à mettre à jour
        :param updates: Dictionnaire contenant les mises à jour
        :return: Le magasin mis à jour
        """
        try:
            response = StoreDAO._supabase.table("stores").update(updates).eq("id", store_id).execute()
            if response.data:
                return response.data[0]
            else:
                raise ValueError(f"Erreur lors de la mise à jour : {response.errors}")
        except Exception as e:
            raise RuntimeError(f"Erreur lors de la mise à jour du magasin : {e}")

    @staticmethod
    def delete(store_id):
        """
        Supprime un magasin par son ID.
        :param store_id: ID du magasin à supprimer
        :return: Confirmation de la suppression
        """
        try:
            response = StoreDAO._supabase.table("stores").delete().eq("id", store_id).execute()
            if response.data:
                return response.data[0]
            else:
                raise ValueError(f"Erreur lors de la suppression : {response.errors}")
        except Exception as e:
            raise RuntimeError(f"Erreur lors de la suppression du magasin : {e}")

from connection import Connexion

class Data :

    def get_une_table_bdd(self, id) :
        cursor = Connexion.connecter()

        query = f"SELECT WHERE {id}"
        cursor.execute(query)

        Connexion.deconnecter()

        return 
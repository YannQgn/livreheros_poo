from connection import Connexion
from monstre import Monstre,Potion

class Data :

    def get_monstre_bdd(self,id) :
        cursor = Connexion.connecter()
        query = f"SELECT  nom, classe, points_de_vie, points_dattaque, points_de_defense, chance_de_crit FROM monstre;"
        cursor.execute(query)
        
        results = cursor.fetchall()
        Connexion.deconnecter()
        monstres=[]
        for result in results:
            monstre = Monstre(result[0], result[1], result[2], result[3], result[4], result[5])
            monstres.append(monstre)
            #print(f"monstre: {monstres}")
        return monstres[id]

        
        
        
    def get_potion_bdd(self,id):
        #id 	nom 	type_potion 	valeur 
        cursor = Connexion.connecter()
        query = f"SELECT nom ,type_potion ,valeur FROM potion;"
        cursor.execute(query)
        
        results = cursor.fetchall()
        Connexion.deconnecter()
        potions=[]
        for result in results:
            potion = Potion(result[0], result[1], result[2])
            potions.append(potion)
            #print(f"monstre: {monstres}")
        return potions[id]
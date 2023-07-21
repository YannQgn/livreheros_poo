from data import Data

#from data import get_monstre_bdd
def main():
    monstre_faible=Data().get_monstre_bdd(0)
    monstre_fort=Data().get_monstre_bdd(0)
    boss=Data().get_monstre_bdd(0)
    
    #print(Data().get_monstre_bdd(0)) 
    #print(Data().get_monstre_bdd(1))
    #print(Data().get_monstre_bdd(2))
    print(Data().get_potion_bdd(3))


# lancement de l'app
if __name__ == "__main__":
    main()
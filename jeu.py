from salle import Donjon
from personage import Joueur
from equipements import BarbareEquipement, HealerEquipement, AnalysteEquipement
from difficultes import DifficulteInconnue, Facile, Moyen, Difficile, Hardcore
from salle import Salle, SallePieges, SalleTresor, SalleCombat

def jouer():

    nom_joueur = input("Entrez votre nom: ")
    print("Choisissez votre classe :")
    print("1. Barbare")
    print("2. Healer")
    print("3. Analyste")
    choix_classe = input("Entrez le numéro de votre classe : ")

    difficulte = None
    joueur = None

    if choix_classe == "1":
        difficulte = DifficulteInconnue()
        equipement = BarbareEquipement()
        joueur = Joueur(nom_joueur, "Barbare", equipement, difficulte)
        joueur.points_dattaque += 10
        joueur.points_de_defense += 5
    elif choix_classe == "2":
        difficulte = DifficulteInconnue()
        equipement = HealerEquipement()
        joueur = Joueur(nom_joueur, "Healer", equipement, difficulte)
        joueur.points_de_vie -= 20
        joueur.points_dattaque += 5
    elif choix_classe == "3":
        difficulte = DifficulteInconnue()
        equipement = AnalysteEquipement()
        joueur = Joueur(nom_joueur, "Analyste", equipement, difficulte)
        joueur.points_de_vie -= 10
        joueur.points_dattaque += 7
        joueur.chance_de_crit += 25
    else:
        print("Classe inconnue, vous serez un Joueur par défaut.")
        joueur = Joueur(nom_joueur, "Inconnu", None, difficulte)

    print("\nFélicitations, vous avez créé votre personnage ! Voici vos statistiques :")
    joueur.afficher_stats()

    print("\nChoisissez la difficulté :")
    print("1. Facile")
    print("2. Moyen")
    print("3. Difficile")
    print("4. Hardcore")
    choix_difficulte = input("Entrez le numéro de la difficulté : ")

    if choix_difficulte == "1":
        difficulte = Facile()
        nombre_salles = 4
    elif choix_difficulte == "2":
        difficulte = Moyen()
        nombre_salles = 6
    elif choix_difficulte == "3":
        difficulte = Difficile()
        nombre_salles = 8
    elif choix_difficulte == "4":
        difficulte = Hardcore()
        nombre_salles = 10
    else:
        difficulte = DifficulteInconnue()
        nombre_salles = 4

    print("\nVous avez choisi la difficulté :", difficulte.nom)

    # Met à jour les statistiques du joueur avec la difficulté choisie
    if joueur.classe == "Barbare":
        joueur.points_dattaque += 10
        joueur.points_de_defense += 5
    elif joueur.classe == "Healer":
        joueur.points_de_vie -= 20
        joueur.points_dattaque += 5
    elif joueur.classe == "Analyste":
        joueur.points_de_vie -= 10
        joueur.points_dattaque += 7
        joueur.chance_de_crit += 25

    print("\nVoici vos nouvelles statistiques avec la difficulté :", difficulte.nom)

    # Création du donjon
    donjon = Donjon()
    donjon.generer_salles(difficulte, nombre_salles)

    # Exploration du donjon
    donjon.explorer(joueur)

# Appel de la fonction pour lancer le jeu
jouer()

import random
from equipements import BarbareEquipement, HealerEquipement, AnalysteEquipement
from difficultes import DifficulteInconnue, Facile, Moyen, Difficile, Hardcore
from salle import Salle

class Joueur:
    def __init__(self, nom, classe, equipement, difficulte):
        self.nom = nom
        self.classe = classe
        self.equipement = equipement
        self.difficulte = difficulte
        self.points_de_vie = 100 + difficulte.points_de_vie
        self.points_dattaque = 10 + self.equipement.points_attaque + difficulte.points_dattaque
        self.points_de_defense = 5 + self.equipement.points_defense + difficulte.points_de_defense
        self.chance_de_crit = 10 + difficulte.chance_de_crit

    def afficher_stats(self):
        print("Nom: ", self.nom)
        print("Classe: ", self.classe)
        print("Points de vie: ", self.points_de_vie)
        print("Points d'attaque: ", self.points_dattaque)
        print("Points de défense: ", self.points_de_defense)
        print("Chance de critique:", self.chance_de_crit)
        print("Arme: ", self.equipement.nom)
        print("Difficulté: ", self.difficulte.nom)

    def choisir_direction(self):
        print("Choisissez une direction :")
        print("1. Nord")
        print("2. Est")
        print("3. Sud")
        print("4. Ouest")
        choix_direction = input("Entrez le numéro de la direction : ")
        return choix_direction

    def entrer_salle(self, salle):
        print("\nVous entrez dans la salle :", salle.nom)
        print(salle.description)

        if isinstance(salle, SallePieges):
            print("Vous évitez de justesse les pièges mortels !")
        elif isinstance(salle, SalleTresor):
            print("Vous trouvez un coffre rempli de richesses !")
        elif isinstance(salle, SalleCombat):
            print("Un ennemi redoutable vous attaque !")

        print("")

class Barbare(Joueur):
    def __init__(self, nom, difficulte):
        equipement = BarbareEquipement()
        super().__init__(nom, "Barbare", equipement, difficulte)
        self.points_dattaque += 10
        self.points_de_defense += 5

    def choisir_direction(self):
        print("Choisissez une direction :")
        print("1. Nord")
        print("2. Est")
        print("3. Sud")
        print("4. Ouest")
        choix_direction = input("Entrez le numéro de la direction : ")
        return choix_direction

class Healer(Joueur):
    def __init__(self, nom, difficulte):
        equipement = HealerEquipement()
        super().__init__(nom, "Healer", equipement, difficulte)
        self.points_de_vie -= 20
        self.points_dattaque += 5

    def choisir_direction(self):
        print("Choisissez une direction :")
        print("1. Nord")
        print("2. Est")
        print("3. Sud")
        print("4. Ouest")
        choix_direction = input("Entrez le numéro de la direction : ")
        return choix_direction

class Analyste(Joueur):
    def __init__(self, nom, difficulte):
        equipement = AnalysteEquipement()
        super().__init__(nom, "Analyste", equipement, difficulte)
        self.points_de_vie -= 10
        self.points_dattaque += 7
        self.chance_de_crit += 25

    def choisir_direction(self):
        print("Choisissez une direction :")
        print("1. Nord")
        print("2. Est")
        print("3. Sud")
        print("4. Ouest")
        choix_direction = input("Entrez le numéro de la direction : ")
        return choix_direction

class SallePieges(Salle):
    def __init__(self, nom, description):
        super().__init__(nom, description)

    def entrer(self, joueur):
        print("\nVous entrez dans la salle :", self.nom)
        print(self.description)

        # Implémentez la logique spécifique à la salle des pièges
        print("Vous évitez de justesse les pièges mortels !")

        print("")

class SalleTresor(Salle):
    def __init__(self, nom, description):
        super().__init__(nom, description)

    def entrer(self, joueur):
        print("\nVous entrez dans la salle :", self.nom)
        print(self.description)

        # Implémentez la logique spécifique à la salle du trésor
        print("Vous trouvez un coffre rempli de richesses !")

        print("")

class SalleCombat(Salle):
    def __init__(self, nom, description):
        super().__init__(nom, description)

    def entrer(self, joueur):
        print("\nVous entrez dans la salle :", self.nom)
        print(self.description)

        # Implémentez la logique spécifique à la salle de combat
        print("Un ennemi redoutable vous attaque !")

        print("")



class SalleFeuDeCamp(Salle):
    def __init__(self, nom, description):
        super().__init__(nom, description)

    def rencontrer_aventurier(self, joueur):
        aventuriers_possibles = [Barbare, Healer, Analyste]
        if isinstance(joueur, Healer):
            aventuriers_possibles.remove(Healer)
        elif isinstance(joueur, Barbare):
            aventuriers_possibles.remove(Barbare)
        elif isinstance(joueur, Analyste):
            aventuriers_possibles.remove(Analyste)

        if aventuriers_possibles:
            aventurier = random.choice(aventuriers_possibles)
            return aventurier
        else:
            return None

    def afficher_bonus(self, aventurier):
        if aventurier == Barbare:
            print("Le Barbare vous donne un bonus d'attaque !")
        elif aventurier == Healer:
            print("Le Healer vous soigne et vous donne un bonus de vie !")
        elif aventurier == Analyste:
            print("L'Analyste vous donne un bonus de défense et de chance de critique !")

    def entrer(self, joueur):
        print("\nVous entrez dans la salle :", self.nom)
        print(self.description)

        # Implémentez la logique spécifique à la salle de feu de camp
        aventurier_rencontre = self.rencontrer_aventurier(joueur)

        # Afficher le personnage rencontré
        if aventurier_rencontre == Barbare:
            print("Vous rencontrez un Barbare !")
        elif aventurier_rencontre == Healer:
            print("Vous rencontrez un Healer !")
        elif aventurier_rencontre == Analyste:
            print("Vous rencontrez un Analyste !")

        # Traiter le bonus en fonction du personnage rencontré
        self.afficher_bonus(aventurier_rencontre)

        # Appliquer le bonus au joueur
        if isinstance(aventurier_rencontre, Barbare):
            joueur.points_dattaque += 5
        elif isinstance(aventurier_rencontre, Healer):
            joueur.points_de_vie += 20
        elif isinstance(aventurier_rencontre, Analyste):
            joueur.points_de_defense += 5
            joueur.chance_de_crit += 10

        print("")

class Donjon:
    def __init__(self):
        self.salles = []

    def ajouter_salle(self, salle):
        self.salles.append(salle)

    def generer_salles(self, difficulte, nombre_salles):
        # Liste des salles disponibles
        liste_salles = [
            Salle("Salle des pièges", "Vous êtes entouré de pièges mortels."),
            Salle("Salle du trésor", "Vous trouvez un trésor rempli de richesses."),
            Salle("Salle du combat", "Un monstre redoutable vous attaque !"),
            SalleFeuDeCamp("Salle feu de camp", "Vous rencontrez un aventurier."),
            # ... Ajoutez d'autres salles selon vos besoins
        ]

        # Vérifie si le nombre de salles demandé est supérieur à la taille de la liste
        if nombre_salles > len(liste_salles):
            nombre_salles = len(liste_salles)

        # Mélange aléatoire des salles
        random.shuffle(liste_salles)

        # Sélection des salles en fonction de la difficulté et du nombre de salles requis
        for i in range(nombre_salles - 1):
            salle = liste_salles[i]
            self.ajouter_salle(salle)

        # Ajout de la salle du Boss
        salle_boss = Salle("Salle du Boss", "Un boss redoutable vous attend !")
        self.ajouter_salle(salle_boss)

    def explorer(self, joueur):
        for salle in self.salles:
            choix_direction = joueur.choisir_direction()

            # Vérifier si la salle est une SalleFeuDeCamp pour appeler sa méthode entrer() spécifique
            if isinstance(salle, SalleFeuDeCamp):
                salle.entrer(joueur)
            else:
                joueur.entrer_salle(salle)

# Exemple d'utilisation
nom_joueur = input("Entrez votre nom: ")
print("Choisissez votre classe :")
print("1. Barbare")
print("2. Healer")
print("3. Analyste")
choix_classe = input("Entrez le numéro de votre classe : ")

difficulte = None

if choix_classe == "1":
    difficulte = DifficulteInconnue()
    joueur = Barbare(nom_joueur, difficulte)
elif choix_classe == "2":
    difficulte = DifficulteInconnue()  # Difficulté par défaut pour la classe Healer
    joueur = Healer(nom_joueur, difficulte)
elif choix_classe == "3":
    difficulte = DifficulteInconnue()  # Difficulté par défaut pour la classe Analyste
    joueur = Analyste(nom_joueur, difficulte)
else:
    difficulte = None
    joueur = Joueur(nom_joueur, "Inconnu", None, difficulte)

print("\nFélicitations, vous avez créé votre personnage ! Voici vos statistiques :")
joueur.afficher_stats()

# Choix de la difficulté
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
if isinstance(joueur, Barbare):
    joueur = Barbare(nom_joueur, difficulte)
elif isinstance(joueur, Healer):
    joueur = Healer(nom_joueur, difficulte)
elif isinstance(joueur, Analyste):
    joueur = Analyste(nom_joueur, difficulte)

print("\nVoici vos nouvelles statistiques avec la difficulté :", difficulte.nom)

# Création du donjon
donjon = Donjon()
donjon.generer_salles(difficulte, nombre_salles)

# Exploration du donjon
donjon.explorer(joueur)
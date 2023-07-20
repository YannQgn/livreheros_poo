import random

class Salle:
    def __init__(self, nom, description):
        self.nom = nom
        self.description = description

    def entrer(self, joueur):
        print("Vous entrez dans la salle :", self.nom)
        print(self.description)

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
        # Déplacer l'importation ici pour éviter les problèmes de circularité
        from personage import Barbare, Healer, Analyste

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
        # Déplacer l'importation ici pour éviter les problèmes de circularité
        from personage import Barbare, Healer, Analyste

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

        # Déplacer l'importation ici pour éviter les problèmes de circularité
        from personage import Barbare, Healer, Analyste

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

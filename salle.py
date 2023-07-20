import random
from potion import Potion
class Salle:
    def __init__(self, nom, description):
        self.nom = nom
        self.description = description

    def __str__(self):
        return f"{self.nom}: {self.description}"

    def entrer(self, joueur):
        print("\nVous entrez dans la salle :", self.nom)
        print(self.description)

    def __potion_random__(self,joueur,pourcentage):
        # par exemple: 0.3 = 30% de chances de trouver une potion
        if random.random() < pourcentage :           
            liste_bonus = ["bonus_attaque","bonus_vie","bonus_defense","bonus_chance_critique"]
            random_bonus = random.choice(liste_bonus)
            chiffre_random = 0
            match random_bonus:
                case "bonus_attaque":
                    chiffre_random = random.randint(5,15)
                case "bonus_vie":
                    chiffre_random = random.randint(10,30)
                case "bonus_defense":
                    chiffre_random = random.randint(2,10)
                case "bonus_chance_critique":
                    chiffre_random = random.randint(1,10)          
            potion = Potion("Potion magique",random_bonus=chiffre_random)
            print(f"Vous trouvez une potion magique de {random_bonus} qui vous augmente de {chiffre_random} points.")
            potion.utiliser(joueur, bonus_type=random_bonus)

class SallePieges(Salle):
    def __init__(self, nom, description):
        super().__init__(nom, description)

    def entrer(self, joueur):
        print(super().__str__())  # Utiliser la méthode __str__ pour afficher le nom spécifique de la salle
        choix = input("Voulez-vous essayer de désamorcer les pièges ? (Oui/Non) : ")
        if choix.lower() == "oui":
            reussite = random.random() < 0.5  # 50% de chance de réussite
            if reussite:
                print("Félicitations ! Vous avez réussi à désamorcer les pièges.")
            else:
                print("Malheureusement, vous n'avez pas réussi à désamorcer les pièges et subissez des dégâts.")
                joueur.points_de_vie -= 10
        else:
            print("Vous décidez de contourner prudemment les pièges.")
        super().__potion_random__(joueur,random.random() < 0.3)
        print("")

class SalleTresor(Salle):
    def __init__(self, nom, description):
        super().__init__(nom, description)

    def entrer(self, joueur):
        print(super().__str__())  # Utiliser la méthode __str__ pour afficher le nom spécifique de la salle
        choix = input("Voulez-vous ouvrir le coffre ? (Oui/Non) : ")
        if choix.lower() == "oui":
            tresor = random.randint(10, 50)  # Montant aléatoire du trésor
            joueur.points_dattaque += tresor
            print(f"Vous trouvez un coffre rempli de richesses ! Votre attaque augmente de {tresor} points.")
        else:
            print("Vous décidez de ne pas ouvrir le coffre.")
        super().__potion_random__(joueur,random.random() < 0.3)
        print("")

class SalleFeuDeCamp(Salle):
    def __init__(self, nom, description):
        super().__init__(nom, description)

    def rencontrer_aventurier(self, joueur):
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
        super().__potion_random__(joueur,random.random() < 0.3)
        print("")

class SalleCombat(Salle):
    def __init__(self, nom, description):
        super().__init__(nom, description)

    def entrer(self, joueur):
        print("\nVous entrez dans la salle :", self.nom)
        print(self.description)
        # Implémentez la logique spécifique à la salle de combat
        ennemi = "Dragon"  # Remplacez par le nom de l'ennemi approprié
        print(f"Un {ennemi} redoutable vous attaque !")
        choix = input("Voulez-vous combattre l'ennemi ? (Oui/Non) : ")
        if choix.lower() == "oui":
            reussite = random.random() < 0.7  # 70% de chance de réussite
            if reussite:
                print(f"Bravo ! Vous avez vaincu le {ennemi}.")
            else:
                print(f"Le {ennemi} était trop puissant pour vous. Vous subissez des dégâts.")
                joueur.points_de_vie -= 30
        else:
            print("Vous décidez de fuir le combat.")
        super().__potion_random__(joueur,random.random() < 0.3)
        print("")

class Donjon:
    def __init__(self):
        self.salles = []

    def ajouter_salle(self, salle):
        self.salles.append(salle)

    def generer_salles(self, difficulte, nombre_salles):
        # Liste des salles disponibles
        liste_salles = [
            SallePieges("Salle des pièges", "Vous êtes entouré de pièges mortels."),
            SalleTresor("Salle du trésor", "Vous trouvez un trésor rempli de richesses."),
            SalleFeuDeCamp("Salle feu de camp", "Vous rencontrez un aventurier."),
            SalleCombat ("Salle des montres", "Vous tombé sur un groupe de monstre")
            # Ajouter d'autres salles selon vos besoins
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
            salle.entrer(joueur)  # Utiliser la méthode polymorphe entrer() pour chaque type de salle

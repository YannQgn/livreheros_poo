import random
import random
import torch
from connection import Connexion
from potion import Potion
from api_gpt import API_GPT

# Ajouter la constante PROMPT_DONJON pour définir le contexte de l'aventure
PROMPT_DONJON = "Dans un univers médiéval fantastique, vous êtes un aventurier courageux qui rêve de devenir riche. Vous décidez de parcourir un donjon mystérieux dans l'espoir de trouver des trésors cachés et de l'argent. Vous vous trouvez actuellement dans une salle du donjon."

class Salle:
    def __init__(self, nom, description):
        self.nom = nom
        self.description = description

    def __str__(self):
        return f"{self.nom}: {self.description}"

    def entrer(self, joueur):
        print("\nVous entrez dans la salle :", self.nom)
        print(self.description)

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

        print("")

class SalleCombat(Salle):
    def __init__(self, nom, description):
        super().__init__(nom, description)

    def choisir_monstre_aleatoire(self):
        conn = Connexion.connecter()  # Utiliser la méthode de connexion pour récupérer l'objet de connexion
        cursor = conn.cursor()  # Récupérer un curseur à partir de l'objet de connexion

        cursor.execute("SELECT * FROM monstre WHERE id <> 3 ORDER BY RAND() LIMIT 1")
        monstre_data = cursor.fetchone()
        monstre = {
            "nom": monstre_data[1],
            "classe": monstre_data[2],
            "points_de_vie": monstre_data[3],
            "points_dattaque": monstre_data[4],
            "points_de_defense": monstre_data[5],
            "chance_de_crit": monstre_data[6]
        }

        cursor.close()
        Connexion.deconnecter()  # Utiliser la méthode deconnexion pour fermer le curseur et la connexion

        return monstre

    def entrer(self, joueur):
        print("\nVous entrez dans la salle :", self.nom)
        print(self.description)

        monstre = self.choisir_monstre_aleatoire()

        print(f"Un {monstre['nom']} vous attaque !")

        choix = input("Voulez-vous combattre le monstre ? (Oui/Non) : ")
        if choix.lower() == "oui":
            reussite = random.random() < 0.7  # 70% de chance de réussite
            if reussite:
                print(f"Bravo ! Vous avez vaincu le {monstre['nom']}.")
            else:
                print(f"Le {monstre['nom']} était trop puissant pour vous. Vous subissez des dégâts.")
                joueur.points_de_vie -= 30
        else:
            print("Vous décidez de fuir le combat.")

        print("")

class SalleBoss(SalleCombat):
    def __init__(self, nom, description):
        super().__init__(nom, description)

    def choisir_monstre_fixe(self):
        conn = Connexion.connecter()  # Utiliser la méthode de connexion pour récupérer le curseur

        # Sélectionner le monstre avec l'ID 3 (monstre3) dans la base de données
        conn.execute("SELECT * FROM monstre WHERE id = 3")
        monstre_data = conn.fetchone()
        monstre = {
            "nom": monstre_data[1],
            "classe": monstre_data[2],
            "points_de_vie": monstre_data[3],
            "points_dattaque": monstre_data[4],
            "points_de_defense": monstre_data[5],
            "chance_de_crit": monstre_data[6]
        }

        conn.close()
        Connexion.deconnecter()  # Utiliser la méthode deconnexion pour fermer la connexion

        return monstre

    def entrer(self, joueur):
        print(super().__str__())  # Utiliser la méthode __str__ pour afficher le nom spécifique de la salle
        boss = "Stephane Le Dévoreur d'espoir"  # Nom du boss, vous pouvez le personnaliser
        print(f"Un {boss} terrifiant vous attaque !")

        while True:
            choix = input("Voulez-vous combattre le boss ? (Oui/Non) : ")
            if choix.lower() == "oui":
                reussite = random.random() < 0.3  # 30% de chance de réussite contre le boss
                if reussite:
                    print(f"Félicitations ! Vous avez vaincu le {boss}. Vous avez gagné le jeu !")
                    break
                else:
                    print(f"Le {boss} Attaque pédagogie ACTIVE. Vous subissez de lourds dégâts.")
                    joueur.points_de_vie -= 70
                    if joueur.points_de_vie <= 0:
                        print("Vous êtes mort. Game Over.")
                        break
            else:
                print("Vous ne pouvez pas fuir le combat contre le boss. Vous devez combattre !")

        print("")

class SallePotion(Salle):
    def __init__(self, nom, description):
        super().__init__(nom, description)
        self.potion = None

    def generer_potion(self):
        conn = Connexion.connecter()
        cursor = conn.cursor()

        # Modifier la requête SQL pour récupérer spécifiquement la potion "Le_Graal"
        cursor.execute("SELECT * FROM potion WHERE nom='Le_Graal' LIMIT 1")
        potion_data = cursor.fetchone()

        if potion_data:
            self.potion = Potion(potion_data[1], potion_data[2], potion_data[3])

        cursor.close()
        Connexion.deconnecter()

class SallePotion(Salle):
    def __init__(self, nom, description):
        super().__init__(nom, description)
        self.potion = None

    def generer_potion(self):
        conn = Connexion.connecter()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM potion ORDER BY RAND() LIMIT 1")
        potion_data = cursor.fetchone()

        if potion_data:
            self.potion = Potion(potion_data[1], potion_data[2], potion_data[3])

        cursor.close()
        Connexion.deconnecter()

    def entrer(self, joueur):
        print("\nVous entrez dans la salle :", self.nom)
        print(self.description)

        self.generer_potion()

        if self.potion:
            print(f"Vous trouvez une potion : {self.potion.nom}")
            choix = input("Voulez-vous utiliser la potion ? (Oui/Non) : ")
            if choix.lower() == "oui":
                self.potion.utiliser(joueur)
                if self.potion.type_potion == "Le_Graal":
                    joueur.points_de_vie = 0
                    print("Vous buvez la potion Le_Graal... Vous êtes mort.")
                    print("Game Over.")
                    return  # Quit the game if the player is dead
            else:
                print("Vous décidez de ne pas utiliser la potion.")

        else:
            print("Vous explorez la salle mais ne trouvez aucune potion.")

        # Check if the player is still alive after using another potion
        if joueur.points_de_vie <= 0:
            print("Vous êtes mort. Game Over.")
            return  # Quit the game if the player is dead

        print("")


class Donjon:
    def __init__(self):
        self.salles = []
        self.difficulte = None
        self.nombre_salles = 0

    def ajouter_salle(self, salle):
        self.salles.append(salle)

    def generer_salles(self):
        # Liste des salles disponibles
        liste_salles = [
            SallePieges("Salle des pièges", "Vous êtes entouré de pièges mortels."),
            SalleTresor("Salle du trésor", "Vous trouvez un trésor rempli de richesses."),
            SalleFeuDeCamp("Salle feu de camp", "Vous rencontrez un aventurier."),
            SalleCombat ("Salle des monstres", "Vous tombez sur un groupe de monstres"),
            SallePotion ("Salle des potion" , "Vous tombez dans une salle rempli de potion bizarre")
            # Ajouter d'autres salles selon vos besoins
        ]

        # Vérifie si le nombre de salles demandé est supérieur à la taille de la liste
        if self.nombre_salles > len(liste_salles):
            self.nombre_salles = len(liste_salles)

        # Mélange aléatoire des salles
        random.shuffle(liste_salles)

        # Sélection des salles en fonction de la difficulté et du nombre de salles requis
        for i in range(self.nombre_salles - 1):
            salle = liste_salles[i]
            self.ajouter_salle(salle)

        # Ajout de la salle du Boss
        salle_boss = SalleBoss("Salle du Boss", "Un boss redoutable vous attend !")
        self.ajouter_salle(salle_boss)

    def obtenir_description_environnement(self, coordonnees_personnage):
        latitude, longitude = coordonnees_personnage

        # Générer une description en utilisant GPT-3.5
        query = PROMPT_DONJON
        description = API_GPT.demande_GPT(query)

        return description

    def explorer(self, joueur):
        for salle in self.salles:
            choix_direction = joueur.choisir_direction()
            salle.entrer(joueur)  # Utiliser la méthode polymorphe entrer() pour chaque type de salle
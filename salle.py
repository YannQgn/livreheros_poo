class Salle:
    def __init__(self, nom, description):
        self.nom = nom
        self.description = description

    def entrer(self, joueur):
        print("Vous entrez dans la salle :", self.nom)
        print(self.description)

class Equipement:
    def __init__(self, nom, points_attaque, points_defense):
        self.nom = nom
        self.points_attaque = points_attaque
        self.points_defense = points_defense


class BarbareEquipement:
    def __init__(self):
        self.nom = "Hache de guerre"
        self.points_attaque = 15
        self.points_defense = 5


class HealerEquipement:
    def __init__(self):
        self.nom = "Bâton de guérison"
        self.points_attaque = 5
        self.points_defense = 10


class AnalysteEquipement:
    def __init__(self):
        self.nom = "Lunettes d'analyse"
        self.points_attaque = 10
        self.points_defense = 5


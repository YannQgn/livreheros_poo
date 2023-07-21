import mysql.connector as mysqlpy

class Connexion:
    __USER = 'root'
    __PWD = 'example'
    __HOST = 'localhost'
    __PORT = '3307'
    __DB = 'poo'
    __bdd = None

    @classmethod
    def connecter(cls):
        if cls.__bdd is None:
            cls.__bdd = mysqlpy.connect(user=cls.__USER, password=cls.__PWD, host=cls.__HOST, port=cls.__PORT, database=cls.__DB)
        
        return cls.__bdd

    @classmethod
    def deconnecter(cls):
        if cls.__bdd is not None:
            cls.__bdd.close()
            cls.__bdd = None

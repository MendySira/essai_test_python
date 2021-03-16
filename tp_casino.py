#tp_casino.py
from random import randrange
from math import ceil 

#Creation de la classe joueur
class Joueur:
    #constructeur
    def __init__(self, name, argent):
        self.name = name
        self.argent = argent
        print("Bonjour %s ,vous avez actuellement %d $ sur votre compte\n" %(self.name,self.argent))
    #Destructeur s'activera lorsque le joueur quitte le casino
    def __del__(self):
        print("%s a %d $ restant et quitte le casino\n" %(self.name,self.argent))
    #Fonction pour voir l'argent restant du joueur et l'afficher
    def voir_compte(self):
        print("Il vous reste %d $ dans votre compte\n" %(self.argent))
        
#Creation de la classe casino              
class Casino:
    #Constructeur
    def __init__(self, name, joueur):
        self.numero_gagnant = 1
        self.numero_mise = 2
        self.argent_mise = 10
        self.name = name
        print("Bonjour Mr(Mme) %s ,bienvenue dans le casino %s, actuellement vous avez %d $\n" %(joueur.name,self.name,joueur.argent))
        print("Une personne vous montre la direction sur la roulette afin de vous s'y installer\n")
        
    #Fonction pour les choses qui se passe quand le joueur joue à la roullette    
    def jouer_roulette(self,argent_mise,numero_mise,joueur):
        self.numero_gagnant = randrange(50)
        self.numero_mise = numero_mise
        self.argent_mise = argent_mise
        #Pour voir si numero mise est pair ou impair et afficher sa couleur
        if self.numero_mise%2 == 0:
            print("Vous avez mise %d $ sur le numéro %d noir\n" %(self.argent_mise,self.numero_mise))
        else:
            print("Vous avez mise %d $ sur le numéro %d rouge\n" %(self.argent_mise,self.numero_mise))

        #Pour voir si numero gagnant est pair ou impair et afficher sa couleur    
        if self.numero_gagnant%2 == 0:
            print("Le numéro gagnant est le %d noir\n" %(self.numero_gagnant))
        else:
            print("Le numéro gagnant est le %d rouge\n" %(self.numero_gagnant))

        #Pour voir si le joueur a gagne ou pas    
        if self.numero_gagnant == self.numero_mise:
            joueur.argent += self.argent_mise*3
            print("Oulala vous avez une chance de ouf, vous avez gagné %d $" %(self.argent_mise*3))
        elif self.numero_gagnant%2 != 0 and self.numero_mise%2 != 0:
            joueur.argent += ceil(self.argent_mise*0.5)
            print("Ah on dirait bien que le rouge est votre couleur porte bonheur, vous avez trouver la bonne couleur et gagner %d $\n"%(ceil(self.argent_mise*0.5)))
        elif self.numero_gagnant%2 == 0 and self.numero_mise%2 == 0:
            #ceil ici va arondir la valeur trouve et la mettre en integer pour que joueur.argent reste en integer 
            joueur.argent += ceil(self.argent_mise*0.5)
            print("Hmm vous aimez le noir? et bien moi aussi, vous avez trouver la bonne couleur et gagner %d $\n"%(ceil(self.argent_mise*0.5)))
        else:
            joueur.argent += -self.argent_mise
            print("Oooh! vous avez perdu %d $, vous avez pas eu ni la bonne couleur ni le bon numéro, peut être vous aurez plus de chance la prochaine fois qui sait\n" %(self.argent_mise))
        

#Verification si le nom du joueur entrer par l'utilisateur est belle et bien un string et reste dans la boucle que si la condition n'est pas respecter
nom_joueur = -1
while nom_joueur == -1:
    nom_joueur = "The Mike"
    #Dans le cas ou l'utlisateur a entrer un nom pas en string(int,...)    
    try:
        nom_joueur = int(nom_joueur)
        print("Vous avez saisie un nombre\n")
        nom_joueur = -1
    #Dans le cas ou l'utlisateur a entrer un nom en string
    except ValueError:
        #print("Vous avez saisie un string\n")  
        continue
            
#Verification si l'argent total  sur le comtpe du joueur entrer par l'utilisateur est belle et bien un integer et reste dans la boucle que si la condition n'est pas respecter
argent_compte = -1
while argent_compte == -1:
    argent_compte = 5000
    #Dans le cas ou l'utlisateur a entrer un argent en int    
    try:
        argent_compte = int(argent_compte)
        #print("Vous avez saisie un nombre\n")       
    #Dans le cas ou l'utlisateur a entrer un argent qui n'est pas un integer
    except ValueError:
        print("Vous n avez pas saisie un nombre\n") 
        argent_compte = -1
        continue
    #Dans le cas ou l'utlisateur a entrer un argent inférieur ou égale à 0
    if argent_compte <= 0:
        print("Vous ne pouvez pas avoir une somme d'argent nulle ou négative sur votre compte\n")
        argent_compte = -1


#Creation de la classe Joueur qui s'appelle p1
p1 = Joueur(nom_joueur, argent_compte)

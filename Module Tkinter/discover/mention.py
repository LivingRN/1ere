from tkinter import Tk, Label, Entry, Button, StringVar
           
### Modèle
def calcul_mention():
    """Calcul de la mention
    Modifie la variable de contrôle mention"""
    m = float(moyenne.get())
    if 0<= m <=20:
        if m < 8:
            mention.set("Refusé")
        elif m < 10:
            mention.set("Passe second groupe")
        elif m < 12:
            mention.set("Passable")
        elif m < 14:
            mention.set("Mention Assez Bien")
        # à compléter avec tous les autres cas de mention
    else:
        mention.set("Valeur non conforme")

def calcul_mention_bac():
    """Calcul de la mention au bac
    Modifie la variable de contrôle mention"""
    m = float(moyenne.get())
    if 0<= m <=20:
        if m < 10:
            mention.set("Refusé")
        elif m < 12:
            mention.set("Passable")
        elif m < 14:
            mention.set("Mention Assez Bien")
        elif m < 16:
            mention.set("Mention Bien")
        elif m < 18:
            mention.set("Mention Très Bien")
        else:
            mention.set("Mention Très Bien avec félicitations du jury")
    else:
        mention.set("Valeur non conforme")

### Vue : interface graphique

# Fenêtre racine
fen = Tk()
fen.title("Compte à rebours")
fen.geometry("600x300")
fen.resizable(width=False, height=False)
# Variables de contrôles (variables globales)
moyenne = StringVar()  # variable de contrôle du widget saisie_moyenne
mention = StringVar()  # variable de contrôle du widget etiq_mention 
# Etiquette du champ de saisie
etiq_moy = Label(fen, text="Moyenne : ", font=("Arial", 20))
etiq_moy.pack()
# Champ de saisie de la moyenne
saisie_moyenne = Entry(fen, textvariable=moyenne, font=("Arial", 20), fg='blue')
saisie_moyenne.pack()
# Bouton de commande
bouton = Button(fen, text="Calcul mention", command=calcul_mention_bac, font=("Arial", 20))
bouton.pack()
# Etiquette d'affichage de la mention
etiq_mention = Label(fen, textvariable=mention, font=("Arial", 20), fg='red')
etiq_mention.pack()
    
### Boucle infinie , réceptionnaire d'événement
fen.mainloop()
from tkinter import Tk, Canvas
import random

### Constantes (valeurs non modifiables à l'execution)
HAUT_FENETRE = 400
LARG_FENETRE = 400


### Fonctions : boite à outils 

def from_rgb(r, g, b):
    """
    Description :

    Renvoie le codage RGB d'une couleur en notation HTML au format #FF00AA
    à partir des composantes rouge r, vert v et bleue b

    Paramètre :
        r : entier entre 0 et 255
        g : entier entre 0 et 255
        b : entier entre 0 et 255

    Renvoie : 
        une chaine de caractères de type str
    """
    # Préconditions sur les paramètres
    assert isinstance(r, int) and 0 <= r <= 255, "r doit être un entier entre 0 et 255"
    assert isinstance(g, int) and 0 <= g <= 255, "g doit être un entier entre 0 et 255"
    assert isinstance(b, int) and 0 <= g <= 255, "b doit être un entier entre 0 et 255"
    # valeur renvoyée
    return f'#{r:02x}{g:02x}{b:02x}'

### Modèle

def ballon(event):
    """Fonction gestionnaire de l'événement
    clic sur bouton gauche de souris"""
    rouge = random.randint(0, 255)
    vert = random.randint(0, 255)
    bleu = random.randint(0, 255)
    can.create_oval(event.x - 10, event.y - 10, event.x + 10, event.y + 10, fill=from_rgb(rouge, vert, bleu))
    fen.update()

### Vue : interface graphique
# Fenetre racine
fen = Tk()
fen.title("Clic ballon")


# Canevas d'affichage de la barre
can = Canvas(fen, background="#000000", width=LARG_FENETRE, height=HAUT_FENETRE)
can.pack()
            


### Controleur

# Si l'événement "Appui sur une touche" est intercepté, on appelle la fonction deplacement
fen.bind("<ButtonPress-1>",  ballon)

### Boucle infinie , réceptionnaire d'événement
fen.mainloop()
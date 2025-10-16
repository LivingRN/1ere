from tkinter import Tk, Canvas

### Constantes (valeurs non modifiables à l'exécution)
LARG_BARRE = 60  # largeur de la barre en pixels
HAUT_BARRE = 20  # hauteur de la barre en pixels
DX = 10          # déplacement horizontal en pixels pour un appui sur touche
DY = 10          # déplacement vertical en pixels pour un appui sur touche
HAUT_FENETRE = 400
LARG_FENETRE = 400

### Variables globales (valeurs modifiables à l'exécution)
x_barre = 160
y_barre = 180
    
### Vue : interface graphique
# Fenêtre racine
fen = Tk()
fen.title("Controle Barre")


# Canevas d'affichage de la barre
can = Canvas(fen, background="#000000", width=LARG_FENETRE, height=HAUT_FENETRE)
can.pack()
# Barre rectangulaire dessinée dans le canevas
barre = can.create_rectangle(x_barre, y_barre, x_barre + LARG_BARRE, y_barre + HAUT_BARRE, fill="white")

### Modèle

def deplacement(event):
    """Fonction gestionnaire de l'événement
    appui sur une touche"""
    global x_barre, y_barre
    if event.keysym == 'Up':
            y_barre = max(0, y_barre - DY)
    elif event.keysym == 'Down':
            y_barre = min(y_barre + DY,  HAUT_FENETRE - HAUT_BARRE)
    elif event.keysym == 'Right':
            x_barre = min(x_barre + DX, LARG_FENETRE - LARG_BARRE,)  
    elif event.keysym == 'Left':
            x_barre = max(0, x_barre - DX)       
    can.coords(barre, x_barre, y_barre, x_barre + LARG_BARRE, y_barre + HAUT_BARRE)
    fen.update()
            


### Controleur

# Si l'événement "Appui sur une touche" est intercepté, on appelle la fonction deplacement
fen.bind("<KeyPress>",  deplacement)

### Boucle infinie , réceptionnaire d'événement
fen.mainloop()
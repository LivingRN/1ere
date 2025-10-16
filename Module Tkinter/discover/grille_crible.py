from tkinter import Tk, Canvas, Button
import random

def action_bouton():
    y = random.randint(0, 19)
    x = random.randint(0, 29)
    id_rec = grille[y][x]
    print(can.itemcget(id_rec, "fill"))
    can.itemconfig(id_rec, fill="#0000ff")
    
# Définition de l'interface graphique

# Fenêtre racine
fen = Tk()
fen.title("Crible aléatoire")
# Canevas
can = Canvas(fen, width=300, height=200)
can.pack() # positionnement
# dessin d'une grillee de 20 x 30 rectangles de coté 10 pixels stockés dans une liste de listes 
# pour récupérer leurs identifiants
grille = [
    [
        can.create_rectangle(
            x * 10,
            y * 10,
            (x + 1) * 10,
            (y + 1) * 10,
            outline="red",
            fill="#ffffff",
        )
        for x in range(30)
    ]
    for y in range(20)
]

# Bouton de contrôle
bouton = Button(fen, text="Crible !", command=action_bouton)
bouton.pack()

fen.mainloop()
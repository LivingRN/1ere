from tkinter import *                   # import du module

fen = Tk()                              # création de la fenêtre racine

fen.geometry("300x50")
fen.resizable(width=False, height=False)

msg = Label(                            # création d'un widget Label dans la fenêtre racine
    fen, 
    text="Hello World", 
    font=("Arial", 20))                 

msg.pack()                              # positionnement géométrique du widget avec la méthode `pack`
fen.mainloop()                          # boucle infinie avec réceptionnaire d'événements
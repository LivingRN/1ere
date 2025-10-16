from tkinter import Entry, Label, IntVar, Scale, Tk, Canvas, Frame, Button


# Fenêtre racine
fen = Tk()
fen.title("Compte à rebours")
fen.geometry("600x300")
fen.resizable(width=False, height=False)
# Variables de contrôles (variables globales)
rouge = IntVar()  # variable de contrôle du widget saisie_rouge
verte = IntVar()  # variable de contrôle du widget saisie_verte
bleue = IntVar()  # variable de contrôle du widget saisie_bleue
# Saisies des couleurs
color = [
Scale(fen, orient='horizontal', from_=0, to=255,
      resolution=0.1, tickinterval=2, length=350,
      label='Rouge', variable=rouge),
Scale(fen, orient='horizontal', from_=0, to=255,
      resolution=0.1, tickinterval=2, length=350,
      label='Vert', variable=verte),
Scale(fen, orient='horizontal', from_=0, to=255,
      resolution=0.1, tickinterval=2, length=350,
      label='Bleu', variable=bleue),
]
saisie_rouge = Entry(fen, width=10)
saisie_rouge.pack()
saisie_verte = Entry(fen, width=10)
saisie_verte.pack()
saisie_bleue = Entry(fen, width=10)
saisie_bleue.pack()

    
### Boucle infinie , réceptionnaire d'événement
fen.mainloop()
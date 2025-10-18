# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Affichage minimal d'une grille Sudoku avec pygame (version Codespaces).

Ce module dessine une grille 9x9 et sauvegarde un screenshot.
"""

import sys
import os
import pygame

os.environ['SDL_VIDEODRIVER'] = 'dummy' # For Codespaces compatibility

GRILLE = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

LARGEUR, HAUTEUR = 1080, 720
CELL = 60
FICHIER_IMAGE = "Mini Projet 1/Mini Projet 1 - GUI/pygame_screenshot.png"

def dessiner(ecran: pygame.Surface):
    """Dessine la grille Sudoku sur la surface fournie et sauvegarde l'image."""
    blanc = (255,255,255)
    noir = (0,0,0)
    gris = (180,180,180)

    ecran.fill(blanc)
    taille = CELL*9
    grille = pygame.Surface((taille, taille))
    grille.fill(blanc)

    # lignes fines
    for i in range(10):
        if i % 3 != 0:
            pygame.draw.line(grille, gris, (i*CELL,0),(i*CELL,taille),1)
            pygame.draw.line(grille, gris, (0,i*CELL),(taille,i*CELL),1)

    # lignes épaisses 3x3
    for i in range(4):
        pygame.draw.line(grille, noir, (i*3*CELL,0),(i*3*CELL,taille),4)
        pygame.draw.line(grille, noir, (0,i*3*CELL),(taille,i*3*CELL),4)

    # nombres
    police = pygame.font.Font(None, 40)
    for i in range(9):
        for j in range(9):
            val = GRILLE[i][j]
            if val:
                txt = police.render(str(val), True, noir)
                rect = txt.get_rect(center=(j*CELL+CELL//2, i*CELL+CELL//2))
                grille.blit(txt, rect)

    ecran.blit(grille, ((LARGEUR-taille)//2, (HAUTEUR-taille)//2))
    pygame.display.flip()
    pygame.image.save(ecran, FICHIER_IMAGE)


def main():
    """Initialise pygame et boucle principale. Utiliser --once pour quitter après le rendu."""
    pygame.init()
    ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
    dessiner(ecran)

    if "--once" in sys.argv:
        pygame.quit()
        return

    horloge = pygame.time.Clock()
    while True:
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                pygame.quit()
                return
        horloge.tick(60)


if __name__ == '__main__':
    main()
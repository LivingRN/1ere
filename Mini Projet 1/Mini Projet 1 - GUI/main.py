# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Affichage minimal d'une grille Sudoku avec pygame.

Ce module dessine une grille 9x9.
"""

import pygame

grille = [
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

largeur, hauteur = 600, 600  # Taille de la fenêtre

def dessiner_sudoku(ecran: pygame.Surface, x: int, y: int, taille_cellule: int = 60) -> None:
    """Dessine la grille de Sudoku sur l'écran donné.

    Args:
        ecran (pygame.Surface): La surface sur laquelle dessiner la grille.
    """
    sudoku = pygame.Surface((540, 540))
    sudoku.fill((255, 255, 255))
    
    # Dessiner les lignes de la grille
    for i in range(10):
        epaisseur = 4 if i % 3 == 0 else 1
        pygame.draw.line(sudoku, (0, 0, 0), (0, i * taille_cellule), (sudoku.get_width(), i * taille_cellule), epaisseur)
        pygame.draw.line(sudoku, (0, 0, 0), (i * taille_cellule, 0), (i * taille_cellule, sudoku.get_height()), epaisseur)

    # Dessiner les chiffres
    font = pygame.font.SysFont(None, 48)
    for i in range(9):
        for j in range(9):
            if grille[i][j] != 0:
                texte = font.render(str(grille[i][j]), True, (0, 0, 0))
                x_pos = j * taille_cellule + 20
                y_pos = i * taille_cellule + 10
                sudoku.blit(texte, (x_pos, y_pos))

    ecran.blit(sudoku, (x, y))

def dessiner_menu(ecran: pygame.Surface) -> None:
    """Dessine le menu sur l'écran donné.

    Args:
        ecran (pygame.Surface): La surface sur laquelle dessiner le menu.
    """
    ecran.fill((255, 255, 255))  # Remplir l'écran en blanc
    
    # Afficher le titre
    font = pygame.font.SysFont(None, 36)
    texte = font.render("Sudoku", True, (0, 0, 0))
    ecran.blit(texte, ((largeur - texte.get_width()) // 2, 10))  # au centre
    
    # Afficher les buttons (instructions, nouvelle partie, quitter, etc.) qui declenchent des actions (fonctions non implémentées ici)
    ## Afficher le bouton 'instructions'
    font = pygame.font.SysFont(None, 24)
    texte = font.render("Instructions", True, (0, 0, 0))
    ecran.blit(texte, (50, 50))

def main() -> None:
    """Point d'entrée principal du programme."""
    global largeur, hauteur
    
    pygame.init()
    ecran = pygame.display.set_mode((largeur, hauteur), pygame.RESIZABLE)
    pygame.display.set_caption("Sudoku")
    
    clock = pygame.time.Clock()
    running = True

    while running:
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                running = False
            if evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_q:
                    running = False

        largeur, hauteur = ecran.get_size()
        
        dessiner_menu(ecran)
        dessiner_sudoku(ecran, (largeur - 540) // 2, (hauteur - 540) // 2)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    
if __name__ == "__main__":
    main()
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 10:28:10 2025

@author: m.tanguy
"""

import nice_print as np
from dosuko_api import EMPTY_BOARD, get_new_dosuko_board, error_response

class Sudoku:
    def __init__(self):
        self.grid = [row[:] for row in EMPTY_BOARD]
        self.starting_grid = [row[:] for row in EMPTY_BOARD]
        self.difficulty = None
        
        self.__caractere_vide = '.'
        self.__vertical_sep = '|'
        self.__horizontal_sep = '—'
        
    def _empty(self):
        """
        Créer une grille vide.

        Returns
        -------
        None.

        """
        self.grid = [row[:] for row in EMPTY_BOARD]

    def reset(self):
        self.grid = self.starting_grid

    def generate_new_grid(self) -> bool:
        """
        Générer une nouvelle grille et mettre à jour self.grid.

        Returns
        -------
        None.

        """
        
        dosuko_response = get_new_dosuko_board()
        
        if not dosuko_response:
            raise RuntimeError("Erreur lors de la récupération d'une nouvelle grille de Sudoku.")
        
        if 'grid' not in dosuko_response or 'difficulty' not in dosuko_response:
            raise ValueError("La réponse de l'API est invalide.")
        
        if dosuko_response == error_response:
            return False
        
        self.starting_grid = [row[:] for row in dosuko_response['grid']]
        self.difficulty = dosuko_response['difficulty']
        # copy starting_grid so modifications to self.grid don't change starting_grid
        self.grid = [row[:] for row in self.starting_grid]
        
        return True
    
    def _is_valid_before_place(self, row: int, col: int, val: int) -> bool:
        """

        Parameters
        ----------
        row : int
            Position (rangée, 0-8) de la valeur.
        col : int
            Position (colonne, 0-8) de la valeur.
        val : int
            Valeur à placer.

        Returns
        -------
        bool
            Renvoyer True si la valeur peut etre placer selon ses paramètres, False dans le cas contraire.

        """
        if not(1 <= val <= 9):
            return False
        
        # Si la case est déjà utilisée
        if self.grid[row][col]:
            return False
        
        # Vérifier si la valeur est valide dans la rangée [row]
        if val in self.grid[row]:
            return False
        
        # Vérifier si la valeur est valide dans la colonne [col]
        for r in self.grid:
            if val == r[col]:
                return False
        
        # Vérifier si la valeur est valide dans son carré 3x3
        debut = (
            row - row%3,
            col - col%3
        )
        fin = (
            row + (2 - row%3),
            col + (2 - col%3)
        )
        for i in range(debut[0], fin[0] + 1):
            for j in range(debut[1], fin[1] + 1):
                if val == self.grid[i][j]:
                    return False
        
        # la valeur est validée !
        return True

    def place(self, row: int, col: int, val: int) -> bool:
        """
        Placer une valeur [val] si possible.

        Parameters
        ----------
        row : int
            Position de la rangée (index).
        col : int
            Position de la colonne (index).
        val : int
            Valeur à insérer.

        Returns
        -------
        bool
            [True] si la valeur est placée correctement. Sinon, [False].

        """
        if val not in range(1, 10):
            return False
        
        # Verifier si la position (row, col) est modifiable
        if self.starting_grid[row][col] != 0:
            return False
        
        self.grid[row][col] = val
        return True

    def is_solution(self) -> bool:
        """
        Vérifier si la grille est solution

        Returns
        -------
        bool
            [True] si la grille est solution.

        """
        # Vérifier qu'il n'y a pas de cases vides
        if any(0 in row for row in self.grid):
            return False

        # Vérifier que chaque rangée a les valeurs 1 à 9
        if any(set(row) != set(range(1, 10)) for row in self.grid):
            return False

        # Vérifier que chaque colonne a les valeurs 1 à 9
        for c in range(9):
            col_vals = {self.grid[r][c] for r in range(9)}
            if col_vals != set(range(1, 10)):
                return False

        # Vérifier que chaque carré 3x3 a les valeurs de 1 à 9
        for box_row in range(3):
            for box_col in range(3):
                box_vals = set()
                for i in range(3):
                    for j in range(3):
                        box_vals.add(self.grid[box_row*3 + i][box_col*3 + j])
                if box_vals != set(range(1, 10)):
                    return False
        
        # Toutes les vérifications sont passées
        return True
    
    def resoudre(self) -> None:
        """
        Résoudre le sudoku en utilisant une méthode de backtracking

        Returns
        -------
        None

        """
        def trouver_case_vide():
            for i in range(9):
                for j in range(9):
                    if self.grid[i][j] == 0:
                        return (i, j)  # rangée, colonne
            return None
        
        vide = trouver_case_vide()
        if not vide:
            return True  # Résolu
        
        else:
            row, col = vide
            
            for val in range(1, 10):
                if self._is_valid_before_place(row, col, val):
                    self.grid[row][col] = val
                    
                    if self.resoudre():      # Récursion
                        return True
                    
                    self.grid[row][col] = 0  # backtrack
        return False
    
    def play_cli(self) -> None:
        """
        Jouer au sudoku dans une interface de ligne de commande (CLI).

        Returns
        -------
        None

        """
        self.generate_new_grid()
        while True:
            print(self)
            action = input("Action [1: placer une valeur] ou [2: verifier si la grille est valide] ou [3: afficher solution] ou [4: quitter]: ")
            try:
                if action == '1':
                    val = int(input("value: "))
                    col = int(input("col: "))
                    row = int(input("row: "))
                    
                    if self.place(row, col, val):
                        print(f"[{val}] a été placée à ({col}, {row}).\n")
                    else:
                        print(f"Ne peut pas placer {val} à ({col}, {row}).\nRéessayer avec une nouvelle valeur.\n")
        
                elif action == '2':
                    if self.is_solution():
                        print("Bravo ! Vous avez resolu le Sudoku !")
                        break
                    else:
                        print("ERREUR: Le sudoku a une erreur") # A preciser plus tard
                
                elif action == '3':
                    self.resoudre()
                
                elif action == '4':
                    break
                
                else:
                    print("ERREUR: Action invalide.")
            
            except KeyboardInterrupt:
                print("ERREUR: Action annulée \n")
                continue
                    
    def __str__(self) -> str:
        __print_str = ""
        for i in range(9):
            if i % 3 == 0 and i != 0:
                __print_str += f"{self.__horizontal_sep} " * 11 + '\n' # Separateur horizontal pour les blocks 3x3
        
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    __print_str += f"{self.__vertical_sep} " # Separateur vertical pour les blocks 3x3
        
                if self.grid[i][j] == 0:
                    __print_str += f"{self.__caractere_vide} " # Representer les cellules vide avec un point.
                else:
                # Imprimer une valeur non-nulle
                    if self.grid[i][j] == self.starting_grid[i][j]:
                        __print_str += np.bold(f"{self.grid[i][j]} ")
                    else:
                        __print_str += f"{self.grid[i][j]} "
                    
                    
            __print_str += '\n' # Nouvelle ligne après chaque rangée
        
        return __print_str

if __name__ == "__main__":
    sudoku = Sudoku()
    sudoku.play_cli()
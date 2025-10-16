# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 10:28:10 2025

@author: m.tanguy
"""

import nice_print as np
import pandas as pd
from dosuko_api import EMPTY_BOARD, get_new_dosuko_board

class Sudoku:
    def __init__(self):
        self.grid, self.starting_grid  = pd.DataFrame(EMPTY_BOARD), pd.DataFrame(EMPTY_BOARD)
        self.difficulty = None
        
        self.__caractere_vide = '.'
        self.__vertical_sep = '|'
        self.__horizontal_sep = '—'
        
    def _empty(self):
        self.grid = pd.DataFrame(EMPTY_BOARD)
    
    def generate_new_grid(self):
        dosuko_response = get_new_dosuko_board()
        
        self.starting_grid, self.difficulty = pd.DataFrame(dosuko_response['grid']), dosuko_response['difficulty']
        self.grid = self.starting_grid
    
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
        for i in range(debut[0], fin[0]):
            for j in range(debut[1], fin[1]):
                if val ==self. grid[i][j]:
                    return False
        
        # la valeur est validée !
        return True

    def is_solution(self):
        # Si pas de cases vides
        if all(val != 0 for val in row for row in self.grid):
            return False
        
        if all(set(row) == set(range(1, 9)) for row in self.grid):
            return False
        
        if all()
    
    def __str__(self):
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
    sudoku.generate_new_grid()
    while True:
        print(sudoku)
        val = int(input("value: "))
        col = int(input("col: "))
        row = int(input("row: "))
        
        if sudoku.place(row, col, val):
            print(f"[{val}] a été placée à ({col}, {row}).\n")
        else:
            print(f"Ne peut pas placer {val} à ({col}, {row}).\nRéessayer avec une nouvelle valeur.\n")
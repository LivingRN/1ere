# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 10:28:10 2025

@author: m.tanguy
"""

from nice_print import *
from dosuko_api import EMPTY_BOARD, get_new_dosuko_board


class Sudoku:
    def __init__(self):
        # Initialize grid and starting_grid as deep copies of EMPTY_BOARD (list of lists)
        # use deep copies to avoid shared references between grid and starting_grid
        self.grid = [row[:] for row in EMPTY_BOARD]
        self.starting_grid = [row[:] for row in EMPTY_BOARD]
        self.solution = None
        self.difficulty = None
        
        self.__caractere_vide = '.'
        self.__vertical_sep = '|'
        self.__horizontal_sep = '—'
    
    def _empty(self):
        self.grid = [row[:] for row in EMPTY_BOARD]
    
    def generate_new_grid(self):
        dosuko_response = get_new_dosuko_board()
        board = dosuko_response['grid']
        self.difficulty = dosuko_response['difficulty']
        # make copies so subsequent modifications don't mutate the original object
        self.starting_grid = [row[:] for row in board]
        self.grid = [row[:] for row in board]

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
        if not (1 <= val <= 9):
            return False
        
        # Si la case est déjà utilisée
        if self.grid[row][col] != 0:
            return False
        
        # Vérifier si la valeur est présente dans la rangée
        if val in self.grid[row]:
            return False
        
        # Vérifier si la valeur est dans la colonne
        if val in [self.grid[i][col] for i in range(9)]:
            return False
        
        # Vérifier le carré 3x3
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if val == self.grid[i][j]:
                    return False
        
        return True
    
    def _is_valid_after_place(self, row: int, col: int, val: int) -> bool:
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
        # Vérifier dans la rangée
        if self.grid[row].count(val) > 1:
            return False
        
        # Vérifier dans la colonne
        col_vals = [self.grid[i][col] for i in range(9)]
        if col_vals.count(val) > 1:
            return False
        
        # Vérifier dans le carré 3x3
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        count = 0
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if val == self.grid[i][j]:
                    count += 1
        if count > 1:
            return False
        
        return True
    
    def place(self, row: int, col: int, val: int, validate: bool = False) -> bool:
        """Placer une valeur dans la grille si elle est valide.

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
            Renvoyer True si la valeur a été placée, False dans le cas contraire.
        """
        if validate and self._is_valid_before_place(row, col, val):
            self.grid[row][col] = val
            return True
        return False
    
    def is_solution(self):
        """Verify if the current grid is a valid solution."""
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    return False
                if not self._is_valid_after_place(i, j, self.grid[i][j]):
                    return False
        return True
    
    def find_solution(self) -> bool:
        """Resoudre le Sudoku en utilisant la méthode de backtracking."""
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    for val in range(1, 10):
                        if self._is_valid_before_place(i, j, val):
                            self.grid[i][j] = val
                            if self.find_solution():
                                return True
                            self.grid[i][j] = 0
                    return False
        return True
    
    def __str__(self):
        __print_str = ""
        for i in range(9):
            if i % 3 == 0 and i != 0:
                __print_str += f"{self.__horizontal_sep} " * 11 + '\n'  # Separateur horizontal pour les blocks 3x3
            
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    __print_str += f"{self.__vertical_sep} "  # Separateur vertical pour les blocks 3x3
                
                if self.grid[i][j] == 0:
                    __print_str += f"{self.__caractere_vide} "  # Representer les cellules vide avec un point.
                else:
                    # Imprimer une valeur non-nulle
                    if self.grid[i][j] == self.starting_grid[i][j]:
                        __print_str += bold(f"{self.grid[i][j]} ")
                    else:
                        if not self._is_valid_after_place(i, j, self.grid[i][j]):
                            __print_str += red(f"{self.grid[i][j]} ")
                        else:
                            __print_str += grey(f"{self.grid[i][j]} ")
            
            __print_str += '\n'  # Nouvelle ligne après chaque rangée
        return __print_str


if __name__ == "__main__":
    sudoku = Sudoku()
    sudoku.generate_new_grid()
    while True:
        print(sudoku)
        val = input("value: ")
        
        if val == 'solution':
            sudoku.find_solution()
            print("Solution trouvée !\n")
            print(sudoku)
            break
        
        val = int(val)
        col = int(input("col: "))
        row = int(input("row: "))
        
        if sudoku.place(row, col, val, validate=True):
            print(f"[{val}] a été placée à ({col}, {row}).\n")
            if sudoku.is_solution():
                print("Félicitations ! Vous avez résolu le Sudoku.\n")
                print(sudoku)
                break
        else:
            print(f"Ne peut pas placer {val} à ({col}, {row}).\nRéessayer avec une nouvelle valeur.\n")
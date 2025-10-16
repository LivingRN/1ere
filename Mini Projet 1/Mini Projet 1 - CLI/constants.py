# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 11:37:19 2025

@author: m.tanguy
"""

DOSUKO_API = "https://sudoku-api.vercel.app/api/dosuku"
    
DOSUKO_API_NEW_BOARD_QUERY = DOSUKO_API + "?query={newboard(limit:1){grids{value,solution,difficulty},results,message}}"

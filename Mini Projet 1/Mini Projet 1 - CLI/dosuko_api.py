# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 11:38:18 2025

@author: m.tanguy
"""

import requests
from constants import DOSUKO_API_NEW_BOARD_QUERY


EMPTY_BOARD = [[0 for _ in range(9)] for _ in range(9)]

# A safe fallback board (partial puzzle) used when the API request fails.
FALLBACK_BOARD = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

FALLBACK_DIFFICULTY = "unknown"

def get_new_dosuko_board() -> dict:
    try:
        response = requests.get(DOSUKO_API_NEW_BOARD_QUERY, timeout=5)
        # validate the response
        if response.status_code != 200:
            # non-OK response -> fallback
            return {"grid": FALLBACK_BOARD, "difficulty": FALLBACK_DIFFICULTY}

        body = response.json()

        # navigate the expected structure defensively
        newboard = body.get("newboard") if isinstance(body, dict) else None
        if not newboard:
            return {"grid": FALLBACK_BOARD, "difficulty": FALLBACK_DIFFICULTY}

        grids = newboard.get("grids")
        if not grids or not isinstance(grids, list) or len(grids) == 0:
            return {"grid": FALLBACK_BOARD, "difficulty": FALLBACK_DIFFICULTY}

        first = grids[0]
        value = first.get("value") if isinstance(first, dict) else None
        difficulty = first.get("difficultly") if isinstance(first, dict) else FALLBACK_DIFFICULTY

        if not value:
            return {"grid": FALLBACK_BOARD, "difficulty": difficulty or FALLBACK_DIFFICULTY}

        return {"grid": value, "difficulty": difficulty or FALLBACK_DIFFICULTY}

    except Exception:
        # Any exception (network, timeout, JSON decode, attribute error) -> fallback
        return {"grid": FALLBACK_BOARD, "difficulty": FALLBACK_DIFFICULTY}
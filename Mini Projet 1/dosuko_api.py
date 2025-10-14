# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 11:38:18 2025

@author: m.tanguy
"""

import requests
from constants import DOSUKO_API_NEW_BOARD_QUERY


EMPTY_BOARD = [[0 for _ in range(9)] for _ in range(9)]

def get_new_dosuko_board() -> dict:
    response = requests.get(DOSUKO_API_NEW_BOARD_QUERY)
    # print(f"Status Code: {response.status_code}")
    # print(f"Content Type: {response.headers['content-type']}")
    # print(f"Body: {response.text[:100]}") # Print first 100 chars

    body = dict(response.json())

    return {
        "grid": body.get("newboard").get("grids")[0].get("value"),
        "difficulty": body.get("newboard").get("grids")[0].get("difficultly")
    }
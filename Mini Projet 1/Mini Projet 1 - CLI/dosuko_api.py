# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 11:38:18 2025

@author: m.tanguy
"""

import requests
from constants import DOSUKO_API_NEW_BOARD_QUERY

EMPTY_BOARD = [[0 for _ in range(9)] for _ in range(9)]

error_response = {
    "grid": EMPTY_BOARD,
    "difficulty": "unknown"
}

def get_new_dosuko_board() -> dict:
    """
    Retrieve a new Sudoku board from the Dosuko API.

    Returns:
        dict: A dictionary containing the Sudoku grid and its difficulty level.
    """
    global error_response
    
    response = requests.get(DOSUKO_API_NEW_BOARD_QUERY)
    # print(f"Status Code: {response.status_code}")
    # print(f"Content Type: {response.headers['content-type']}")
    # print(f"Body: {response.text[:100]}") # Print first 100 chars
    
    if response.status_code != 200:
        print(Exception(f"Failed to retrieve board: {response.status_code}"))
        return error_response
    
    if "application/json" not in response.headers.get("content-type", ""):
        print(Exception("Invalid content type received from API"))
        return error_response
    
    if not response.text:
        print(Exception("Empty response body received from API"))
        return error_response
    
    if "newboard" not in response.text:
        print(Exception("Expected 'newboard' key not found in response"))
        return error_response
    
    if "grids" not in response.text:
        print(Exception("Expected 'grids' key not found in response"))
        return error_response
    
    if "value" not in response.text:
        print(Exception("Expected 'value' key not found in response"))
        return error_response
    
    body = dict(response.json())

    return {
        "grid": body.get("newboard").get("grids")[0].get("value"),
        "difficulty": body.get("newboard").get("grids")[0].get("difficultly")
    }
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 11:40:24 2025

@author: m.tanguy
"""

def bold(s: str):
    return '\033[1m' + s + '\033[0m'

def italic(s: str):
    return '\x1B[3m' + s + '\x1B[0m'
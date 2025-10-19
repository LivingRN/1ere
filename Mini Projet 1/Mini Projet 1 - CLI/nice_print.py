# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 11:40:24 2025

@author: m.tanguy
"""

import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

def bold(s: str):
    return Style.BRIGHT + s + Style.RESET_ALL

def italic(s: str):
    return '\x1B[3m' + s + Style.RESET_ALL

def grey(s: str):
    return Fore.LIGHTBLACK_EX + s + Style.RESET_ALL

def green(s: str):
    return Fore.GREEN + s + Style.RESET_ALL

def red(s: str):
    return Fore.RED + s + Style.RESET_ALL


if __name__ == '__main__':
    # Demo
    print(bold('This is bold text'))
    print(italic('This is italic (may not render on Windows pwsh)'))
    print(grey('This is grey text'))
    print(green('This is green text'))
    print(red('This is red text'))
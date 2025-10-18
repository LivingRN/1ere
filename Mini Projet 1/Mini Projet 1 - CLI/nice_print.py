# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 11:40:24 2025

@author: m.tanguy
"""

import colorama
from colorama import Fore, Style

# enable colorama so ANSI sequences (and Fore/Style) work on Windows
colorama.init(autoreset=True)

def bold(s: str):
    return Style.BRIGHT + s + Style.RESET_ALL

def italic(s: str):
    # italics are not supported in many Windows terminals; keep the ANSI code as fallback
    return '\x1B[3m' + s + Style.RESET_ALL

def grey(s: str):
    return Fore.LIGHTBLACK_EX + s + Style.RESET_ALL

def green(s: str):
    return Fore.GREEN + s + Style.RESET_ALL

def red(s: str):
    return Fore.RED + s + Style.RESET_ALL


if __name__ == '__main__':
    # Quick interactive demo so running this module prints sample outputs.
    print(bold('This is bold text'))
    # Italics may not be supported in Windows PowerShell; this is a best-effort.
    print(italic('This is italic (may not render on Windows terminals)'))
    print(grey('This is grey text'))
    print(green('This is green text'))
    print(red('This is red text'))
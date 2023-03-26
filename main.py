from colored import fg
import os
from Zapsurveys import ZapSurveys
from filemanager import OpenFileEditor
import ctypes
import time

ctypes.windll.kernel32.SetConsoleTitleW("Zappy - Proxyless Checker")


yellow = fg(3)
green = fg(2)
reset = fg(7)
cyan = fg(6)
red = fg(1)
dark_yellow = fg(166)
dark_cyan = fg(4)

width = os.get_terminal_size().columns

def logo():
    print(cyan, rf"""
                                   ________                                         
                                  /        |                                        
                                  $$$$$$$$/   ______    ______    ______   __    __ 
                                      /$$/   /      \  /      \  /      \ /  |  /  |
                                     /$$/    $$$$$$  |/$$$$$$  |/$$$$$$  |$$ |  $$ |
                                    /$$/     /    $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |
                                   /$$/____ /$$$$$$$ |$$ |__$$ |$$ |__$$ |$$ \__$$ |
                                  /$$      |$$    $$ |$$    $$/ $$    $$/ $$    $$ |
                                  $$$$$$$$/  $$$$$$$/ $$$$$$$/  $$$$$$$/   $$$$$$$ |
                                                      $$ |      $$ |      /  \__$$ |
                                                      $$ |      $$ |      $$    $$/ 
                                                      $$/       $$/        $$$$$$/  



                                                   {cyan}Made With <3 By Tubouu{cyan}
"""+ reset)




logo()
def zappy():
    print(f'''
    {cyan}[1] - ZapSurveys
    [2] - Combo Editor
    [3] - Exit{reset}
    
    
    ''')
    option = input(f"{cyan}[+]{reset} ")

    if option == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        logo()
        threads = input(f'{cyan}[+] How many threads?{reset} ')
        ZapSurveys().start(int(threads))
    elif option == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        logo()
        print(f'''
        
        
        
                                                        {cyan}Combo Editor{reset}        
        ''')
        OpenFileEditor()
    elif option == '3':
        exit()
    else:
        print(f"{cyan}Invalid Option{reset}")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        logo()
        zappy()


zappy()
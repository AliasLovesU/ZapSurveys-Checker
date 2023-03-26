from colored import fg
from Variables import Zappy
import os

yellow = fg(3)
green = fg(2)
reset = fg(7)
cyan = fg(6)
red = fg(1)
dark_yellow = fg(166)
dark_cyan = fg(4)
rosy_brown = fg(138)

def log(type:str,account:str,title:str=None):
        match type:
            case "custom":
                print(f"    [{reset}{yellow}CUSTOM{yellow}{reset}] {account} | {title}")
            case "good":
                print(f"    [{green}HIT{green}]{reset} {account} | {title}")
            case _:
                print(f"    {red}{account}{reset}")





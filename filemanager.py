import os
import time
import tkinter as tk
from tkinter import filedialog

from colored import fg

yellow = fg(3)
green = fg(2)
reset = fg(7)
cyan = fg(6)
red = fg(1)
dark_yellow = fg(166)
dark_cyan = fg(4)
rosy_brown = fg(138)



def OpenFile():
    root = tk.Tk()
    root.attributes("-topmost", True)
    file_path = filedialog.askopenfilename()
    root.withdraw()
    print(f'{cyan}[+] Imported combos from:{reset} {green}{file_path}{reset}')
    time.sleep(2)
    combos = ""
    
    with open(file_path, errors="ignore") as file:
        combos = file.read().splitlines()

    return combos


def OpenFileEditor():
    root = tk.Tk()
    root.attributes("-topmost", True)
    file_path = filedialog.askopenfilename()
    root.withdraw
    combos = []
    
    with open(file_path, errors="ignore") as file:
        for combo in file:
            combo = combo.strip()
            if ":" in combo:
                combo = combo.replace(":", "|")
            elif "|" in combo:
                combo = combo.replace("|", ":")
            combos.append(combo)
    
    
    dir_path = os.path.dirname(file_path)
    output_path = os.path.join(dir_path, "new_combos.txt")
    with open(output_path, "w") as output_file:
        output_file.write("\n".join(combos))

    print(f"{green}[+] Edited {len(combos)} combos to {output_path}{reset}")
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(1)
    exit()



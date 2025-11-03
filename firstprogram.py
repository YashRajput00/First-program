import time 
import sys

def print_lyrics ():
    lyrics = [
       "kyoon pyaar main too nadaan bane",
        "ik pagal ka armaan bane",
        "Ab laut ke jaana mushkil hai",
        "maine chhod diya hai jag sara",
        "Itna na mujhse tu pyaar badha",
        "ki main ik badal aawara",
        "janam janam se hoon saath tere",
        "hai naam mera jal ki dhara",
    ]
    delays = [0.5, 0.9, 0.8, 0.9, 0.8, 0.7, 0.9, 1.0]

    print("Itna Na Tu Mujhse Pyaar Badha\n")
    time.sleep(2.0)
    
    for i, line in enumerate(lyrics):
        for char in line: 
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        print()
        time.sleep(delays[i]) if i < len(delays) else 0.5
print_lyrics()
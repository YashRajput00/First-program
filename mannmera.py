import time 
import sys

def print_lyrics ():
    lyrics = [
       "Rag-rag wo samaya mere",
       "Dil par woh chaaya mere",
       "Mujhmein wo aise jaise jaan",
       "Gire barsaat mai paani jaise",
       "Koi kahaani jaise",
       "Dil se ho dil tak jo bayaan",
       "Aashiq dil tera purana hai ye",
       "Deewana-deewana samjhe na, ho",
    ]
    delays = [0.5, 0.9, 0.8, 0.9, 0.8, 0.7, 0.9, 1.0]

    print("Mann mera\n")
    time.sleep(2.0)
    
    for i, line in enumerate(lyrics):
        for char in line: 
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        print()
        time.sleep(delays[i]) if i < len(delays) else 0.5
print_lyrics()
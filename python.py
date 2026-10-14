import os
import sys
import time

# Terminal colors
RESET = "\033[0m"
BOLD = "\033[1m"
PINK = "\033[95m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
GOLD = "\033[38;5;220m"
WHITE = "\033[97m"

SONG_TITLE = "CHOGADA TARA"

# Format: (lyric, color, typing speed, pause after line)
LYRICS = [
    ("Chhup Chhup Ke Tumhe Dekha Main Karoon", PINK, 0.09, 0.35),
    ("Saari Saari Raat, Saari Saari Raat..", CYAN, 0.09, 0.45),
    ("Chhup Chhup Ke Mujhe Dekha Tu Kare", YELLOW, 0.09, 0.35),
    ("Saari Saari Raat, Saari Saari Raat..", GREEN, 0.09, 0.45),
    ("Mil Jaaye Mujhko Agar Saath Tera", PINK, 0.09, 0.35),
    ("To Bhulun Main Saara Jahaan..", CYAN, 0.09, 1.4),
    ("Chogada Taara, Chabeela Taara", YELLOW, 0.09, 0.35),
    ("Rangoola Taara", GREEN, 0.09, 0.35),
    ("Rangbheru Juye Taari Vaat Re.. Haa", PINK, 0.09, 0.35),
    ("Chogada Taara,", CYAN, 0.09, 0.35),
    ("Ore Chabeela Taara", YELLOW, 0.09, 0.35),
    ("Ore Rangeela Taara", GREEN, 0.09, 0.35),
    ("Rangbheru Juve Taari Vaat Re.. Haa (2x)", PINK, 0.09, 0.8),
]


def type_line(text, color, speed):
    """Print one lyric line with a typewriter effect."""
    sys.stdout.write(color + "♫ " + RESET)
    sys.stdout.flush()

    for character in text:
        sys.stdout.write(color + character + RESET)
        sys.stdout.flush()
        time.sleep(speed)

    print()


def main():
    os.system("cls" if os.name == "nt" else "clear")

    width = 62
    print(GOLD + "═" * width + RESET)
    print(GOLD + BOLD + SONG_TITLE.center(width) + RESET)
    print(GOLD + "═" * width + RESET)
    print()

    for lyric, color, typing_speed, pause_after in LYRICS:
        type_line(lyric, color, typing_speed)
        time.sleep(pause_after)

    print()
    print(GOLD + "♪ Thanks for listening! ♪" + RESET)


if __name__ == "__main__":
    main()
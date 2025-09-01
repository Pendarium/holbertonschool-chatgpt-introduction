#!/usr/bin/python3
import random
import os
from colorama import init, Fore, Style

# Initialiser colorama (reset automatique, mais on le force aussi à la main)
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.total_mines = mines
        self.mines = set()
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.first_move_done = False

    def place_mines(self, safe_x, safe_y):
        while len(self.mines) < self.total_mines:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if (x, y) != (safe_x, safe_y) and (x, y) not in self.mines:
                self.mines.add((x, y))

    def print_board(self, reveal=False):
        clear_screen()
        print('   ' + ' '.join(f"{i:2}" for i in range(self.width)))
        for y in range(self.height):
            print(f"{y:2} ", end='')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (x, y) in self.mines:
                        print(" *", end='')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(f" {count}" if count > 0 else "  ", end='')
                else:
                    print(" .", end='')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (nx, ny) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if (x, y) in self.mines:
            return False
        if self.revealed[y][x]:
            return True

        self.revealed[y][x] = True

        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        self.reveal(nx, ny)
        return True

    def has_won(self):
        for y in range(self.height):
            for x in range(self.width):
                if not self.revealed[y][x] and (x, y) not in self.mines:
                    return False
        return True

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input(Fore.BLUE + "Entrez la coordonnée X : " + Style.RESET_ALL))
                y = int(input(Fore.BLUE + "Entrez la coordonnée Y : " + Style.RESET_ALL))

                if not (0 <= x < self.width and 0 <= y < self.height):
                    print(Fore.RED + "Coordonnées hors limites. Réessayez." + Style.RESET_ALL)
                    input(Fore.RED + "Appuyez sur Entrée pour continuer..." + Style.RESET_ALL)
                    continue

                if not self.first_move_done:
                    self.place_mines(x, y)
                    self.first_move_done = True

                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print(Fore.RED + "💥 BOOM ! Vous avez touché une mine. Game Over." + Style.RESET_ALL)
                    break

                if self.has_won():
                    self.print_board(reveal=True)
                    print(Fore.GREEN + "🎉 Félicitations ! Vous avez gagné !" + Style.RESET_ALL)
                    break

            except ValueError:
                print(Fore.YELLOW + "❌ Entrée invalide. Veuillez entrer des nombres." + Style.RESET_ALL)
                input(Fore.GREEN + "Appuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()

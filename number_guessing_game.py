import random
import time
import os
from colorama import Fore, Style, init

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome_message():
    print(Fore.CYAN + "Bienvenido al juego de Adivina el Número!")
    print("Estoy pensando en un número entre 1 y 100.")

def choose_difficulty():
    print("Selecciona el nivel de dificultad:")
    print("1. Fácil (10 intentos)")
    print("2. Medio (5 intentos)")
    print("3. Difícil (3 intentos)")

    while True:
        try:
            choice = int(input("Elige una opción (del 1 al 3): "))
            if choice == 1:
                return 10
            elif choice == 2:
                return 5
            elif choice == 3:
                return 3
            else:
                print(Fore.RED + "Por favor, selecciona un número válido (del 1 al 3).")
        except ValueError:
            print(Fore.RED + "Entrada inválida. Por favor, ingresa un número.")

def get_hint(target_number, guess):
    if target_number % 2 == 0:
        hint = "El número es par."
    else:
        hint = "El número es impar."

    if abs(target_number - guess) <= 10:
        hint += " Además, estás cerca del número."

    return hint

def play_game():
    welcome_message()
    attempts = choose_difficulty()
    target_number = random.randint(1, 100)
    print(f"Tienes {attempts} intentos para adivinar el número.\n")

    start_time = time.time()

    for attempt in range(1, attempts + 1):
        print(Fore.YELLOW + f"Intentos restantes: {attempts - attempt + 1}\n")
        while True:
            try:
                guess = int(input(f"Intento {attempt}/{attempts}: Ingresa tu número: "))
                break
            except ValueError:
                print(Fore.RED + "Entrada inválida. Por favor, ingresa un número.")

        if guess == target_number:
            elapsed_time = time.time() - start_time
            print(Fore.GREEN + f"¡Felicidades! Adivinaste el número {target_number} en {attempt} intentos.")
            print(Fore.CYAN + f"Tiempo total: {elapsed_time:.2f} segundos.\n")
            return
        elif guess < target_number:
            print(Fore.BLUE + "El número es mayor que tu conjetura.\n")
        else:
            print(Fore.BLUE + "El número es menor que tu conjetura.\n")

        if attempt < attempts:
            while True:
                hint_request = input("¿Quieres una pista? (s/n o Enter para continuar): ").strip().lower()
                if hint_request in ('s', 'n', ''):
                    break
                print(Fore.RED + "Entrada inválida. Ingresa 's' para sí, 'n' para no o presiona Enter para continuar.")
            
            if hint_request == 's':
                print(Fore.MAGENTA + get_hint(target_number, guess) + "\n")

    print(Fore.RED + f"Lo siento, te quedaste sin intentos. El número era {target_number}.\n")

def main():
    while True:
        clear_screen()
        play_game()
        play_again = input("¿Quieres jugar otra vez? (s/n): ").strip().lower()
        if play_again != 's':
            print(Fore.CYAN + "Gracias por jugar. ¡Hasta luego!\n")
            break

if __name__ == "__main__":
    main()

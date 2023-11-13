# Zmienne
plansza = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
tura = True
wygrana = False
tury = 0
print(f"Aktualny wygląd planszy {plansza}")
while wygrana == False:
    odpowiedz = int(input("Podaj numer pola: "))
    if 0 > odpowiedz > 9:
        print("Podałeś zły numer pola, spróbuj jeszcze raz")
        continue
    
    if tura:
        plansza[odpowiedz - 1] = "X"
    else:
        plansza[odpowiedz - 1] = "O"
    
    tura = not tura
    print(f"Aktualny wygląd planszy {plansza}")
    tury += 1

    # Poziome
    if plansza[0] == plansza[1] and plansza[0] == plansza[2]:
        print(f"{plansza[0]} Wygrał!")
        wygrana = True
    elif plansza[3] == plansza[4] and plansza[3] == plansza[5]:
        print(f"{plansza[0]} Wygrał!")
        wygrana = True
    elif plansza[6] == plansza[7] and plansza[6] == plansza[8]:
        print(f"{plansza[0]} Wygrał!")
        wygrana = True

    # Pionowe
    elif plansza[0] == plansza[3] and plansza[0] == plansza[6]:
        print(f"{plansza[0]} Wygrał!")
        wygrana = True
    elif plansza[1] == plansza[4] and plansza[1] == plansza[7]:
        print(f"{plansza[0]} Wygrał!")
        wygrana = True
    elif plansza[2] == plansza[5] and plansza[2] == plansza[8]:
        print(f"{plansza[0]} Wygrał!")
        wygrana = True

    # Na Ukos
    elif plansza[0] == plansza[4] and plansza[0] == plansza[8]:
        print(f"{plansza[0]} Wygrał!")
        wygrana = True
    elif plansza[2] == plansza[4] and plansza[2] == plansza[6]:
        print(f"{plansza[0]} Wygrał!")
        wygrana = True

    # Remis 
    if tury == 9 and wygrana == False:
        print("Remis!")
        break

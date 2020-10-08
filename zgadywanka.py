from random import randint


def start():
    los = randint(1, 10)
    odp = None
    ilosc = 0
    ans = None
    while odp != los:
        ilosc += 1
        try:
            odp = int(input("Podaj liczbe: "))
        except ValueError:
            continue
        if odp > los:
            print("Podana liczba jest wieksza od wylosowanej")
        elif odp < los:
            print("Podana liczba jest mniejsza od wylosowanej")
        else:
            print("\nWygrales w gre brawo!\n\nZgadles za", ilosc, "razem\n\n")
            print("Chcesz zagrac jeszcze raz?\n1 - TAK\n2 - NIE\n")
            while ans != 1:
                try:
                    ans = int(input("-> "))
                except ValueError:
                    continue
                if ans == 1:
                    start()
                elif ans == 2:
                    input("Nacisnij dowolny przycisk aby zakonczyc")
                    return 0


start()

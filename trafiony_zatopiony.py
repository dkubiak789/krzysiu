from random import randrange

def losuj_liczby(ilosc_liczb, min, max):
    liczby = []
    while len(liczby) < ilosc_liczb:
        liczba = randrange(min, max)
        if (liczba >= min) and (liczba <= max) and (liczba > 0) and (liczba not in liczby):
            liczby.append(liczba)
    return liczby

def znajdz_min(liczby):
    min = 0
    for liczba in liczby:
        if liczba < min or min == 0:
            min = liczba
    return min

def znajdz_max(liczby):
    max = 0
    for liczba in liczby:
        if liczba > max or max == 0:
            max = liczba
    return max

def znajdz(liczby_gracza, wylosowane_liczby):
    trafione = []
    for liczba_gracza in liczby_gracza:
        if liczba_gracza in wylosowane_liczby:
            trafione.append(liczba_gracza)
    return trafione

if __name__ == '__main__':
    liczby_gracza_str = input('Twoje liczby: ').split(',')
    liczby_gracza = [int(liczba) for liczba in liczby_gracza_str]
    min = znajdz_min(liczby_gracza)
    max = znajdz_max(liczby_gracza)
    wylosowane_liczby = losuj_liczby(len(liczby_gracza), min, max)
    trafione = znajdz(liczby_gracza, wylosowane_liczby)

    print('Liczby gracza: ', liczby_gracza)
    print('Wylosowane liczby: ', wylosowane_liczby)
    print('Trafione: ', trafione)

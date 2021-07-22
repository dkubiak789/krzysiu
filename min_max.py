from random import randrange

def losuj_liczby(ilosc_liczb, min, max):
    liczby = []
    while len(liczby) < ilosc_liczb:
        liczba = randrange(min, max)
        if (liczba >= min) and (liczba <= max) and (liczba != 0):
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

if __name__ == '__main__':
    ilosc_liczb = int(input('Ile liczb? '))
    min = int(input('Minimum: '))
    max = int(input('Maksimum: '))

    liczby = losuj_liczby(ilosc_liczb, min, max)
    print('Wylosowane liczby: ', liczby)

    liczba_min = znajdz_min(liczby)
    print('Najmniejsza liczba: ', liczba_min)

    liczba_max = znajdz_max(liczby)
    print('Największa liczba: ', liczba_max)

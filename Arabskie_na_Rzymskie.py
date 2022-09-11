class LiczbaRzymska:
    """

    """
    def __init__(self, liczba_arabska):
        ...


def zamien_arabskie_na_rzymskie(liczba_arabska):
    jednosci = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
    dziesiatki = [x.replace('X', 'C').replace('V', 'L').replace('I', 'X') for x in jednosci]
    setki = [x.replace('X', 'M').replace('V', 'D').replace('I', 'C') for x in jednosci]
    '''
    V - 5
    X - 10
    L - 50
    C - 100
    D - 500
    M - 1000
    '''
    arab = str(liczba_arabska)
    arab = f'{arab:0>4}'
    print(int(arab[0]) * 'M' + setki[int(arab[1])] + dziesiatki[int(arab[2])] + jednosci[int(arab[3])])

zamien_arabskie_na_rzymskie(45)
'''
"3674"
"0005"
3 * 'M' + DCLXXIV = MMMDCLXXIV
'''
'''
b = LiczbaRzymska('2395')
print(a) # CL (150)
print(int(a)) # 150, metoda __int__(self)
print(a == b, a < b, a > b) # False, True, False, __eq__, __le__, __gt__
print(a + b) # MMDXLV (2545)
print(a - b, a * b)
print('V' in a, 'X' in 'a', 'L' in a), # False, False, True
a += b # __iadd__
print(a, b) # MMDXLV(2545) MMCCCCXV (2395)
print(len(a)) # 6, metoda __len__, długość napisu MMDXLV
c = LiczbaRzymska(3)
d = LiczbaRzymska(8)
print(c * d) # XXIV (24), metoda __mul__(self, other)
print(d - c) # V (5), metoda __sub__(self, other)
print(c - d) # ValueError: Wynik jest liczbą mniejszą od zera
(edited)
'''
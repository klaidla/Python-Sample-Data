'''Zadanie 1 na pętlę while oraz instrukcję if
Pamiętasz grę: zgadnij liczbę z zakresu 1 – 100? Zgadujący podaje
odpowiedź, a Ty mówisz „zgadłeś”, „za dużo” albo „za mało”.
Zaimplementuj taką grę. Sam ustal jaka powinna być maksymalna ilość prób do zgadnięcia liczby.'''


moja_liczba = 77

counter = 0

while True:

    liczba_uzytkownika =(int(input('Zgadnij liczbę od 1 do 100')))
    print(liczba_uzytkownika)

    if liczba_uzytkownika > moja_liczba:
            print('za dużo')

    if liczba_uzytkownika < moja_liczba:
            print('za mało')

    if liczba_uzytkownika == moja_liczba:
        print('zgadles')
        break

    counter += 1

    if counter == 5:
        print('wykorzystałeś limit podejść')
        break


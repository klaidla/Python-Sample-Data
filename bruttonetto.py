''' wykorzystaj petle nieskonczona while do wyswietlania menu na ekranie.
petla konczy dzialanie po wybraniu opcji  nr 1 (zastosuj break).
po wybraniu pierwszej opcji (podanie liczby z klawiatury), program prosi o podanie kwoty brutto, a potem oblicza
kwote netto (netto = 80% brutto).'''

while True:

    choice =(int(input('------Menu------\n'
          '1) Brutto -> netto\n'
          '2) Netto -> Brutto\n'
          '3) Wyjście\n'
                
        'Wybór: \n'
    )))
    print(choice)

    if choice == 1:
        amount_brutto1 = (int(input('Podaj kwotę Brutto: ')))
        amount_netto1 = amount_brutto1 * 0.8
        print('Kwota netto z wpisanej kwoty to', amount_netto1)

    elif choice == 2:
        amount_netto2 = (int(input('Podaj kwotę Netto: ')))
        amount_brutto2 = 10 / 8 * amount_netto2
        print('Kwota Brutto z wpisanej kwoty to', amount_brutto2)

    elif choice == 3:
        print('Wyszedłeś z MENU')
        break

    else:
        print('Polecenie nierozpoznane')








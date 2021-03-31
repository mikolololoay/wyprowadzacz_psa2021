def wyprowadz_psa(imie_psa, wiek_psa, pogoda)
    czas_spaceru = 100 / wiek_psa
    if czas_spaceru < 15:
        czas_spaceru = 15
    if pogoda == 'deszcz' or pogoda == 'burza':
        czas_spaceru -= 10
    print(f'{imie_psa}, do nogi!')
    return czas_spaceru
    
imie_psa = 'Azor'
wiek_psa = 9
pogoda = 'słonecznie'
wyprowadz_psa(imie_psa, wiek_psa, pogoda)
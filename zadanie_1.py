'''
Stwórz program, który na podstawie

    tabeli inflacji wartości
    oprocentowania kredytu,
    kwoty początkowej kredytu
    stałej wartości raty

wyliczy wartość zadłużenia w każdym miesiącu przez 2 nadchodzące lata.

Niech program wydrukuje dla każdego miesiąca następującą linię:
Twoja pozostała kwota kredytu to X, to Y mniej niż w poprzednim miesiącu.

Napisz program tak, by wysokość początkowego kredytu, oprocentowanie kredytu (ponad inflację) i kwota raty były pobierane ze standardowego wejścia (terminal).

Przykładowe wartości kredytu i formułę do jego wyliczenia znajdziesz w załączniku powyżej. Skopiuj z niego wartości inflacji dla każdego miesiąca.

Wyślij link do swojego repozytorium (nie spakowany kod). Repozytorium powinno zawierać więcej, niż jeden commit.

'''
'''
1. dane wejściowe: tabela w excelu z wartościami inflacji (pobrać dane za pomocą context managera albo przypisać do zmiennych - co potrafię zrobić?),
oprocentowanie kredytu - standardowe wejście z terminalu
kwota początkowa kredytu - standardowe wejście z terminalu
stała wartość raty - standardowe wejście z tarminalu

2. co musze zrobić? wyliczyć wrtości kredytu 
co mam do tego? formuła z excela

3. wyjście
wypisanie po każdym miesiącu zdania:
Twoja pozostała kwota kredytu to X, to Y mniej niż w poprzednim miesiącu.

4. Zrobić testy manualne (a w przyszłości napisać testy jednostkowe do tych funkcjonalności)!!! pamiętać od edge casach i poprawnie je obsługiwać

5. wysłać to do zdalnego repozytorium


'''
inflacja_1 = 1.59282448436825
inflacja_2 = -0.453509101198007
inflacja_3 = 2.32467171712441
inflacja_4 = 1.26125440724877
inflacja_5 = 1.78252628571251
inflacja_6 = 2.32938454145522
inflacja_7 = 1.50222984223283
inflacja_8 = 1.78252628571251
inflacja_9 = 2.32884899407637
inflacja_10 = 0.616921348207244
inflacja_11 = 2.35229588637833
inflacja_12 = 0.337779545187098
inflacja_13 = 01.57703524727525
inflacja_14 = -0.292781442607648
inflacja_15 = 2.48619659017508
inflacja_16 = 0.267110317834564
inflacja_17 = 1.41795267229799
inflacja_18 = 1.05424326726375
inflacja_19 = 1.4805201044812
inflacja_20 = 1.57703524727525
inflacja_21 = -0.0774206903147018
inflacja_22 = 1.16573339872354
inflacja_23 = -0.404186717638335
inflacja_24 = 1.49970852083123

oprocentowanie_kredytu = float(input("Podaj oprocentowanie kredytu: "))
kwota_poczatkowa_kredytu = float(input("Podaj kwotę początkową kredytu: "))
stala_warosc_raty = float(input("Podaj stałą wartość raty: "))
formula_do_wyswietlenia = 'Twoja pozostała kwota kredytu to {kwota_kredytu}, to {roznica_w_racie} mniej niż w poprzenim miesiącu.'

print(f'Oprocentowanie to: {oprocentowanie_kredytu}, kwota poczatkowa to: {kwota_poczatkowa_kredytu}, stała wartość raty: {stala_warosc_raty}')

kwota_po_pierwszej_racie = (1 + ((inflacja_1 + oprocentowanie_kredytu)/1200)) * kwota_poczatkowa_kredytu - stala_warosc_raty

kwota_po_drugiej_racie = (1 + ((inflacja_2 + oprocentowanie_kredytu)/1200)) * kwota_po_pierwszej_racie - stala_warosc_raty

kwota_po_trzeciej_racie = (1 + ((inflacja_3 + oprocentowanie_kredytu)/1200)) * kwota_po_drugiej_racie - stala_warosc_raty

kwota_po_czwartej_racie = (1 + ((inflacja_4 + oprocentowanie_kredytu)/1200)) * kwota_po_trzeciej_racie - stala_warosc_raty

kwota_po_piatej_racie = (1 + ((inflacja_5 + oprocentowanie_kredytu)/1200)) * kwota_po_czwartej_racie - stala_warosc_raty

kwota_po_szostej_racie = (1 + ((inflacja_6 + oprocentowanie_kredytu)/1200)) * kwota_po_piatej_racie - stala_warosc_raty

kwota_po_siodmej_racie = (1 + ((inflacja_7 + oprocentowanie_kredytu)/1200)) * kwota_po_szostej_racie - stala_warosc_raty

kwota_po_osmej_racie = (1 + ((inflacja_8 + oprocentowanie_kredytu)/1200)) * kwota_po_siodmej_racie - stala_warosc_raty

kwota_po_dziewiatej_racie = (1 + ((inflacja_9 + oprocentowanie_kredytu)/1200)) * kwota_po_osmej_racie - stala_warosc_raty

kwota_po_dziesiatej_racie = (1 + ((inflacja_10 + oprocentowanie_kredytu)/1200)) * kwota_po_dziewiatej_racie - stala_warosc_raty

kwota_po_jedenastej_racie = (1 + ((inflacja_11 + oprocentowanie_kredytu)/1200)) * kwota_po_dziesiatej_racie - stala_warosc_raty

kwota_po_dwunastej_racie = (1 + ((inflacja_12 + oprocentowanie_kredytu)/1200)) * kwota_po_jedenastej_racie - stala_warosc_raty

kwota_po_trzynastej_racie = (1 + ((inflacja_13 + oprocentowanie_kredytu)/1200)) * kwota_po_dwunastej_racie - stala_warosc_raty

kwota_po_czternastej_racie = (1 + ((inflacja_14 + oprocentowanie_kredytu)/1200)) * kwota_po_trzynastej_racie - stala_warosc_raty

kwota_po_pietnastej_racie = (1 + ((inflacja_15 + oprocentowanie_kredytu)/1200)) * kwota_po_czternastej_racie - stala_warosc_raty

kwota_po_szesnastej_racie = (1 + ((inflacja_16 + oprocentowanie_kredytu)/1200)) * kwota_po_pietnastej_racie - stala_warosc_raty

kwota_po_siedemnastej_racie = (1 + ((inflacja_17 + oprocentowanie_kredytu)/1200)) * kwota_po_szesnastej_racie - stala_warosc_raty

kwota_po_osiemnastej_racie = (1 + ((inflacja_18 + oprocentowanie_kredytu)/1200)) * kwota_po_siedemnastej_racie - stala_warosc_raty

kwota_po_dziewietnastej_racie = (1 + ((inflacja_19 + oprocentowanie_kredytu)/1200)) * kwota_po_osiemnastej_racie - stala_warosc_raty

kwota_po_dwudziestej_racie = (1 + ((inflacja_20 + oprocentowanie_kredytu)/1200)) * kwota_po_dziewietnastej_racie - stala_warosc_raty

kwota_po_dwudziestej_pierwszej_racie = (1 + ((inflacja_21 + oprocentowanie_kredytu)/1200)) * kwota_po_dwudziestej_racie - stala_warosc_raty

kwota_po_dwudziestej_drugiej_racie = (1 + ((inflacja_22 + oprocentowanie_kredytu)/1200)) * kwota_po_dwudziestej_pierwszej_racie - stala_warosc_raty

kwota_po_dwudziestej_trzeciej_racie = (1 + ((inflacja_23 + oprocentowanie_kredytu)/1200)) * kwota_po_dwudziestej_drugiej_racie - stala_warosc_raty

kwota_po_dwudziestej_czwartej_racie = (1 + ((inflacja_24 + oprocentowanie_kredytu)/1200)) * kwota_po_dwudziestej_trzeciej_racie - stala_warosc_raty

print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_pierwszej_racie, roznica_w_racie = (kwota_poczatkowa_kredytu - kwota_po_pierwszej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_drugiej_racie, roznica_w_racie = (kwota_poczatkowa_kredytu - kwota_po_drugiej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_trzeciej_racie, roznica_w_racie = (kwota_poczatkowa_kredytu - kwota_po_trzeciej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_czwartej_racie, roznica_w_racie = (kwota_poczatkowa_kredytu - kwota_po_czwartej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_piatej_racie, roznica_w_racie = (kwota_poczatkowa_kredytu - kwota_po_piatej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_szostej_racie, roznica_w_racie = (kwota_poczatkowa_kredytu - kwota_po_szostej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_siodmej_racie, roznica_w_racie = (kwota_poczatkowa_kredytu - kwota_po_siodmej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_osmej_racie, roznica_w_racie = (kwota_poczatkowa_kredytu - kwota_po_osmej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_dziewiatej_racie, roznica_w_racie = (kwota_poczatkowa_kredytu - kwota_po_dziewiatej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_dziesiatej_racie, roznica_w_racie = (kwota_poczatkowa_kredytu - kwota_po_dziesiatej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_jedenastej_racie, roznica_w_racie = (kwota_poczatkowa_kredytu - kwota_po_jedenastej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_dwunastej_racie, roznica_w_racie = (kwota_poczatkowa_kredytu - kwota_po_dwunastej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_trzynastej_racie, roznica_w_racie = (kwota_poczatkowa_kredytu - kwota_po_trzynastej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_czternastej_racie, roznica_w_racie = (kwota_poczatkowa_kredytu - kwota_po_czternastej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_pietnastej_racie, roznica_w_racie = (kwota_poczatkowa_kredytu - kwota_po_pietnastej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_szesnastej_racie, roznica_w_racie = (kwota_poczatkowa_kredytu - kwota_po_szesnastej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_siedemnastej_racie, roznica_w_racie = (kwota_poczatkowa_kredytu - kwota_po_siedemnastej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_osiemnastej_racie, roznica_w_racie = (kwota_poczatkowa_kredytu - kwota_po_osiemnastej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_dziewietnastej_racie, roznica_w_racie = (kwota_poczatkowa_kredytu - kwota_po_dziewietnastej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_dwudziestej_racie, roznica_w_racie = (kwota_poczatkowa_kredytu - kwota_po_dwudziestej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_dwudziestej_pierwszej_racie, roznica_w_racie = (kwota_poczatkowa_kredytu - kwota_po_dwudziestej_pierwszej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_dwudziestej_drugiej_racie, roznica_w_racie = (kwota_poczatkowa_kredytu - kwota_po_dwudziestej_drugiej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_dwudziestej_trzeciej_racie, roznica_w_racie = (kwota_poczatkowa_kredytu - kwota_po_dwudziestej_trzeciej_racie)))
print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_dwudziestej_czwartej_racie, roznica_w_racie = (kwota_poczatkowa_kredytu - kwota_po_dwudziestej_czwartej_racie)))

#print(formula_do_wyswietlenia.format(kwota_kredytu=kwota_po_dwunastej_racie, roznica_w_racie = (kwota_poczatkowa_kredytu - kwota_po_dwunastej_racie)))
#print(f'Twoja pozostała kwota kredytu to {kwota_po_drugiej_racie}, to {kwota_po_pierwszej_racie - kwota_po_drugiej_racie} mniej niż w poprzednim miesiącu.')
#print(f'Twoja pozostała kwota kredytu to {kwota_po_trzeciej_racie}, to {kwota_po_drugiej_racie - kwota_po_trzeciej_racie} mniej niż w poprzednim miesiącu.')

# Projekt AAL

## Zespół
* Maciej Dmowski
* Jakub Strawa

## Temat
#### Ekstremalnie tania linia lotnicza
Jak wiadomo gdy samolot pasażerski nie znajduje się w powietrzu, to przynosi straty. Z problemem strat zaś poradzić sobie muszą pracownicy ekstremalnie taniej linii lotniczej, znajdującej się na skraju bankructwa i dysponującej jednym samolotem. Dział sprzedaży i marketingu zbiera zamówienia od biur podróży, zaś dział optymalizacji stara się wskazać te, które należy przyjąć tak - aby czas postoju samolotu był jak najmniejszy.
Dla uproszczenia przyjmujemy, iż zamówienia określać będą jedynie moment wylotu i powrotu samolotu na lotnisko (przyjmujemy tylko zamówienia, w których zamawiający zapewnia także „ładunek” na natychmiastowy lot powrotny), zaś czas obsługi naziemnej samolotu jest pomijalny. A zatem - dana jest lista par (w,p) reprezentujących zamówienia zebrane przez dział sprzedaży, gdzie w - czas wylotu samolotu, p - czas przylotu samolotu; w,p < 30000, długość listy jest nie większa niż 10000. Zaproponuj algorytm, który wskaże które zamówienia należy przyjąć, tak aby zmaksymalizować czas pobytu samolotu w powietrzu.


## Opis problemu
#### Projekt napisany w języku Python
Posiadamy maksymalnie 10000 lotów opisanych czasami wylotu i przylotu. Celem naszego algorytmu jest uzyskanie jak największej zajętości czasowej - czasu pobytu samolotu w powietrzu dla przedziału 0 – 30000 liczonego w minutach. Uzyskamy dzięki temu plan lotów na prawie 21 dni.

## Założenia
* Czasy wylotu oraz przylotu generowane są z dokładnością do minuty (przedział 0-30000), a planowanie wykonujemy dla 30000 minut, ponieważ najpóźniejszy możliwy powrót jest po 30000 minutach od początku okresu planowania. 
* Każda minuta poza lot lotniskiem przynosi taki sam zysk bez względu czy lot trwa 10 czy 1000 minut. 
* Dane wejściowe są przyjmowane za poprawne.

## Opis algorytmu
Na początku sortujemy dane według rosnących godzin wylotów. Następnie, generujemy graf skierowany ważony. Wierzchołek startowy: 0, połączony jest ze wszystkimi lotami. Każdy lot połączony jest z każdym możliwym następnym lotem - przylot lotu poprzedniego <= wylot lotu następnego. Krawędzie wychodzące z wierzchołkamają wagi odpowiadające długości lotu tego wierzchołka. Ostatni wierzołek jest punktem końcowym porządkowania - minuta: 30.000, do którego wchodzą krawędzie z wierzchołków każdego z lotów. Następnie wyszukujemy ścieżkę o największym koszcie w grafie - największy sumaryczny czas w powietrzu.

![Przykładowy graf](https://codimd.s3.shivering-isles.com/demo/uploads/upload_13ea6cff1295fc308ec3aca6fea71a18.png)

## Struktury danych wejściowych
Danymi wejściowymi jest lista par liczb naturalnych w pliku .txt.

### Przykładowe dane (np. plik.txt)
```
432,533
64,112
34,234
543,2240
234,653
3,68
0,94
2345,21532
34,67
443,765
2354,5843
723,2341
45,7643
```
### Generacja danych
Generujemy maksymalnie 10 000 lotów sprawdzając tylko czy godzina wylotu jest wcześniejsza od godziny przylotu.
W zależności od potrzeb zmieniane będą paramtery generacji, np. generacja lotu o maksymalnej długości lub lotów o długości 1 minuty, w celu sprawdzenia przypadków skrajnych.

## Dane wynikowe
Lista kolejnych lotów, łączny czas w powietrzu, czas działania algorytmu.

## Sposób działania
1. Pobranie danych wejściowych ze standardowego wejścia i wyrzucenie wyniku na standardowe wyjście, np.: 
     ```
     prog1 –m1 <<in.txt >>out.txt
     ```
2. Wygenerowanie instancji problemu i rozwiązanie go, np.: 
     ```
     prog1 –m2 –n100 –d0.5 >>out.txt
     gen1 –n100 –d0.5 | prog1 –m1
     ```
3. Przeprowadzenie całego procesu testowania z pomiarem czasu dla rosnącego n i porównaniem ze złożonością teoretyczną, np.: 
     ```
     prog1 –m3 –n1000 –k30 –step500 –r10
     ```
    Pomiar czasu dla k problemów o wielkościach n, n+step, n+2*step itd. Dla każdej wielkości losowanych r instancji problemu.


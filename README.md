# Projekt AAL

## Zespół
* Maciej Dmowski
* Jakub Strawa

## Temat
#### Ekstremalnie tania linia lotnicza
Jak wiadomo gdy samolot pasażerski nie znajduje się w powietrzu, to przynosi straty. Z problemem strat zaś poradzić sobie muszą pracownicy ekstremalnie taniej linii lotniczej, znajdującej się na skraju bankructwa i dysponującej jednym samolotem. Dział sprzedaży i marketingu zbiera zamówienia od biur podróży, zaś dział optymalizacji stara się wskazać te, które należy przyjąć tak - aby czas postoju samolotu był jak najmniejszy.
Dla uproszczenia przyjmujemy, iż zamówienia określać będą jedynie moment wylotu i powrotu samolotu na lotnisko (przyjmujemy tylko zamówienia, w których zamawiający zapewnia także „ładunek” na natychmiastowy lot powrotny), zaś czas obsługi naziemnej samolotu jest pomijalny. A zatem - dana jest lista par (w,p) reprezentujących zamówienia zebrane przez dział sprzedaży, gdzie w - czas wylotu samolotu, p - czas przylotu samolotu; w,p < 30000, długość listy jest nie większa niż 10000. Zaproponuj algorytm, który wskaże które zamówienia należy przyjąć, tak aby zmaksymalizować czas pobytu samolotu w powietrzu.


## Opis problemu
#### Projekt napisany w języku Python 3.8
Posiadamy maksymalnie 10000 lotów opisanych czasami wylotu i przylotu. Celem naszego algorytmu jest uzyskanie jak największej zajętości czasowej - czasu pobytu samolotu w powietrzu dla przedziału 0 – 30000 liczonego w minutach. Uzyskamy dzięki temu plan lotów na prawie 21 dni zakładając, że 1 jednostka czasowa to 1 minuta.

## Założenia
* Czasy wylotu oraz przylotu generowane są z dokładnością do minuty (przedział 0-30000), a planowanie wykonujemy dla 30000 minut, ponieważ najpóźniejszy możliwy powrót jest po 30000 minutach od początku okresu planowania. 
* Każda minuta poza lot lotniskiem przynosi taki sam zysk bez względu czy lot trwa 10 czy 10000 minut. 

## Opis algorytmu
Na początku sortujemy dane według rosnących godzin wylotów. Następnie, generujemy graf skierowany ważony. Wierzchołek startowy: 0, połączony jest ze wszystkimi lotami. Każdy lot połączony jest z każdym możliwym następnym lotem - przylot lotu poprzedniego <= wylot lotu następnego. Krawędzie wychodzące z wierzchołka mają wagi odpowiadające długości lotu tego wierzchołka. Ostatni wierzchołek jest punktem końcowym porządkowania - minuta: 30.000, do którego wchodzą krawędzie z wierzchołków każdego z lotów. Następnie wyszukujemy ścieżkę o największym koszcie w grafie - największy sumaryczny czas w powietrzu.

![Przykładowy graf](https://codimd.s3.shivering-isles.com/demo/uploads/upload_13ea6cff1295fc308ec3aca6fea71a18.png)

## Struktury danych wejściowych
Danymi wejściowymi jest lista par liczb naturalnych w pliku .txt, gdzie druga liczba jest większa od pierwszej o co najmnniej 1, a przedział utworzony przez te liczby należy do przedziału [0,30000].

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
W zależności od potrzeb zmieniane będą parametry generacji, np. generacja lotów o długości 30000 lub 1, w celu sprawdzenia przypadków skrajnych.

## Dane wynikowe
Dla trybu 1(-m 1) do pliku zapisywane są następujące dane:
- łączny czas samolotu w powietrzu
- łączny czas wszystkich obliczeń dla danego problemu
- wyodrębnione czasy poszczególnych operacji: generacja danych, dodawanie wierzchołków, dodawanie krawędzi, sortowanie, szukanie ścieżki
- kolejność oraz czasy wylotów i przylotów wybranych lotów

Dla trybu 2(-m 2) do pliku zapisywane są następujące dane:
- łączny czas samolotu w powietrzu
- łączny czas wszystkich obliczeń dla danego problemu
- wyodrębnione czasy poszczególnych operacji: generacja danych, dodawanie wierzchołków, dodawanie krawędzi, sortowanie, szukanie ścieżki
- kolejność oraz czasy wylotów i przylotów wybranych lotów
Dodatkowo do pliku generated_data.txt zapisywane są wygenerowane loty.

Dla trybu 3(-m 3) do pliku zapisywane są następujące dane:
- tabela do pliku table.txt posiadająca wszystkie informacje o iteracjach i instancjach problemów(wszystkie informacje z trybu 1)
- porównanie z założoną żłożonością obliczeniową

## Sposób działania
0. Do poprawnego działania program wymaga ściągnięcia biblioteki Beautiful Table:
     ```
     pip install beautifultable
     ```
1. Pobranie danych wejściowych z pliku i wypisanie rozwiązania do pliku: 
     ```
     python main.py –m 1 -in data.txt -out result.txt
     ```
2. Wygenerowanie instancji problemu o rozmiarze n i wypisanie rozwiązanie do pliku: 
     ```
     python main.py -m 2 -n 1000 -out result.txt
     ```
3. Przeprowadzenie całego procesu testowania z pomiarem czasu dla rosnącego o s(tep) n i porównaniem ze złożonością teoretyczną: 
     ```
     python main.py -m 3 -n 1000 –s 500 -k 30 –r 10
     ```
    Pomiar czasu dla k problemów o wielkościach n, n+step, n+2*step itd. Dla każdej wielkości losowanych r instancji problemu.
4. Uzyskanie prostej pomocy co do flag:
    ```
    python main.py -h
    ```

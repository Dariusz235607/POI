import csv
import numpy as np
from sklearn.cluster import KMeans
import random


#Wczytanie chmury punktow
def wczytaj_chmury_xyz(nazwapliku):
    punkty = []
    with open(nazwapliku, 'r') as file:
        reader = csv.reader(file, delimiter=' ')
        for row in reader:
            # Konwersja współrzędnych tekstowych na liczby zmiennoprzecinkowe
            punkty.append([float(val) for val in row])
    return np.array(punkty)


#Uzycie funkcji K-średnich (podzielenie punktow na 3 grupy/klastry)
def klasterpunktow(punkty, k=3):
    kmeans = KMeans(n_clusters=k, random_state=123)
    labels = kmeans.fit_predict(punkty)
    return labels


#obliczenie równań płaszczyzny na podstawie 3 punków
#równanie płaszczyzny: ax + by + cz + d = 0
def rownanieplaszczyzny(p1, p2, p3):
    #utworzenie wektorów płaszczyzny
    v1 = p2 - p1
    v2 = p3 - p1
    #obliczenie wektora normalnego płaszczyzny (iloczyn wektorowy)
    normal = np.cross(v1, v2)
    #normalizacja wektora normalnego (długość = 1)
    normal = normal / np.linalg.norm(normal)
    #obliczenie współczynnika d z równania płaszczyzny
    d = -np.dot(normal, p1)
    return normal, d


#obliczenie odległości punktu od płaszczyzny
def odlegloscipunktow(punkt, normal, d):
    return abs(np.dot(normal, punkt) + d) / np.linalg.norm(normal)


#algorytm RANSAC do znajdowania płaszczyzn
def RANSAC(punkty, i=100, wartosc_prog=1.0):
    best_dopasowanie = []   #najlepszy zbiór punktów pasujących do płaszczyzny
    best_basic = None       #najlepszy wektor normalny
    best_d = None           #najlepszy współczynnik d

    #Ransac
    for _ in range(i):
        #losowy wybór 3 punktów do próbki
        probka = punkty[random.sample(range(len(punkty)), 3)]
        p1, p2, p3 = probka
        try:
            normal, d = rownanieplaszczyzny(p1, p2, p3)
        except:
            continue    #pomijanie jeżeli nie można obliczyć

        odleglosci = np.abs(np.dot(punkty, normal) + d)
        dopasowanie = punkty[odleglosci < wartosc_prog]

        if len(dopasowanie) > len(best_dopasowanie):
            best_dopasowanie = dopasowanie
            best_basic = normal
            best_d = d

    #średnia odległość punktów zgodnych od płaszczyzny
    if best_dopasowanie is not None and len(best_dopasowanie) > 0:
        odleglosci = [odlegloscipunktow(p, best_basic, best_d) for p in best_dopasowanie]
        srednia_odleglosc = np.mean(odleglosci)
    else:
        srednia_odleglosc = float('inf')

    return best_basic, srednia_odleglosc


#Klasyfikacja płaszczyzny
def klasyfikacja_figur(norm_wect, srednia_odleglosc, wartosc_prog=0.1):
    if srednia_odleglosc > wartosc_prog:
        return "nie jest płaszczyzną"

    # Jeśli wektor normalny jest prawie pionowy względem Z, to pozioma
    if abs(norm_wect[2]) > 0.9:
        return "płaszczyzna pozioma"
    else:
        return "płaszczyzna pionowa"


#MAIN
def main():
    nazwapliku = "chmura_punktow.xyz"
    punkty = wczytaj_chmury_xyz(nazwapliku)
    labels = klasterpunktow(punkty)

    print("Wyniki analizy klas:")

    #analiza każdego klastra osobno
    for i in range(3):
        klasterpunktow_i = punkty[labels == i]
        normal, sredniaodl = RANSAC(klasterpunktow_i)
        klasyfikacja = klasyfikacja_figur(normal, sredniaodl)

        print(f"\nChmura {i + 1}:")
        print(f"  Wektor normalny: {normal}")
        print(f"  Średnia odległość punktów od płaszczyzny: {sredniaodl:.4f}")
        print(f"  Klasyfikacja: {klasyfikacja}")


if __name__ == "__main__":
    main()

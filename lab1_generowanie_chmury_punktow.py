import numpy as np
from csv import writer

'Stworzenie funkcji'

'Pozioma powierzchnia'
def utworz_powierzchnie_pozioma(szerokosc, dlugosc, num_points):
    x = np.random.uniform(10, szerokosc, num_points)
    y = np.random.uniform(10, dlugosc, num_points)
    z = np.zeros(num_points)
    return np.column_stack((x, y, z))

'Pionowa powierzchnia'
def utworz_powierzchnie_pionowa(szerokosc, wysokosc, num_points):
    x = np.random.uniform(10, szerokosc, num_points)
    y = np.zeros(num_points)
    z = np.random.uniform(10, wysokosc, num_points)
    return np.column_stack((x, y, z))

'Cylinder'
def utworz_cylinder(promien, wysokosc, num_points):
    theta = np.random.uniform(0, 2 * np.pi, num_points)
    x = promien * np.cos(theta)-10
    y = promien * np.sin(theta)-20
    z = np.random.uniform(0, wysokosc, num_points)
    return np.column_stack((x, y, z))

'Funkcja zapisu do pliku xyz na podstawie pliku csv'
def save_xyz(filename, points):
    with open(filename, 'w', encoding='utf-8', newline='\n') as csvfile:
        csvwriter = writer(csvfile, delimiter=' ')
        for p in points:
            csvwriter.writerow(p)

'Ilość punktów chmury na dany obiekt'
num_points = 1000

'Wywolanie funkcji i stworzenie chmury punktow 3 obiektow'
powierzchnia_pozioma = utworz_powierzchnie_pozioma(100, 100, num_points)
powierzchnia_pionowa = utworz_powierzchnie_pionowa(200, 50, num_points)
cylinder = utworz_cylinder(20, 30, num_points)

'Łączenie wszystkich punktów'
all_points = np.vstack((powierzchnia_pozioma, powierzchnia_pionowa, cylinder))

'Zapis do jednego pliku'
save_xyz("chmura_punktow.xyz", all_points)

print("Plik .xyz z wszystkimi obiektami został zapisany.")

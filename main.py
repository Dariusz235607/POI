import numpy as np
from csv import writer

'Stworzenie funkcji'

'Pozioma powierzchnia'
def generate_horizontal_plane(szerokosc, dlugosc, num_points):
    x = np.random.uniform(-szerokosc / 2, szerokosc / 2, num_points)
    y = np.random.uniform(-dlugosc / 2, dlugosc / 2, num_points)
    z = np.zeros(num_points)
    return np.column_stack((x, y, z))

'Pionowa powierzchnia'
def generate_vertical_plane(szerokosc, wysokosc, num_points):
    x = np.random.uniform(-szerokosc / 2, szerokosc / 2, num_points)
    y = np.zeros(num_points)
    z = np.random.uniform(0, wysokosc, num_points)
    return np.column_stack((x, y, z))

'Cylinder'
def generate_cylindrical_surface(promien, wysokosc, num_points):
    theta = np.random.uniform(0, 2 * np.pi, num_points)
    x = promien * np.cos(theta)
    y = promien * np.sin(theta)
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
horizontal_plane = generate_horizontal_plane(100, 100, num_points)
vertical_plane = generate_vertical_plane(200, 50, num_points)
cylindrical_surface = generate_cylindrical_surface(20, 30, num_points)

'Łączenie wszystkich punktów'
all_points = np.vstack((horizontal_plane, vertical_plane, cylindrical_surface))

'Zapis do jednego pliku'
save_xyz("chmura_punktow.xyz", all_points)

print("Plik .xyz z wszystkimi obiektami został zapisany.")

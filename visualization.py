import matplotlib.pyplot as plt

def draw_target(ax):
    # Średnica największego okręgu
    max_diameter = 13

    # Promień największego okręgu
    max_radius = max_diameter / 2

    # Środek tarczy
    center = (7, 7)

    # Liczba okręgów
    num_circles = 10

    # Kolory okręgów: pierwsze 6 zewnętrznych białe, kolejne 4 wewnętrzne czarne
    for i in range(num_circles):
        radius = max_radius - i * (max_radius / num_circles)
        if i < 6:
            # Okręgi białe z czarnymi obwodami
            circle = plt.Circle(center, radius, color='white', ec='black')
        else:
            # Okręgi czarne z białymi obwodami
            circle = plt.Circle(center, radius, color='black', ec='white')
        ax.add_patch(circle)

    # Numerowanie okręgów
    for i in range(6):
        # Numerowanie dla okręgów od 1 do 8 (od góry do dołu)
        ax.text(center[0], center[1] + (max_radius - (i + 0.5) * (max_radius / num_circles)), str(i + 1),
                color='black', fontsize=12, ha='center', va='center')

    for i in range(6,8):
        # Numerowanie dla okręgów od 1 do 8 (od góry do dołu)
        ax.text(center[0], center[1] + (max_radius - (i + 0.5) * (max_radius / num_circles)), str(i + 1),
            color='white', fontsize=12, ha='center', va='center')

    for i in range(6):
        # Numerowanie dla okręgów od 1 do 8 (od dołu do góry)
        ax.text(center[0], center[1] - (max_radius - (i + 0.5) * (max_radius / num_circles)), str(i + 1),
                color='black', fontsize=12, ha='center', va='center')

    for i in range(6,8):
        # Numerowanie dla okręgów od 1 do 8 (od dołu do góry)
        ax.text(center[0], center[1] - (max_radius - (i + 0.5) * (max_radius / num_circles)), str(i + 1),
                color='white', fontsize=12, ha='center', va='center')

    # Ustawienia osi
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 14)
    ax.set_aspect('equal', 'box')
    ax.set_xticks(range(0, 15))
    ax.set_yticks(range(0, 15))
    # ax.grid(True)  # dodawanie siatki

# współrzędne strzałów
shots = [
    ((7884.775543608633*13)/64430, (22838.51119155334*13)/64430),
    ((24073.51260199742*13/64430), (37992.12236113629*13/64430)),
    ((15116.66390309517*13/64430), (54275.71549885366*13/64430)),
    ((18564.395807999732*13/64430), (43437.10125277875*13/64430)),
    ((22664.709740788436*13/64430), (29410.843368672293*13/64430)),
    ((31067.860132505986*13/64430), (57912.247095776445*13/64430)),
    ((36189.26367992368*13/64430), (54073.65887752067*13/64430)),
    ((42077.08474912534*13/64430), (24095.11853764947*13/64430))
]


fig, ax = plt.subplots()
draw_target(ax)

# Rysowanie strzałów
for x, y in shots:
    ax.plot(x, y, 'ro')  # dodanie czerwonego punktu

plt.show()

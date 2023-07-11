import skyfield as skyfield
import networkx as nx
import matplotlib.pyplot as plt
from skyfield.data import hipparcos, stellarium
from skyfield.api import Star, load,
import constelas

print(constelas.constell)

with load.open(hipparcos.URL) as f:
    stars = hipparcos.load_dataframe(f)
url = ('https://raw.githubusercontent.com/Stellarium/stellarium/master'
       '/skycultures/modern_st/constellationship.fab')
with load.open(url) as f:
    constellations = stellarium.parse_constellations(f)

limiting_magnitude = 6.5
bright_stars = (stars.magnitude <= limiting_magnitude)

def get_cstars(ct,n):
    hoshi = []
    for i in range(0, len(ct[n][1])):
        if ct[n][1][i][0] not in hoshi:
            hoshi.append(ct[n][1][i][0])
        if ct[n][1][i][1] not in hoshi:
            hoshi.append(ct[n][1][i][1])
        continue
    return hoshi

def get_lines(ct, n):
    return ct[n][1:]

def star_info(z):
    star_info = Star.from_dataframe(stars.loc[z])
    return star_info

def star_pos(star_info):
    planets = load('de421.bsp')
    earth = planets['earth']
    ts = load.timescale()
    t = ts.now()
    astrometric = earth.at(t).observe(star_info)
    return astrometric.position.au

def form_const(ct, n):
    cstars = get_cstars(ct, n)
    x_stars, y_stars = [], []
    for i in cstars:
        x_stars.append(star_pos(star_info(i))[0])
        y_stars.append(star_pos(star_info(i))[1])
    xy_stars = [x_stars,y_stars]
    return xy_stars

def plot_const(c, n):
    options = {
        'edge_color': 'white',
        'node_color': 'orange',
        'node_size': 200,
        'width': 1,
        'node_shape': "*",
        'style': ':',
        'font_color': 'white',
    }
    constella = get_lines(c, n)[0]
    stars = get_cstars(c, n)
    coords = form_const(c, n)
    positions = dict()
    for i in range(len(stars)):
        positions[stars[i]] = (coords[0][i], coords[1][i])
    G = nx.Graph()
    G.add_edges_from(constella)
    ax = plt.gca().set_facecolor("black")
    nx.draw_networkx(G, positions, with_labels=False, label="The Aries Constellation", **options)
    plt.show()

plot_const(constellations, 6)
print(get_lines(constellations, 6))

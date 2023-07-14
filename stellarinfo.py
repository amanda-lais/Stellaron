from skyfield.api import Star, load, wgs84
from skyfield.data import hipparcos, stellarium
from skyfield.projections import build_stereographic_projection
import skyfield as skyfield

# === GLOBAL ===

with load.open(hipparcos.URL) as f:
    stars = hipparcos.load_dataframe(f)
url = ('https://raw.githubusercontent.com/Stellarium/stellarium/master'
       '/skycultures/modern_st/constellationship.fab')
with load.open(url) as f:
    constellations = stellarium.parse_constellations(f)

# === FUNCTIONS ===

###
# n: id number of the constellation
# h: HIP

# Gets stars' information
def stars_info():
    planets = load('de421.bsp')
    earth = planets['earth']
    ts = load.timescale()
    t = ts.now()
    observer = wgs84.latlon(+0, -0).at(t)
    ra, dec, distance = observer.radec()
    center_object = Star(ra=ra, dec=dec)
    center = earth.at(t).observe(center_object)
    projection = build_stereographic_projection(center)
    star_positions = earth.at(t).observe(Star.from_dataframe(stars))
    stars['x'], stars['y'] = projection(star_positions)
    return stars

# Gets the stars pertaining
# to a certain constellation
def get_ctstars(n):
    ct_stars = []
    for i in range(0, len(constellations[n][1])):
        if constellations[n][1][i][0] not in ct_stars:
            ct_stars.append(constellations[n][1][i][0])
        if constellations[n][1][i][1] not in ct_stars:
            ct_stars.append(constellations[n][1][i][1])
        continue
    return ct_stars

# Gets constellation's edges
def get_lines(h):
    return constellations[h][1:]

# Gets the XY coordinates
# of a certain star
def get_xy(stars_info, h):
    return stars_info[['x', 'y']].loc[h].values

# Gets the positions of all stars that
# are part of a certain constellation
def ct_pos(n):
    positions = dict()
    st_info = stars_info()
    ct_stars = get_ctstars(n)
    for i in range(len(ct_stars)):
        xy = get_xy(st_info, ct_stars[i])
        positions[ct_stars[i]] = (xy[0], xy[1])
    return positions
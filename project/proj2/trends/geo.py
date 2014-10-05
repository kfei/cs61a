"""Geography and projection utilities."""

from data import DATA_PATH
from math import sin, cos, atan2, radians, sqrt
from json import JSONDecoder

#############################
# Position Data Abstraction #
#############################

def make_position(lat, lon):
    """Return a geographic position, which has a latitude and longitude."""
    return [lat, lon]

def latitude(position):
    """Return the latitudinal coordinate of a geographic position."""
    return position[0]

def longitude(position):
    """Return the longitudinal coordinate of a geographic position."""
    return position[1]

### === +++ ABSTRACTION BARRIER +++ === ###

def geo_distance(position0, position1):
    """Return the great circle distance (in miles) between two
    geographic positions.

    Uses the "haversine" formula.
    http://en.wikipedia.org/wiki/Haversine_formula

    >>> round(geo_distance(make_position(50, 5), make_position(58, 3)), 1)
    559.2
    """
    earth_radius = 3963.2  # miles
    positions = [position0, position1]
    lat0, lat1 = [radians(latitude(p)) for p in positions]
    lon0, lon1 = [radians(longitude(p)) for p in positions]
    dlat, dlon = lat1-lat0, lon1-lon0
    a = sin(dlat/2) ** 2  + sin(dlon/2) ** 2 * cos(lat0) * cos(lat1)
    c = 2 * atan2(sqrt(a), sqrt(1-a));
    return earth_radius * c;

def position_to_xy(position):
    """Convert a geographic position within the US to a planar x-y point."""
    lat = latitude(position)
    lon = longitude(position)
    if lat < 25:
        return _hawaii(position)
    elif lat > 52:
        return _alaska(position)
    else:
        return _lower48(position)

def albers(origin, parallels, translate, scale):
    """Return an Albers projection from geographic positions to x-y positions.

    Derived from Mike Bostock's Albers javascript implementation for D3
    http://mbostock.github.com/d3
    http://mathworld.wolfram.com/AlbersEqual-AreaConicProjection.html

    Arguments:
    origin -- a geographic position
    parallels -- bounding latitudes
    translate -- x-y translation to place the projection within a larger map
    scale -- scaling factor
    """
    phi1, phi2 = [radians(p) for p in parallels]
    s, c = sin(phi1), cos(phi1)
    base_lat = radians(latitude(origin))
    base_lon = radians(longitude(origin))
    n = 0.5 * (s + sin(phi2))
    C = c*c + 2*n*s
    p0 = sqrt(C - 2*n*sin(base_lat))/n

    def project(position):
        lat, lon = radians(latitude(position)), radians(longitude(position))
        t = n * (lon - base_lon)
        p = sqrt(C - 2*n*sin(lat))/n
        x = scale * p * sin(t) + translate[0]
        y = scale * (p * cos(t) - p0) + translate[1]
        return [x, y]
    return project

_lower48 = albers(make_position(38, -98), [29.5, 45.5], [480, 250], 1000)
_alaska = albers(make_position(60, -160), [55, 65], [150, 440], 400)
_hawaii = albers(make_position(20, -160), [8, 18], [300, 450], 1000)

def format_shapes(shapes):
    """Format a shape as a list of lists of positions, one for each shape.
    The states.json file has an odd format, that the get function normalizes.

    >>> single = []
    """
    def get(shape):
        """Get the shape from one of the elements of shapes."""
        if type(shape[0][0]) == list:  # the shape is a single polygon
            assert len(shape) == 1, 'Multi-polygon shape'
            return shape[0]
        else:
            return shape

    return [[make_position(lat, lon) for lon, lat in get(s)] for s in shapes]

def load_states():
    """Return a dictionary from state names to lists of polygons.

    >>> len(load_states()['HI'])  # Hawaii has 5 islands
    5
    """
    with open(DATA_PATH + 'states.json', encoding='utf8') as json_data_file:
        states = JSONDecoder().decode(json_data_file.read())
    return {state: format_shapes(shapes) for state, shapes in states.items()}

us_states = load_states()

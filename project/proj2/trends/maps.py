"""Map drawing utilities for U.S. sentiment data."""

from graphics import Canvas
from geo import position_to_xy, us_states

# A fixed gradient of sentiment colors from negative (blue) to positive (red)
# Colors chosen via Cynthia Brewer's Color Brewer (colorbrewer2.com)
SENTIMENT_COLORS = ["#313695", "#4575B4", "#74ADD1", "#ABD9E9", "#E0F3F8",
                    "#FFFFFF", "#FEE090", "#FDAE61", "#F46D43", "#D73027",
                    "#A50026"]
SENTIMENT_COLORS = ["#22366A", "#3B596A", "#427676", "#3F9A82", "#77BFFF", 
                    "#FFFFFF",
                    #"#ECDB60", "#F1B82D", "#FFDD22", "#FFAA11", "#FF8800"
                    "#ECDB60", "#FFDD22", "#FFAA11", "#FF8800", "#FF5500"
                    ]
GRAY = "#AAAAAA"

def get_sentiment_color(sentiment, sentiment_scale=4):
    """Returns a color corresponding to the sentiment value.

    Arguments:
    sentiment -- a number between -1 (negative) and +1 (positive)
    """
    if sentiment is None:
        return GRAY
    scaled = (sentiment_scale * sentiment + 1)/2
    index = int( scaled * len(SENTIMENT_COLORS) ) # Rounds down
    if index < 0:
        index = 0
    if index >= len(SENTIMENT_COLORS):
        index = len(SENTIMENT_COLORS) - 1
    return SENTIMENT_COLORS[index]

def draw_state(shapes, sentiment_value=None):
    """Draw the named state in the given color on the canvas.

    Arguments:
    state -- a list of list of polygons (which are lists of positions)
    sentiment_value -- a number between -1 (negative) and 1 (positive)
    canvas -- the graphics.Canvas object
    """
    for polygon in shapes:
        vertices = [position_to_xy(position) for position in polygon]
        color = get_sentiment_color(sentiment_value)
        get_canvas().draw_polygon(vertices, fill_color=color)

def draw_name(name, location):
    """Draw the two-letter postal code at the center of the state.

    Arguments:
    location -- a position
    """
    center = position_to_xy(location)
    get_canvas().draw_text(name.upper(), center, anchor='center', style='bold')

def draw_dot(location, sentiment_value=None, radius=3):
    """Draw a small dot at location.

    Arguments:
    location -- a position
    sentiment_value -- a number between -1 (negative) and 1 (positive)
    """
    center = position_to_xy(location)
    color = get_sentiment_color(sentiment_value)
    get_canvas().draw_circle(center, radius, fill_color=color)

def memoize(fn):
    """A decorator for caching the results of the decorated function."""
    cache = {}
    def memoized(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]
    return memoized

@memoize
def get_canvas():
    """Return a Canvas, which is a drawing window."""
    return Canvas(width=960, height=500)

def wait(secs=0):
    """Wait for mouse click."""
    get_canvas().wait_for_click(secs)

def message(s):
    """Display a message."""
    c = get_canvas()
    c.draw_text(s, (c.width//2, c.height//2), size=36, anchor='center')

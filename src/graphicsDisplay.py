# graphicsDisplay.py
# ------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from graphicsUtils import *
import graphicsUtils as _gu
import math, time
from game import Directions

DEFAULT_GRID_SIZE = 30.0
FONT = "Segoe UI"

# Page layout (pixels)
MARGIN = 24             # gap between window edge and panels
MIN_WIDTH = 840         # header/footer need this much room on small mazes
MAZE_SIDE_PAD = 70      # extra inset of the maze relative to the panels
HEADER_TOP = 16
HEADER_HEIGHT = 56
MAZE_GAP = 24           # vertical gap header->maze and maze->footer
FOOTER_HEIGHT = 66
INFO_PANE_HEIGHT = HEADER_HEIGHT

# Palette
BG_TOP = (7, 18, 48)
BG_BOTTOM = (3, 8, 22)
MAZE_FLOOR_COLOR = '#020714'
PANEL_FILL = '#07122c'
PANEL_BORDER = '#2152c4'
PANEL_GLOW = ['#0a1c48', '#0d2763']
WALL_LAYERS = [         # (width as fraction of grid, colour) drawn back-to-front
    (0.98, '#06173f'),
    (0.84, '#0a2e88'),
    (0.68, '#46a6ff'),
    (0.58, '#1456f0'),
    (0.22, '#1d63ff'),
]
FOOD_COLOR = '#FFFFFF'
FOOD_GLOW_COLOR = '#24438f'
PACMAN_COLOR = '#FFD21F'
PACMAN_OUTLINE = '#FFB000'
PACMAN_GLOW = ['#241e0a', '#4a3c0b', '#8a6d0c']
BACKGROUND_COLOR = '#040914'
TEXT_COLOR = '#FFFFFF'
SCORE_COLOR = '#FFD21F'
EXPANDED_COLOR = '#0c2f66'       # tiles for cells explored by the last search

BTN_ACTIVE = {'fill': '#1673ff', 'outline': '#59c8ff', 'text': '#FFFFFF', 'glow': ['#0b2a66', '#114aa8']}
BTN_IDLE = {'fill': '#0b1a3d', 'outline': '#2a4a8f', 'text': '#d6e2ff', 'glow': [None, None]}
BTN_HOVER = {'fill': '#11285a', 'outline': '#3d6fd0', 'text': '#FFFFFF', 'glow': [None, None]}

ALGORITHMS = [
    ('bfs', 'BFS', 70),
    ('dfs', 'DFS', 70),
    ('ucs', 'UCS', 70),
    ('astar', 'A* Search', 95),
    ('retry', '🔄 Retry', 85),
    ('autograder', '🧪 Autograder', 115)
]


def _blend(c0, c1, t):
    return '#%02x%02x%02x' % tuple(int(a + (b - a) * t) for a, b in zip(c0, c1))


def roundedRect(x0, y0, x1, y1, r, **kw):
    """Draw a rounded rectangle on the canvas as a smoothed polygon."""
    if _gu._canvas is None: return None
    r = min(r, (x1 - x0) / 2.0, (y1 - y0) / 2.0)
    pts = [x0 + r, y0, x0 + r, y0, x1 - r, y0, x1 - r, y0, x1, y0, x1, y0 + r, x1, y0 + r,
           x1, y1 - r, x1, y1 - r, x1, y1, x1 - r, y1, x1 - r, y1, x0 + r, y1, x0 + r, y1,
           x0, y1, x0, y1 - r, x0, y1 - r, x0, y0 + r, x0, y0 + r, x0, y0]
    return _gu._canvas.create_polygon(pts, smooth=True, **kw)


def glowPanel(x0, y0, x1, y1, r, fill=PANEL_FILL, border=PANEL_BORDER, glow=PANEL_GLOW, tags=()):
    """A rounded panel with a soft outer glow. Returns the ids of every layer."""
    ids = []
    for i, colour in enumerate(glow):
        if colour is None: continue
        g = (len(glow) - i) * 2.5
        ids.append(roundedRect(x0 - g, y0 - g, x1 + g, y1 + g, r + g, fill='', outline=colour, width=2.5, tags=tags))
    ids.append(roundedRect(x0, y0, x1, y1, r, fill=fill, outline=border, width=1.5, tags=tags))
    return ids


def pacmanShape(pos, r, direction=Directions.EAST, mouth=50, glow=True):
    """Pacman as a yellow pie slice, optionally with a warm halo. Returns item ids."""
    if _gu._canvas is None: return []
    x, y = pos
    ids = []
    if glow:
        for i, colour in enumerate(PACMAN_GLOW):
            gr = r * (1.55 - i * 0.17)
            ids.append(_gu._canvas.create_oval(x - gr, y - gr, x + gr, y + gr, fill=colour, outline=''))
    facing = {Directions.EAST: 0, Directions.NORTH: 90, Directions.WEST: 180, Directions.SOUTH: 270}.get(direction, 0)
    start = facing + mouth / 2.0
    ids.append(_gu._canvas.create_arc(x - r, y - r, x + r, y + r, start=start, extent=360 - mouth,
                                      style='pieslice', fill=PACMAN_COLOR, outline=PACMAN_OUTLINE, width=1))
    return ids


class InfoPane:
    """Header bar: logo, score/lives pill and settings button. Score is static for now."""
    def __init__(self, layout, gridsize, canvasWidth=None):
        self.gridsize = gridsize
        self.width = canvasWidth or layout.width * gridsize
        self.height = INFO_PANE_HEIGHT
        self.drawPane()

    def drawPane(self):
        c = _gu._canvas
        if c is None: return
        x0, y0 = MARGIN, HEADER_TOP
        x1, y1 = self.width - MARGIN, HEADER_TOP + HEADER_HEIGHT
        cy = (y0 + y1) / 2.0
        glowPanel(x0, y0, x1, y1, 16)

        # Logo + title
        pacmanShape((x0 + 36, cy), 15, mouth=70, glow=False)
        c.create_text(x0 + 66, cy, text="Pacman", fill=TEXT_COLOR, font=(FONT, 17, "bold"), anchor="w")

        # Score / lives pill
        pw, ph = 340, HEADER_HEIGHT - 12
        px0, px1 = self.width / 2.0 - pw / 2.0, self.width / 2.0 + pw / 2.0
        glowPanel(px0, cy - ph / 2.0, px1, cy + ph / 2.0, ph / 2.0, fill='#091733', border='#2a5ccc', glow=['#0b2050'])
        c.create_text(px0 + 48, cy, text="Score", fill=TEXT_COLOR, font=(FONT, 12), anchor="w")
        self.scoreText = c.create_text(px0 + 108, cy, text="0", fill=SCORE_COLOR, font=(FONT, 17, "bold"), anchor="w")
        mid = px0 + pw / 2.0 - 8
        c.create_line(mid, cy - 13, mid, cy + 13, fill='#2a4a8f', width=1)
        c.create_text(mid + 20, cy, text="Lives", fill=TEXT_COLOR, font=(FONT, 12), anchor="w")
        for i in range(3):
            pacmanShape((mid + 86 + i * 25, cy), 10, mouth=70, glow=False)

        # Settings button (decorative)
        sx, sr = x1 - 30, 16
        c.create_oval(sx - sr - 2, cy - sr - 2, sx + sr + 2, cy + sr + 2, outline='#0d2763', width=2)
        c.create_oval(sx - sr, cy - sr, sx + sr, cy + sr, fill='#0a1a42', outline='#2f7dff', width=2)
        c.create_text(sx, cy, text="⚙", fill='#e6efff', font=("Segoe UI Symbol", 14))

    def updateScore(self, score):
        # Score logic intentionally not wired up yet; the header always shows 0.
        pass


class PacmanGraphics:
    def __init__(self, zoom=1.0, frameTime=0.1, capture=False):
        self.zoom = zoom
        self.gridSize = DEFAULT_GRID_SIZE * zoom
        self.frameTime = frameTime
        self.capture = capture
        self.activeAlgo = 'bfs'
        self._expanded_cells = []
        self.floorId = None

    def initialize(self, state, isBlue=False):
        self.isBlue = isBlue
        self.startGraphics(state.layout)
        self.drawStaticObjects(state)
        self.drawAgentObjects(state)

    def startGraphics(self, layout):
        self.layout = layout
        self.width = layout.width
        self.height = layout.height

        mazeW = self.width * self.gridSize
        mazeH = self.height * self.gridSize
        self.canvasWidth = max(mazeW + 2 * (MARGIN + MAZE_SIDE_PAD), MIN_WIDTH)
        self.mazeLeft = (self.canvasWidth - mazeW) / 2.0
        self.mazeTop = HEADER_TOP + HEADER_HEIGHT + MAZE_GAP
        self.footerTop = self.mazeTop + mazeH + MAZE_GAP
        self.canvasHeight = self.footerTop + FOOTER_HEIGHT + 18

        begin_graphics(self.canvasWidth, self.canvasHeight, BACKGROUND_COLOR, "Pacman")
        if _gu._canvas is not None:
            _gu._canvas.configure(highlightthickness=0, borderwidth=0)
        self.drawBackground()
        self.infoPane = InfoPane(layout, self.gridSize, self.canvasWidth)
        self.drawFooter()

    def drawBackground(self):
        c = _gu._canvas
        if c is None: return
        bands = 64
        step = self.canvasHeight / float(bands)
        for i in range(bands):
            colour = _blend(BG_TOP, BG_BOTTOM, i / float(bands - 1))
            c.create_rectangle(0, i * step, self.canvasWidth, (i + 1) * step + 1, fill=colour, outline='')
        # Faint side panels peeking in from the window edges
        top, bottom = self.mazeTop + 10, self.footerTop - 30
        roundedRect(-60, top, 14, bottom, 22, fill='#06102a', outline='#14306e', width=1.5)
        roundedRect(self.canvasWidth - 14, top, self.canvasWidth + 60, bottom, 22, fill='#06102a', outline='#14306e', width=1.5)

    def drawFooter(self):
        c = _gu._canvas
        if c is None: return
        x0, y0 = MARGIN, self.footerTop
        x1, y1 = self.canvasWidth - MARGIN, self.footerTop + FOOTER_HEIGHT
        cy = (y0 + y1) / 2.0
        glowPanel(x0, y0, x1, y1, 16)
        label = c.create_text(x0 + 26, cy, text="Search Algorithms:", fill='#e6edff', font=(FONT, 12), anchor="w")

        bx = c.bbox(label)[2] + 22
        bh = 38
        self.buttons = {}
        for key, caption, bw in ALGORITHMS:
            tag = 'algo_' + key
            self.buttons[key] = self.buildButton((bx, cy - bh / 2.0, bx + bw, cy + bh / 2.0), caption, tag)
            self.styleButton(key, BTN_ACTIVE if key == self.activeAlgo else BTN_IDLE)
            c.tag_bind(tag, '<Button-1>', lambda e, k=key: self.onAlgoClick(k))
            c.tag_bind(tag, '<Enter>', lambda e, k=key: self.onAlgoHover(k, True))
            c.tag_bind(tag, '<Leave>', lambda e, k=key: self.onAlgoHover(k, False))
            bx += bw + 12

    def buildButton(self, box, caption, tag):
        """Create a button's canvas items once; styleButton only recolours them.
        (Deleting items under the cursor fires <Leave>/<Enter> and loops forever.)"""
        c = _gu._canvas
        x0, y0, x1, y1 = box
        glow = []
        for i in range(2):
            g = (2 - i) * 2.5
            glow.append(roundedRect(x0 - g, y0 - g, x1 + g, y1 + g, 11 + g, fill='', outline='', width=2.5))
        body = roundedRect(x0, y0, x1, y1, 11, width=1.5, tags=(tag,))
        # Lighter top half to fake the glossy gradient of the active pill
        gloss = roundedRect(x0 + 2, y0 + 2, x1 - 2, (y0 + y1) / 2.0 + 2, 9, fill='#2a86ff', outline='', tags=(tag,))
        label = c.create_text((x0 + x1) / 2.0, (y0 + y1) / 2.0, text=caption, tags=(tag,))
        return {'glow': glow, 'body': body, 'gloss': gloss, 'text': label}

    def styleButton(self, key, style):
        c = _gu._canvas
        btn = self.buttons[key]
        for item, colour in zip(btn['glow'], style['glow']):
            c.itemconfigure(item, outline=colour or '')
        c.itemconfigure(btn['body'], fill=style['fill'], outline=style['outline'])
        c.itemconfigure(btn['gloss'], state='normal' if style is BTN_ACTIVE else 'hidden')
        c.itemconfigure(btn['text'], fill=style['text'], font=(FONT, 12, "bold" if style is BTN_ACTIVE else "normal"))

    def onAlgoClick(self, key):
        _gu.set_clicked_algo(key)
        self.activeAlgo = key
        for k in self.buttons:
            self.styleButton(k, BTN_ACTIVE if k == key else BTN_IDLE)

    def onAlgoHover(self, key, entering):
        _gu._canvas.configure(cursor='hand2' if entering else '')
        if key != self.activeAlgo:
            self.styleButton(key, BTN_HOVER if entering else BTN_IDLE)

    def drawExpandedCells(self, cells):
        """Shade every cell the last search expanded, beneath the walls, dots and Pacman."""
        c = _gu._canvas
        if c is None: return
        for cell_id in self._expanded_cells:
            c.delete(cell_id)
        self._expanded_cells = []
        inset = self.gridSize * 0.06
        half = self.gridSize / 2.0 - inset
        for cell in cells:
            if isinstance(cell, tuple) and len(cell) >= 2:
                sx, sy = self.to_screen((cell[0], cell[1]))
                tile = c.create_rectangle(sx - half, sy - half, sx + half, sy + half, fill=EXPANDED_COLOR, outline='')
                if self.floorId is not None:
                    c.tag_raise(tile, self.floorId)
                self._expanded_cells.append(tile)

    def drawStaticObjects(self, state):
        layout = state.layout
        c = _gu._canvas
        self.walls = []
        if c is not None:
            mx1 = self.mazeLeft + self.width * self.gridSize
            my1 = self.mazeTop + self.height * self.gridSize
            self.floorId = c.create_rectangle(self.mazeLeft + self.gridSize / 2.0, self.mazeTop + self.gridSize / 2.0,
                               mx1 - self.gridSize / 2.0, my1 - self.gridSize / 2.0, fill=MAZE_FLOOR_COLOR, outline='')
            self.drawWalls(layout.walls)

        self.food = {}
        for x in range(layout.width):
            for y in range(layout.height):
                if state.food[x][y]:
                    self.food[(x, y)] = self.drawFood((x, y))

    def drawWalls(self, walls):
        """Walls are thick rounded bars joining neighbouring wall cells, layered for a neon glow."""
        c = _gu._canvas
        segments, dots = [], []
        for x in range(self.width):
            for y in range(self.height):
                if not walls[x][y]: continue
                linked = False
                if x + 1 < self.width and walls[x + 1][y]:
                    segments.append(((x, y), (x + 1, y))); linked = True
                if y + 1 < self.height and walls[x][y + 1]:
                    segments.append(((x, y), (x, y + 1))); linked = True
                hasLeft = x > 0 and walls[x - 1][y]
                hasDown = y > 0 and walls[x][y - 1]
                if not linked and not hasLeft and not hasDown:
                    dots.append((x, y))

        for frac, colour in WALL_LAYERS:
            w = self.gridSize * frac
            for a, b in segments:
                (ax, ay), (bx, by) = self.to_screen(a), self.to_screen(b)
                self.walls.append(c.create_line(ax, ay, bx, by, fill=colour, width=w, capstyle='round', joinstyle='round'))
            for d in dots:
                dx, dy = self.to_screen(d)
                self.walls.append(c.create_oval(dx - w / 2, dy - w / 2, dx + w / 2, dy + w / 2, fill=colour, outline=''))

    def drawFood(self, cell):
        sx, sy = self.to_screen(cell)
        g = self.gridSize
        return [circle((sx, sy), g * 0.2, FOOD_GLOW_COLOR, FOOD_GLOW_COLOR),
                circle((sx, sy), g * 0.13, FOOD_COLOR, FOOD_COLOR)]

    def drawAgentObjects(self, state):
        self.agentImages = []
        for agentState in state.agentStates:
            if agentState.isPacman:
                self.agentImages.append((self.drawPacman(agentState), agentState.copy()))

    def drawPacman(self, agentState):
        direction = agentState.getDirection()
        if direction == Directions.STOP:
            direction = Directions.EAST
        return pacmanShape(self.to_screen(agentState.getPosition()), self.gridSize * 0.42, direction)

    def update(self, state):
        # Redraw Pacman when it moves or turns, and clear any dots it has eaten.
        for i, agentState in enumerate([a for a in state.agentStates if a.isPacman]):
            ids, prev = self.agentImages[i]
            if prev.getPosition() != agentState.getPosition() or \
               (agentState.getDirection() != Directions.STOP and prev.getDirection() != agentState.getDirection()):
                for item in ids:
                    remove_from_screen(item)
                self.agentImages[i] = (self.drawPacman(agentState), agentState.copy())
        for cell in [cell for cell in self.food if not state.food[cell[0]][cell[1]]]:
            for item in self.food.pop(cell):
                remove_from_screen(item)
        self.infoPane.updateScore(state.score)
        sleep(self.frameTime)

    def finish(self):
        sleep(self.frameTime)

    def to_screen(self, point):
        (x, y) = point
        x = self.mazeLeft + (x + 0.5) * self.gridSize
        y = self.mazeTop + (self.height - y - 0.5) * self.gridSize
        return (x, y)

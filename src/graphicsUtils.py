# graphicsUtils.py
# ----------------
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


import sys
import time

try:
    import tkinter
except ImportError:
    try:
        import Tkinter as tkinter
    except ImportError:
        tkinter = None

_root_window = None
_canvas = None
_canvas_x = None
_canvas_y = None
_canvas_color = None

def formatColor(r, g, b):
    return '#%02x%02x%02x' % (int(r * 255), int(g * 255), int(b * 255))

BACKGROUND_COLOR = formatColor(0, 0, 0)

# Keyboard state
_keys_waiting = set()   # keys pressed since last call to keys_waiting()
_keys_held = set()      # keys currently held down

def keys_waiting():
    """Return keys pressed since the last call and clear the queue."""
    global _keys_waiting
    keys = _keys_waiting
    _keys_waiting = set()
    return keys

def keys_pressed():
    """Return the set of keys currently held down."""
    return _keys_held

def clear_keys():
    """Clear all key state."""
    global _keys_waiting, _keys_held
    _keys_waiting = set()
    _keys_held = set()

def _on_key_press(event):
    global _keys_waiting, _keys_held
    _keys_held.add(event.keysym)
    _keys_waiting.add(event.keysym)

def _on_key_release(event):
    global _keys_held
    _keys_held.discard(event.keysym)

_last_clicked_algo = None

def get_clicked_algo():
    global _last_clicked_algo
    algo = _last_clicked_algo
    _last_clicked_algo = None
    return algo

def set_clicked_algo(algo):
    global _last_clicked_algo
    _last_clicked_algo = algo

def begin_graphics(width=640, height=480, color=None, title=None):
    if color is None:
        color = BACKGROUND_COLOR
    global _root_window, _canvas, _canvas_x, _canvas_y, _canvas_color
    if tkinter is None:
        return
    try:
        _root_window = tkinter.Tk()
        _root_window.protocol('WM_DELETE_WINDOW', _destroy_window)
        _root_window.title(title or 'Pacman')
        _root_window.resizable(0, 0)

        _canvas = tkinter.Canvas(_root_window, width=width, height=height, background=color)
        _canvas.pack()
        _canvas_x = width
        _canvas_y = height
        _canvas_color = color
        _root_window.bind('<KeyPress>', _on_key_press)
        _root_window.bind('<KeyRelease>', _on_key_release)
        _root_window.focus_set()
    except Exception:
        _root_window = None
        _canvas = None

def _destroy_window():
    global _root_window
    if _root_window is not None:
        try:
            _root_window.destroy()
        except Exception:
            pass
        _root_window = None

def sleep(ms):
    if _root_window:
        try:
            _root_window.update_idletasks()
            _root_window.update()
        except Exception:
            pass
    time.sleep(ms / 1000.0)

def polygon(coords, outlineColor, fillColor=None, filled=1, smoothed=0, width=1):
    if _canvas is None: return
    try:
        c = []
        for x, y in coords:
            c.append(x)
            c.append(y)
        if not fillColor:
            fillColor = outlineColor
        if not filled:
            fillColor = ""
        return _canvas.create_polygon(c, outline=outlineColor, fill=fillColor, smooth=smoothed, width=width)
    except Exception:
        return None

def circle(pos, r, outlineColor, fillColor=None, endpoints=None, style='pieslice', width=1):
    if _canvas is None: return
    try:
        x, y = pos
        x0, y0 = x - r, y - r
        x1, y1 = x + r, y + r
        if not fillColor:
            fillColor = outlineColor
        if endpoints is None:
            return _canvas.create_oval(x0, y0, x1, y1, outline=outlineColor, fill=fillColor, width=width)
        else:
            start, end = endpoints
            return _canvas.create_arc(x0, y0, x1, y1, outline=outlineColor, fill=fillColor, start=start, extent=end - start, style=style, width=width)
    except Exception:
        return None

def text(pos, color, contents, font="Helvetica", size=12, style="normal", anchor="nw"):
    if _canvas is None: return
    try:
        x, y = pos
        return _canvas.create_text(x, y, fill=color, text=contents, font=(font, size, style), anchor=anchor)
    except Exception:
        return None

def changeText(id, newText, font=None, size=12, style="normal"):
    if _canvas is None: return
    try:
        _canvas.itemconfig(id, text=newText)
    except Exception:
        pass

def changeColor(id, newColor):
    if _canvas is None: return
    try:
        _canvas.itemconfig(id, fill=newColor)
    except Exception:
        pass

def remove_from_screen(id):
    if _canvas is None: return
    try:
        _canvas.delete(id)
    except Exception:
        pass


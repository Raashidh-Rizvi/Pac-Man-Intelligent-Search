# util.py
# -------
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
import inspect
import heapq
import random
import io


"""
 Data structures and useful functions for Pac-Man search problems.
"""

class FixedRandom:
    def __init__(self, seed=0):
        self.seed = seed

    def random(self):
        self.seed = (self.seed * 9301 + 49297) % 233280
        return self.seed / 233280.0

def manhattanDistance(xy1, xy2):
    "Returns the Manhattan distance between points xy1 and xy2"
    return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])

def nearestPoint(pos):
    """
    Finds the nearest grid point to a position (which may be a float tuple).
    """
    x, y = pos
    gridX = int(x + 0.5)
    gridY = int(y + 0.5)
    return (gridX, gridY)

def chooseFromDistribution(distribution):
    """
    Takes a Counter instance representing a distribution and returns a random choice.
    """
    if sum(distribution.values()) == 0:
        return None
    r = random.random()
    base = 0.0
    for key, value in distribution.items():
        base += value
        if r <= base:
            return key
    return list(distribution.keys())[0]

class Stack:
    "A container with a last-in-first-out (LIFO) queuing policy."
    def __init__(self):
        self.list = []

    def push(self, item):
        "Push 'item' onto the stack"
        self.list.append(item)

    def pop(self):
        "Pop the most recently added item from the stack"
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the stack is empty"
        return len(self.list) == 0

class Queue:
    "A container with a first-in-first-out (FIFO) queuing policy."
    def __init__(self):
        self.list = []

    def push(self, item):
        "Enqueue the 'item' into the queue"
        self.list.insert(0, item)

    def pop(self):
        "Dequeue the earliest enqueued item"
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the queue is empty"
        return len(self.list) == 0

class PriorityQueue:
    """
      Implements a priority queue data structure. Each inserted item
      has a priority associated with it and the client is usually interested
      in quick retrieval of the lowest-priority item in the queue. This
      data structure allows items to be inserted and removed efficiently.
    """
    def __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (priority, count, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0

    def update(self, item, priority):
        # If item already exists with higher priority, update its priority and rebuild the heap.
        for i, (p, c, it) in enumerate(self.heap):
            if it == item:
                if p <= priority:
                    return
                del self.heap[i]
                heapq.heapify(self.heap)
                break
        self.push(item, priority)

class PriorityQueueWithFunction(PriorityQueue):
    """
    Implements a priority queue with the same push/pop signature of the
    Queue and Stack classes. This class takes a function that maps
    an item to a priority before pushing it onto the queue.
    """
    def __init__(self, priorityFunction):
        self.priorityFunction = priorityFunction
        PriorityQueue.__init__(self)

    def push(self, item):
        "Adds an item to the queue with priority from priorityFunction"
        PriorityQueue.push(self, item, self.priorityFunction(item))

def raiseNotDefined():
    fileName = inspect.stack()[1][1]
    lineNum = inspect.stack()[1][2]
    method = inspect.stack()[1][3]
    print("*** Method not implemented: %s at line %s of %s" % (method, lineNum, fileName))
    sys.exit(1)

class Counter(dict):
    """
    A counter keeps track of counts for a set of keys.
    """
    def __getitem__(self, idx):
        self.setdefault(idx, 0)
        return dict.__getitem__(self, idx)

    def incrementAll(self, keys, count):
        for key in keys:
            self[key] += count

    def argMax(self):
        """
        Returns the key with the highest value.
        """
        if len(list(self.keys())) == 0: return None
        all = list(self.items())
        values = [x[1] for x in all]
        maxIndex = values.index(max(values))
        return all[maxIndex][0]

    def totalCount(self):
        """
        Returns the sum of counts for all keys.
        """
        return sum(self.values())

    def normalize(self):
        """
        Normalizes the counts such that the total sum equals 1.
        """
        total = float(self.totalCount())
        if total == 0: return
        for key in self.keys():
            self[key] = self[key] / total

    def copy(self):
        return Counter(dict.copy(self))

def lookup(name, namespace):
    """
    Get a method or class from any imported module from its name.
    Usage: lookup(functionName, globals())
    """
    dots = name.split('.')
    if len(dots) == 1:
        if name in namespace:
            return namespace[name]
        if hasattr(sys.modules[__name__], name):
            return getattr(sys.modules[__name__], name)
        return None

    moduleStr = '.'.join(dots[:-1])
    if moduleStr not in sys.modules:
        return None
    return getattr(sys.modules[moduleStr], dots[-1], None)

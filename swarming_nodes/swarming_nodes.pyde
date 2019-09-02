import random
from math import sqrt

# Notes
# Each node will do anything it can to stay away from a wall
# Each node will move towards the closest node (only if it's in front)

#### CONFIG ####
num_nodes = 10
win_size = (800,600)
nodes = []

#### Script ####

def getClosestNode(current_node):
    # copy the list to a new memory location
    nodes_instance = list(nodes)
    
    # sort the list in place
    nodes_instance.sort(key = lambda p: sqrt((p._x - current_node._x)**2 + (p._y - current_node._y)**2))
    
    # get the closest node
    return nodes_instance[-1]

def within(a, b, tolerance):
    return abs(a - b) < tolerance

def dist2vel(x1, y1, x2, y2):
    output = [0,0]
    
    if x2 < x1:
        output[0] = -1
    else:
        output[0] = 1
            
    if y2 < y1:
        output[1] = -1
    else:
        output[1] = 1
    
    return tuple(output)

class Node(object):
    _x = 0
    _y = 0
    
    _vx = 0
    _vy = 0
    
    # where the node wants to go if its locked
    _goal_x = 0
    _goal_y = 0
    
    def __init__(self, max_x, max_y):
        self._x = random.randint(0, max_x)
        self._y = random.randint(0, max_y)
        
        self._goal_x = random.randint(0, max_x)
        self._goal_y = random.randint(0, max_y)
    
    def computeMovement(self):
        # Find closest node
        closest = getClosestNode(self)
        
        # Calc velocity
        self._vx, self._vy = dist2vel(self._x, self._y, closest._x, closest._y)
            
        # Override this if node is within 20 of closest
        # Just use a random velocity 
        if  within(self._x, closest._x, 300) or within(self._y, closest._y, 300):
            self._vx, self._vy = dist2vel(self._x, self._y, self._goal_x, self._goal_y)
        
        # if  within(self._y, closest._y, 300):
        #     _, self._vy = dist2vel(self._x, self._y, self._goal_x, self._goal_y)
        
        # # Override this calculation with "self preservation" from walls
        if within(self._x, win_size[0], 10):
            self._vx = -1
        elif within(self._x, 0, 10):
            self._vx = 1
        
        if within(self._y, win_size[1], 10):
            self._vy = -1
        elif within(self._y, 0, 10):
            self._vy = 1
            
    
    def draw(self):
        # Handle velocity
        self._x += self._vx
        self._y += self._vy
        
        # Push graphics to screen
        fill(0,0,0)
        circle(self._x, self._y, 10)

#### Processing funcitons ####
def setup():
    size(win_size[0], win_size[1])
    
    for _ in range(num_nodes):
        nodes.append(Node(win_size[0], win_size[1]))
    
def draw():
    # Re-clear the screen
    background(255,255,255)
    
    # Iterate each node
    for node in nodes:
        # Handle node's movement
        node.computeMovement()
        
        # Re-draw node
        node.draw()
        

import random

#### CONFIG ####
num_nodes = 10
win_size = (800,600)

#### Script ####
class Node(object):
    _x = 0
    _y = 0
    
    def __init__(self, max_x, max_y):
        self._x = random.randint(0, max_x)
        self._y = random.randint(0, max_y)
    
    def computeMovement(self):
        pass
    
    def draw(self):
        fill(0,0,0)
        circle(self._x, self._y, 10)

nodes = []

#### Processing funcitons ####
def setup():
    size(win_size[0], win_size[1])
    
    for _ in range(num_nodes):
        nodes.append(Node(win_size[0], win_size[1]))
    
def draw():
    # Iterate each node
    for node in nodes:
        # Handle node's movement
        node.computeMovement()
        
        # Re-draw node
        node.draw()
        

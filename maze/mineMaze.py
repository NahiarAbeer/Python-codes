import sys
class Node():
    def __init__(self, action , parent , state):
        self.action = action
        self.parent = parent
        self.state =state
class StackFrontier():
    def __init__(self, frontier):
        self.frontier = frontier
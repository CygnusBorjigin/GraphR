from re import L
from typing import Tuple


class Node:
    def __init__(self, value, rho, activity=0):
        self.value = value
        self.rho = rho
        self.activity = activity
        self.active = False

    def receive(self, new_activity):
        self.activity = self.activity + new_activity
        
        if self.activity > self.rho:
            self.active = True

    def relax(self):
        self.activity = self.activity * 0.75

        if self.activity < self.rho:
            self.active = False

    def reset(self):
        self.activity = 0
        self.active = False
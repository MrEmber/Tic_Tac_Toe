
from lib2to3.pytree import convert
from queue import Empty
from tkinter import E

empty_tic_tac_template = """
                   |       |   
             {1}   |  {2}  |  {3}
          _________|_______|_______
                   |       |
             {4}   |  {5}  |  {6}
           ________|_______|_______
                   |       |  
             {7}   |  {8}  |  {9}
                   |       |
    """
tic_tac_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
class Tic_Tac_Data:
    def __init__(self):
        pass
    def __repr__(self):
        return empty_tic_tac_template
        return tic_tac_list 



class Tic_Tac_Moves():
    def _init__(self):
        pass
    def __repr__(self,move):
        pass
class Tic_Tac_Convert():
    pass
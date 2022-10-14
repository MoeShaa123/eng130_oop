
from reptile import Reptile

class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.forked_tongue = True

    def uses_tongue_to_smell(self):
        return("if I can touch it I can smell it aswell")

smart_Snake = Snake()
print(f"This function is called from current class {smart_Snake.uses_tongue_to_smell()}")
print(f"This function is called from parent class {smart_Snake.hunt()}")
print(f"This function is called from grand parent class {smart_Snake.breathe()}")


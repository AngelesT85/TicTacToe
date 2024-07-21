class Field:
    def __init__(self) -> None:
        self.field = [["" for _ in range(3)] for i in range(3)]
        self.image = "images/Field.png"

class Tic:
    def __init__(self) -> None:
        self.image = "images/Tic.png"
        self.comp_value = 1

class TacToe:
    def __init__(self) -> None:
        self.image = "images/TacToe.png"
        self.comp_value = 0

field = Field()
tic = Tic()
tactoe = TacToe()
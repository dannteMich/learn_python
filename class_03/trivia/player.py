class Player:
    
    def __init__(self, name: str):
        self._name = name
        self._score = 0

    def increase_score(self, amount: int):
        self._score += amount
    
    @property
    def score(self): 
        return self._score

    @property
    def name(self) -> int:
        return self._name



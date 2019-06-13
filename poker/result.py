

class Result:

    def __init__(self, type, hand, tie_breaker):
        self._type = type
        self._hand = hand
        self._tie_breaker = tie_breaker

    @property
    def type(self): return self._type

    @property
    def hand(self): return self._hand

    @property
    def tie_breaker(self): return self._tie_breaker

    @type.setter
    def type(self, value): self._type = value

    @hand.setter
    def hand(self, value): self._hand = value

    @tie_breaker.setter
    def tie_breaker(self, value): self._tie_breaker = value


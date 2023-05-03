class Negyzet:

    def __init__(self, oldal: float = 0):
        super().__init__()
        self.oldal: float = oldal

    def terulet(self) -> float:
        return self.oldal * self.oldal

    def kerulet(self) -> float:
        return 4 * self.oldal
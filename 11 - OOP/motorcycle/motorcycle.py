class Motorcycle:
    def __init__(self) -> None:
        super().__init__()
        self.manufacturer: str = None
        self.type: str = None                               
        self.model: str = None
        self.horsePower: int = 0                                            
        self.productionYear: int = 0  
        self.fuelConsumption: float = None
        self.cylinder: int = 0
        self.torgue: int = 0
                           
    def __str__(self) -> str:
        return f"{self.manufacturer} {self.model} ({self.productionYear})"
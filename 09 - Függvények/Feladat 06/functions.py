def calculateUnit(temperature: float, unit: str) -> float:

    if(unit == "K"):
        return temperature + 273
    elif (unit == "F"):
        return 9/5*temperature + 32
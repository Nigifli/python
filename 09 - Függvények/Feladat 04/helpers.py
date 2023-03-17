def color(q: str) -> str:
    value: int = len(q)
    return f"\033[38;2;{value};{value};{value}m{q}\033[0m"
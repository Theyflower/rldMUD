red = '31'
green = '32'
yellow = '33'
blue = '34'
magenta = '35'
cyan = '36'

def colored(text: str, color: str) -> str:
    return f"\033[{color}m{text}\033[0m"
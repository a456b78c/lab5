from colorama import Fore

class Cube:
    def __init__(self, size, color):
        self.size = size
        self.color = color
    
    def draw(self):
        colors = {
            'red': Fore.RED,
            'green': Fore.GREEN,
            'blue': Fore.BLUE,
            'yellow': Fore.YELLOW,
            'magenta': Fore.MAGENTA,
            'cyan': Fore.CYAN,
            'white': Fore.WHITE,
            'black': Fore.BLACK
        }
        cube_color = colors.get(self.color.lower(), Fore.WHITE)
        # ASCII Cube drawing logic
        t = v = h = int(self.size / 2)
        s, p, b, f, n = " ", cube_color + "+", cube_color + "|", cube_color + "/", "\n"
        l = p + (cube_color + "-") * (t * 4) + p
        S = s * (4 * t)
        k = s * h
        K = b + S + b
        r = (s * t) + s + l + n
        while t:
            r += (s * t) + f + (S + f + s * (h - t) + b) + n
            t -= 1
        r += l + (k + b) + n + ((K + k + b + n) * (v - 1)) + K + k + p + n
        while v:
            v -= 1
            r += K + (s * v) + f + n
        r += l
        return r
    def resize(self, scaling_factor):
        self.size = int(self.size * scaling_factor)

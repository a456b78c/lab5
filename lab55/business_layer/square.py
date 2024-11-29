from colorama import Fore

class Square:
    def __init__(self, size, color):
        self.size = size  # Висота квадрата
        self.width = size * 2  # Ширина, яка відповідає передній грані куба
        self.color = color

    @staticmethod
    def from_cube(cube):
        # Створюємо квадрат, який має ту ж висоту та подвійну ширину як передня грань куба
        return Square(size=cube.size, color=cube.color)

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
        square_color = colors.get(self.color.lower(), Fore.WHITE)
        square = ""
        # Верхній рядок квадрата
        square += square_color + "+" + "-" * self.width + "+" + "\n"
        # Бокові сторони квадрата
        for _ in range(self.size):
            square += square_color + "|" + " " * self.width + "|" + "\n"
        # Нижній рядок квадрата
        square += square_color + "+" + "-" * self.width + "+"
        return square

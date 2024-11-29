""" import sys
from colorama import Fore, init
init(autoreset=True)

class Command:
    def execute(self):
        pass

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

class Square:
    def __init__(self, size, color):
        self.size = size
        self.color = color

    @staticmethod
    def from_cube(cube):
        return Square(size=int(cube.size), color=cube.color)

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
        square += square_color + "+" + "-" * self.size + "+" + "\n"
        # Бокові сторони квадрата
        for _ in range(self.size):
            square += square_color + "|" + " " * self.size + "|" + "\n"
        # Нижній рядок квадрата
        square += square_color + "+" + "-" * self.size + "+"
        return square

class CommandLineInterface:
    def __init__(self):
        self.scene = []
        self.last_cube = None  # Останній створений куб

    def run(self):
        print("Welcome to the ASCII Art Generator!")
        while True:
            command = input("Enter a command (create/render/exit): ").lower()
            if command == "exit":
                print("Exiting the program.")
                sys.exit(0)
            elif command == "create":
                self.create_shape()
            elif command == "render":
                self.render_scene()
            else:
                print("Invalid command. Please enter 'create', 'render', or 'exit'.")

    def create_shape(self):
        shape_type = input("Enter shape type (cube/square): ").lower()
        if shape_type == "cube":
            self.create_cube()
        elif shape_type == "square":
            self.create_square()
        else:
            print("Invalid shape type. Please enter 'cube' or 'square'.")

    def create_cube(self):
        try:
            size = int(input("Enter the size of the cube: "))
            color = input("Enter the color of the cube (e.g., red, green, blue): ").lower()
            cube = Cube(size, color)
            self.scene.append(cube)
            self.last_cube = cube
            print("Cube created.")
        except ValueError:
            print("Invalid input for size. Please enter a numeric value.")

    def create_square(self):
        if not self.last_cube:
            print("No cube exists to create a square from. Please create a cube first.")
            return
        square = Square.from_cube(self.last_cube)
        self.scene.append(square)
        print("Square created as the front face of the last cube.")

    def render_scene(self):
        if not self.scene:
            print("No shapes to render. Please create shapes first.")
            return
        for shape in self.scene:
            print(shape.draw())
            print("\n")  # Додає відступ між фігурами

def main():
    cli = CommandLineInterface()
    cli.run()

if __name__ == "__main__":
    main()
 """
from presentation_layer.cli import CommandLineInterface

def main():
    cli = CommandLineInterface()
    cli.run()

if __name__ == "__main__":
    main()

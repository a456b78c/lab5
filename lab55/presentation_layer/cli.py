import sys
from business_layer.cube import Cube
from business_layer.square import Square
from persistent_layer.file_storage import FileStorage

class CommandLineInterface:
    def __init__(self):
        self.scene = []
        self.last_cube = None

    def run(self):
        print("Welcome to the ASCII Art Generator!")
        while True:
            command = input("Enter a command (create/render/save/resize/exit): ").lower()
            if command == "exit":
                print("Exiting the program.")
                sys.exit(0)
            elif command == "create":
                self.create_shape()
            elif command == "render":
                self.render_scene()
            elif command == "save":
                self.save_to_file()
            elif command == "resize":
                self.resize_shape()
            else:
                print("Invalid command. Please enter 'create', 'render', 'save', 'resize', or 'exit'.")

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
            print("\n")

    def resize_shape(self):
        if not self.scene:
            print("No shape to resize. Please create a shape first.")
            return

        try:
            scaling_factor = float(input("Enter the scaling factor for the current shape: "))
            current_shape = self.scene[-1]
            current_shape.resize(scaling_factor)
            print("Shape resized.")
        except ValueError:
            print("Invalid input. Please enter a numeric scaling factor.")        

    def save_to_file(self):
        file_name = input("Enter the file name to save the ASCII art (include .txt extension): ")
        FileStorage.save_to_file(self.scene, file_name)

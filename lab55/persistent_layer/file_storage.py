class FileStorage:
    @staticmethod
    def save_to_file(scene, file_name):
        if not scene:
            print("No shapes to save. Please create a shape first.")
            return
        try:
            with open(file_name, "w") as file:
                for shape in scene:
                    ascii_art = shape.draw()
                    file.write(ascii_art + "\n\n")
            print(f"ASCII art saved to {file_name}.")
        except Exception as e:
            print(f"Error saving to file: {e}")

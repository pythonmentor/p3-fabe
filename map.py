class Map:
    def __init__(self, filename):
        self.filename = filename
        self.structure = 0

    def load_maze(self):
        # loading a maze structure from the txt file
        with open(self.filename, "r") as f:
            level_structure = []

            for ligne in f:
                line_level = []
                for sprite in ligne:
                    if sprite != "\n":
                        line_level.append(sprite)
                level_structure.append(line_level)
            self.structure = level_structure

def main():
    map = Map("level.txt")
    map.load_maze()
    print(map.structure)

if __name__ == "__main__":
    main()
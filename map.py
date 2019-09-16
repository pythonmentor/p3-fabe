class Map:
    def __init__(self, filename):
        self.filename = filename
        self.structure = []

    def load_maze(self):
        # loading a maze structure from the txt file
        with open(self.filename, "r") as f:

            for ligne in f:
                line_level = list(ligne)
                line_level = line_level[:-1] # remove last character from line_level list
                self.structure.append(line_level)


def main():
    map = Map("level.txt")
    map.load_maze()
    print(map.structure)

if __name__ == "__main__":
    main()
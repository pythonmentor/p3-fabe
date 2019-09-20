class Map:
    def __init__(self, filename):
        self.filename = filename
        self.structure = []
        self.start = None
        self.finish = None

    def load_maze(self):
        # loading a maze structure from the txt file
        with open(self.filename, "r") as f:
            for ligne in f:
                line_level = list(ligne)
                line_level = line_level[:-1] # remove last character from line_level list
                self.structure.append(line_level)

    def load_hero(self):
        # define the initial position of MacGyver
        for n_ligne, ligne in enumerate(self.structure):
            for n_col, col in enumerate(ligne):
                if col == "d":
                    print("MacGyver")

    def load_guardian(self):
        # define the initial position of guardian
        for n_ligne, ligne in enumerate(self.structure):
            for n_col, col in enumerate(ligne):
                if col == "a":
                    print("guardian")

    """def load_guardian(self):
        for x in range(len(self.structure)):
	        for y in range(len(self.structure[x])):
                if y == "a":
                    print("guardian")"""

    def load_items(self):
        pass


  


    


    

def main():
    map = Map("level.txt")
    map.load_maze()
    map.load_hero()
    map.load_guardian()

if __name__ == "__main__":
    main()
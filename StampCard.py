from tabulate import tabulate

# TODO: Put the dependencies into a venv so that it's easy to install

class StampCard:
    # A stamp card for an establishment which contains a name and a capacity
    # Authors: Cody Antonio Gagnon & Chuan-Li Ojales Chang

    def __init__(self, card_name, stamp_capacity):
        self.card_name = card_name
        self.stamp_capacity = stamp_capacity

    def name(self):
        """
        Return the name of the stampcard
        """
        return self.card_name

    def capacity(self):
        """
        Return the capacity as a string.
        """
        return str(self.stamp_capacity)

    def print_stamps(self):
        stamps = []
        stamps_per_row = self.stamp_capacity / 2  # hardcoded rows for now...
        for x in range(1, 3):
            stamps.append(["X"] * stamps_per_row)
        print (tabulate(stamps, tablefmt="grid"))  # takes a list of lists or another tabular data type as the first argument, and outputs a nicely formatted table


oasis = StampCard("Oasis", 10)
print("Name: " + oasis.name() + ", Capacity: " + oasis.capacity())
oasis.print_stamps()

class StampCard:
    # A stamp card for an establishment which contains a name and a capacity
    # Authors: Cody Antonio Gagnon & Chuan-Li Ojales Chang

    def __init__(self, card_name, stamp_capacity):
        self.card_name = card_name
        self.stamp_capacity = stamp_capacity

    def name(self):
        return self.card_name

    def capacity(self):
        """
        Return the capacity as a string.
        """
        return str(self.stamp_capacity)

    def print_stamps(self):
        stamps = []
        for x in range(3, self.stamp_capacity):
            stamps.append(["X"] * self.stamp_capacity)
        for row in stamps:
            # concatenates each string
            print (" ".join([str(row)]))

    def stamp_row(self):
        return (1, len(self.stamp_capacity) - 1)

    def stamp_col(self):
        return (1, len(self.stamp_capacity) - 1)


oasis = StampCard("Oasis", 5)
print("Name: " + oasis.name() + ", Capacity in each row: " + oasis.capacity())
oasis.print_stamps()

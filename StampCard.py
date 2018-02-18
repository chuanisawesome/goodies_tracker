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
        for i in range(1, self.stamp_capacity):
            print("x")

oasis = StampCard("Oasis", 10)
print("Name: " + oasis.name() + ", Capacity: " + oasis.capacity())
oasis.print_stamps()

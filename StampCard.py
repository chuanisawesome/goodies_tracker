# -*- coding: utf-8 -*-
from tabulate import tabulate
import chardet

# TODO: Put the dependencies into a venv so that it's easy to install
# TODO: add the amount of stamps we currently have vs. the stamp_capacity


class StampCard:
    # A stamp card for an establishment which contains a name and a capacity
    # Authors: Cody Antonio Gagnon & Chuan-Li Ojales Chang

    def __init__(self, card_name, card_description, stamp_capacity,
                 stamp_symbol, redeemable_location):
        """
        Initialize the stamp card with a:
            name
            description
            capacity
            symbol for stamping
            location to be redeemed
        """
        self.name = card_name
        self.description = card_description
        self.stamp_capacity = stamp_capacity
        self.stamp_symbol = stamp_symbol
        self.location = redeemable_location

    def get_name(self):
        """
        Return the name of the stampcard
        """
        return self.name

    def get_description(self):
        """
        Return the description of the stampcard
        """
        return self.description

    def get_capacity(self):
        """
        Return the capacity as a string.
        """
        return str(self.stamp_capacity)

    def get_symbol(self):
        """
        Return the capacity as a string.
        """
        return self.stamp_symbol

    def get_location(self):
        """
        Return the redeemable location as a string.
        """
        return self.location

    def print_stamps(self):
        stamps = []
        stamps_per_row = self.stamp_capacity / 2  # hardcoded rows for now...
        for x in range(1, 3):
            sta = raw_input("Enter a stamp: ")                              # enters raw_input stamps from user
            stamps.append((chardet(sta)['encoding'], 'utf-8')) * stamps_per_row # is able to put unicode into the StampCard
        print (tabulate(stamps, tablefmt="grid").encode('utf8', 'replace'))  # takes a list of lists or another tabular data type as the first argument, and outputs a nicely formatted table


def main():
    stamp = unicode("🍭", 'utf8')
    oasis = StampCard("Oasis", "Bubble Tea", 10, stamp, "University District")
    print("Name: " + oasis.get_name() + ", Capacity: " + oasis.get_capacity())
    oasis.print_stamps()


main()

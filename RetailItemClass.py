from operator import inv


class RetailItem:
    def __init__(self, desc, inv, price):
        self.__item_description = desc
        self.__inventory_units = inv
        self.__unit_price = price

    def set_description(self, desc):
        self.__item_description = str(desc)

    def set_inventory(self, inv):
        self.__iventory_units = int(inv)

    def set_price(self, price):
        self.__unit_price = float(price)

    def get_description(self):
        return self.__item_description

    def get_inventory(self):
        return self.__inventory_units

    def get_price(self):
        return self.__unit_price

    def __str__(self):
        return (
            "Item Description: "
            + self.__item_description
            + ","
            + " Units of Inventory: "
            + str(self.__inventory_units)
            + ","
            + " Unit Price: $"
            + str(self.__unit_price)
        )

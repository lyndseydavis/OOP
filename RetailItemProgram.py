import RetailItemClass as r


def main():
    # create objects
    Item1 = r.RetailItem("Jacket", 12, 59.95)
    Item2 = r.RetailItem("Designer Jeans", 40, 34.95)
    Item3 = r.RetailItem("Shirt", 20, 24.95)

    # print objects
    print("Item #1 -- ", Item1)
    print("Item #2 -- ", Item2)
    print("Item #3 -- ", Item3)


main()

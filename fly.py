import InsectClass as i


def main():

    # create an object from the insect class
    my_insect = i.Insect()

    # Toss the coin.
    print("I am going to get the flight length ten times.")
    for count in range(10):
        my_insect.lenflight()
        # Display the insect len of flight
        print("The flight length is:", my_insect.get_flight())


# Call the main function.
main()

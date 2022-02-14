import CoinClass as c


def show_coin_status(coin_obj):
    print("This side of the coin is up:", coin_obj.get_sideup())


def flip(coin_obj):
    coin_obj.toss()


# create an instance of the object
my_coin = c.Coin()

# pre flip status - should be heads
show_coin_status(my_coin)
# flip 10 times and show status each time
for i in range(10):
    flip(my_coin)
    show_coin_status(my_coin)

class CellPhone:
    def __init__(self, mfg, model, retail):
        self.__manufact = mfg
        self.__model = model
        self.__retail_price = retail

    def set_manufact(self, mfg):
        self.__manufact = str(mfg)

    def set_model(self, model):
        self.__model = str(model)

    def set_retail_price(self, retail):
        self.__retail_price = float(retail)

    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retail_price

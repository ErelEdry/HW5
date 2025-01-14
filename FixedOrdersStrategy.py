class FixedOrdersStrategy:
    def __init__(self, lst_orders):
        self.__lst_orders = lst_orders
        self.__current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current_index < len(self.__lst_orders):
            current_orders = self.__lst_orders[self.__current_index]
            self.__current_index += 1
            return current_orders
        else:
            raise StopIteration
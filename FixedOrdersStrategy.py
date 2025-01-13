class FixedOrdersStrategy:
    def __init__(self, lst_orders):
        self.lst_orders = lst_orders
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < len(self.lst_orders):
            current_orders = self.lst_orders[self.current_index]
            self.current_index += 1
            return current_orders
        else:
            raise StopIteration
from ServingStrategy import ServingStrategy
from exceptions import OrderOutOfBoundsException


class LeastPatienceCustomerServingStrategy(ServingStrategy):
        def select_next_order(self, orders):
            if len(orders) == 0:
                raise OrderOutOfBoundsException()

            min_patience_id = min(orders.keys())
            min_patience = orders[min_patience_id][0].get_patience()

            for order_id, (customer, _) in orders.items():
                current_patience = customer.get_patience()
                if current_patience < min_patience:
                    min_patience = current_patience
                    min_patience_id = order_id

            return min_patience_id
from baskets.models import Basket
from orders.models import OrderProduct


def move_products_from_basket_to_order(
    basket_dict: dict,
    order_id: int,
) -> None:
    for product in basket_dict["products"]:
        OrderProduct(
            order_id=order_id,
            product_id=product["id"],
            quantity=product["quantity"],
            unit_price=product["unit_price"],
        ).save()


def clear_basket(basket_id: int) -> None:
    Basket.objects.filter(id=basket_id).first().basketproduct_set.delete(hard=True)

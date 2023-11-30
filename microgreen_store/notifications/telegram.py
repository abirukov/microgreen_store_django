import requests

from microgreen_store.settings import config
from orders.models import Order


def notify_about_order(order: Order) -> None:
    if config.admin_tg_id:
        text = prepare_text(order)
        send_message(config.admin_tg_id, text)


def prepare_text(order: Order) -> str:
    order_dict = order.as_dict()
    text = f"Сделан заказ № {order_dict["id"]} на сумму {order_dict["total"]} рублей\nТовары:\n"
    for product in order_dict["products"]:
        text += f"\t{product["title"]}: {product["quantity"]} шт. по {product["unit_price"]} руб.\n"
    return text


def send_message(chat_id: str, text: str) -> None:
    requests.post(
        'https://bot.green-beaver.ru/send_message',
        json={
            'chat_id': chat_id,
            'text': text,
        },
    )

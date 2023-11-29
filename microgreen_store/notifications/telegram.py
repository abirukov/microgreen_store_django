import requests

from microgreen_store.settings import config
from orders.models import Order


def notify_about_order(order: Order) -> None:
    if config.admin_tg_id:
        text = prepare_text(order)
        send_message(config.admin_tg_id, text)


def prepare_text(order: Order) -> str:
    return f'Сделан заказ № {order.id} на сумму {order.total} рублей\n {order.json()}'


def send_message(chat_id: str, text: str) -> None:
    requests.post(
        'https://bot.green-beaver.ru/send_message',
        json={
            'chat_id': chat_id,
            'text': text,
        },
    )

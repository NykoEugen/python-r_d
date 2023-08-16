from celery import shared_task
from purchases.models import Purchase
from users.models import User


@shared_task
def print_message():
    print(f'Some message')


@shared_task
def count_purchase(user_id):
    user = User.objects.get(id=user_id)
    purchases_count = Purchase.objects.filter(user=user).count()
    print(f"User ({user.username}) have {purchases_count} purchases")

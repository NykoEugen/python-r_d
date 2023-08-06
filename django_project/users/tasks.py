from celery import shared_task
from purchases.models import Purchase


@shared_task
def print_message(message):
    print(f'Some message: {message}')


@shared_task
def count_purchase(user_id):
    purchases_count = Purchase.objects.filter(user=user_id).count()
    print(f"User ({user_id}) have {purchases_count} purchases")

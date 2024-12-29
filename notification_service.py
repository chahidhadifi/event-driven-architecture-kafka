from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'order-topic',
    bootstrap_servers=['localhost:9092'],
    group_id='notification-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))  
)

def send_email(customer_id, order_id, total):
    print(f"Envoi d'un email à {customer_id} pour la commande {order_id} d'un montant de {total}MAD.")

for message in consumer:
    event = message.value
    send_email(event['customer_id'], event['order_id'], event['total'])

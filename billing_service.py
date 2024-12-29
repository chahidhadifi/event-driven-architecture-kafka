from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'order-topic',
    bootstrap_servers=['localhost:9092'],
    group_id='billing-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8')) 
)

def generate_invoice(order_id, total):
    print(f"Génération de la facture pour la commande {order_id} d'un montant de {total}MAD.")

for message in consumer:
    event = message.value
    generate_invoice(event['order_id'], event['total'])

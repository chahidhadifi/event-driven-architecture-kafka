from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'order-topic',
    bootstrap_servers=['localhost:9092'],
    group_id='inventory-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8')) 
)

def update_inventory(product_name, quantity):
    print(f"Mise à jour de l'inventaire : {product_name} - Quantité restante: {quantity}.")

for message in consumer:
    event = message.value
    update_inventory(event['product_name'], 100 - event['quantity'])

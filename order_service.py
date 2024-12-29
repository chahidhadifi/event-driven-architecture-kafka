from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8') 
)

def place_order(order_id, customer_id, product_name, quantity, price):
    event = {
        'order_id': order_id,
        'customer_id': customer_id,
        'product_name': product_name,
        'quantity': quantity,
        'price': price,
        'total': price * quantity
    }

    producer.send('order-topic', event)
    print(f"Commande passée : {event}")

place_order(101, 'customer123', 'Laptop', 1, 1000)
time.sleep(1)
place_order(102, 'customer456', 'Smartphone', 2, 500)

producer.flush()

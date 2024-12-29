# Event-Driven Architecture Demo

A demonstration of Event-Driven Architecture (EDA) using Apache Kafka and Python. This project implements a simple order processing system with multiple microservices communicating through Kafka events.

## Architecture Overview

The system consists of:

- An Order Service (Producer) that generates order events
- Three consumer services:
  - Notification Service: Sends email confirmations
  - Inventory Service: Updates product stock levels
  - Billing Service: Generates invoices
- Kafka broker for event distribution
- Zookeeper for Kafka cluster management

## Prerequisites

- Docker and Docker Compose
- Python 3.x
- pip (Python package manager)

## Quick Start

1. Clone the repository:

```bash
git clone https://github.com/chahidhadifi/event-driven-architecture-kafka.git
cd event-driven-architecture-kafka
```

2. Create and activate a virtual environment:

```bash
python -m venv env
source env/bin/activate  # For Linux/macOS
# or
env\Scripts\activate     # For Windows
```

3. Install dependencies:

```bash
pip install kafka-python
```

4. Start Kafka and Zookeeper:

```bash
docker-compose up -d
```

5. In separate terminal windows, start the consumer services:

```bash
python notification_service.py
python inventory_service.py
python billing_service.py
```

6. Run the order service to generate events:

```bash
python order_service.py
```

## Project Structure

```
.
├── docker-compose.yml
├── order_service.py
├── notification_service.py
├── inventory_service.py
├── billing_service.py
└── README.md
```

## Stopping the Services

To stop all services:

1. Stop the Python scripts using Ctrl+C in each terminal
2. Stop Kafka and Zookeeper:

```bash
docker-compose down
```

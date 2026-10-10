from datetime import datetime, timedelta

ORDERS_DB = {
    "ORD-101": {
        "order_id": "ORD-101",
        "customer_id": "CUST-01",
        "item_name": "Wireless Noise Cancelling Headphones",
        "status": "DELIVERED",
        "delivery_date": (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d"),
        "return_window_days": 7,
        "is_returnable": True,
        "return_status": "NONE",
        "shipping_address": "42 Market Street, New Delhi"
    },
    "ORD-102": {
        "order_id": "ORD-102",
        "customer_id": "CUST-02",
        "item_name": "Smart Fitness Band",
        "status": "SHIPPED",
        "delivery_date": None,
        "return_window_days": 7,
        "is_returnable": True,
        "return_status": "NONE",
        "shipping_address": "15 Park Avenue, Mumbai"
    },
    "ORD-103": {
        "order_id": "ORD-103",
        "customer_id": "CUST-01",
        "item_name": "Cotton T-Shirt (Pack of 3)",
        "status": "DELIVERED",
        "delivery_date": (datetime.now() - timedelta(days=20)).strftime("%Y-%m-%d"),
        "return_window_days": 7,
        "is_returnable": True,
        "return_status": "EXPIRED",
        "shipping_address": "42 Market Street, New Delhi"
    },
    "ORD-104": {
        "order_id": "ORD-104",
        "customer_id": "CUST-03",
        "item_name": "Ergonomic Gaming Mouse",
        "status": "PROCESSING",
        "delivery_date": None,
        "return_window_days": 7,
        "is_returnable": True,
        "return_status": "NONE",
        "shipping_address": "88 Mall Road, Patiala"
    }
}
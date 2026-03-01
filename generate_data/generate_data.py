import pandas as pd
from datetime import datetime
from pathlib import Path
import random

# Make random reproducible
random.seed(42)

# Output directory
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.parent / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

# --------------------
# Generate Customers
# --------------------
customers = pd.DataFrame({
    "customer_id": [f"C{i}" for i in range(1, 6)],
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "email": [f"user{i}@example.com" for i in range(1, 6)]
})

customers.to_csv(DATA_DIR / "customers.csv", index=False)

# --------------------
# Generate Orders
# --------------------
orders = pd.DataFrame({
    "order_id": [f"O{i}" for i in range(1, 21)],
    "customer_id": [f"C{random.randint(1, 5)}" for _ in range(20)],
    "order_date": pd.date_range(start="2024-01-01", periods=20, freq="D")
})

orders.to_csv(DATA_DIR / "orders.csv", index=False)

# --------------------
# Generate Shipments
# --------------------
statuses = ["shipped", "delivered"]

shipment_data = []
for i, order_id in enumerate(orders["order_id"], start=1):
    status = random.choice(statuses)
    shipped_at = datetime(2024, 1, 2) + pd.Timedelta(days=i)

    delivered_at = (
        shipped_at + pd.Timedelta(days=1)
        if status == "delivered"
        else None
    )

    shipment_data.append({
        "shipment_id": f"S{i}",
        "order_id": order_id,
        "status": status,
        "shipped_at": shipped_at,
        "delivered_at": delivered_at
    })

shipments = pd.DataFrame(shipment_data)
shipments.to_csv(DATA_DIR / "shipments.csv", index=False)
print("✅ CSV files successfully generated in:", DATA_DIR)
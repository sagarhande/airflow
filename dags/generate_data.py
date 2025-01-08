import pandas as pd
import random
from datetime import datetime, timedelta


if __name__=="__main__":
    # Parameters
    num_rows = 1000
    user_ids = range(1, 101)  # 100 users
    product_ids = range(1, 51)  # 50 products
    actions = ['view', 'click', 'purchase', 'cart_add']
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)

    # Generate random data
    data = {
        "interaction_id": range(1, num_rows + 1),
        "user_id": [random.choice(user_ids) for _ in range(num_rows)],
        "product_id": [random.choice(product_ids) for _ in range(num_rows)],
        "action": [random.choice(actions) for _ in range(num_rows)],
        "timestamp": [
            start_date + timedelta(days=random.randint(0, (end_date - start_date).days)) +
            timedelta(seconds=random.randint(0, 86399))
            for _ in range(num_rows)
        ],
    }

    # Create DataFrame
    interaction_data = pd.DataFrame(data)

    # Save to CSV
    file_path = "interaction_data.csv"
    interaction_data.to_csv(file_path, index=False)

    file_path

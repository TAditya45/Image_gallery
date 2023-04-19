import matplotlib.pyplot as plt
import pymongo
from collections import Counter

# Define colors for different statuses
COLORS = {'good': 'green', 'bad': 'red', 'pending': 'orange'}

# Specify the SKU ID to query
SKU_ID = "ABD12"

# Connect to the MongoDB server
with pymongo.MongoClient("mongodb://localhost:27017/") as client:
    # Select the database and collection
    db = client['product_id']
    collection = db['images']

    # Retrieve the data from MongoDB for the given SKU ID
    data = collection.find({'sku_id': SKU_ID})

    # Check if the cursor is empty
    if data.count() == 0:
        print(f"No images found in the database for SKU ID {SKU_ID}")
    else:
        # Count the number of images with each status
        statuses = Counter(d['status'] for d in data)

        # Create a bar chart showing the number of images with each status
        fig, ax = plt.subplots()
        ax.bar(statuses.keys(), statuses.values(), color=[COLORS.get(s, 'gray') for s in statuses.keys()])
        ax.set_title("Statuses for SKU ID {}".format(SKU_ID))
        ax.set_xlabel("Status")
        ax.set_ylabel("Count")

        # Display the chart
        plt.show()

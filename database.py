import pymongo
import os

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create a database and collection
db = client["product_id"]
collection = db["images"]

# Define the path to the images folder
images_folder = "./images/"

# Validate that the images_folder path exists
if not os.path.exists(images_folder):
    print("Error: images_folder path does not exist")
    exit()

# Get a list of all image file names in the folder
image_files = [f for f in os.listdir(images_folder) if os.path.isfile(os.path.join(images_folder, f))]

# Loop through the image files and insert them into the collection
for image_file in image_files:
    # Set the SKU ID and order ID for the image
    sku_id = "ABD12"
    order_id = image_file.split(".")[0]

    # Validate that the order_id is not already in the collection
    if collection.find_one({"sku_id": sku_id, "order_id": order_id}) is not None:
        print(f"Error: order ID {order_id} already exists for SKU ID {sku_id}")
        continue
    
    # Set the image path and read the image data
    image_path = os.path.join(images_folder, image_file)
    with open(image_path, "rb") as f:
        image_data = f.read()
    
    # Set the status for the image
    status = "good"
    if int(order_id) <= 10:
        status = "bad"
    elif int(order_id) > 20:
        print(f"Warning: order ID {order_id} for SKU ID {sku_id} has an unknown status")

    # Add the image path to the document
    document = {"sku_id": sku_id, "order_id": order_id, "status": status, "image_data": image_data, "image_path": image_path}
    collection.insert_one(document)

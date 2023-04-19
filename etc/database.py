# import necessary libraries
import pymongo
import os

# connect to MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017/")

# create database and collection
mydb = client["mydatabase"]
mycol = mydb["images"]

# specify the path to the directory containing the images
path = "/path/to/images/"

# loop through all the subdirectories and files in the specified directory
for root, dirs, files in os.walk(path):
    for file in files:
        # get the directory name as SKUID and file name as unit id
        skuid = os.path.basename(root)
        unit_id = os.path.splitext(file)[0]

        # get the full path of the image file
        image_path = os.path.join(root, file)

        # check if the image file has a red or green line
        with open(image_path, "rb") as f:
            image_data = f.read()
            if b"red line" in image_data:
                status = "bad"
            elif b"green line" in image_data:
                status = "good"
            else:
                status = "unknown"

        # insert the image information into the MongoDB collection
        mydict = {"skuid": skuid, "unit_id": unit_id, "status": status, "path": image_path}
        x = mycol.insert_one(mydict)
        print(x.inserted_id)

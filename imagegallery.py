import io
import pymongo
import tkinter as tk
from PIL import Image, ImageTk


# Constants and variables
SKUID = "ABD12"
IMAGE_SIZE = (200, 200)
NUM_IMAGES_PER_ROW = 4


# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.product_id
collection = db.images


class ImageGrid(tk.Frame):
    def __init__(self, master, images):
        super().__init__(master)

        self.images = images
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Create a scrollable frame
        canvas = tk.Canvas(self)
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Loop through the images and create a grid layout
        row = 0
        col = 0
        for i, image in enumerate(images):
            try:
                # Get the filename and extension of the image
                filename = image["order_id"]
                if "." in filename:
                    filename, extension = filename.split(".")
                else:
                    extension = ""

                # Open the image data as a PIL Image object and resize it
                with Image.open(io.BytesIO(image["image_data"])) as img_data:
                    img_data = img_data.resize(IMAGE_SIZE, Image.ANTIALIAS)

                    # Convert the PIL Image object to a Tkinter PhotoImage object
                    img = ImageTk.PhotoImage(img_data)

                    # Create a frame to hold the image and label
                    frame = tk.Frame(scrollable_frame)
                    frame.grid(row=row, column=col, padx=10, pady=10)

                    # Create a label with the image and add it to the frame
                    label = tk.Label(frame, image=img)
                    label.pack()

                    # Add a label with the filename and extension below the image
                    filename_label = tk.Label(frame, text=filename, font=("Helvetica", 10), fg="gray")
                    filename_label.pack(pady=(5, 0))
                    extension_label = tk.Label(frame, text=extension, font=("Helvetica", 8), fg="gray")
                    extension_label.pack()

                    # Add a colored line under the image based on the status
                    status = image["status"]
                    line_color = "green" if status == "good" else "red"
                    line = tk.Label(frame, bg=line_color, height=3)
                    line.pack(fill="x")

                    # Move to the next column and row
                    col += 1
                    if col == NUM_IMAGES_PER_ROW:
                        col = 0
                        row += 1

            except Exception as e:
                print("Error processing image {}: {}".format(image["order_id"], e))

        # Pack the scrollbar and canvas
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)


# Get all images with the SKUID
images = collection.find({"sku_id": SKUID})

# Create a Tkinter window
window = tk.Tk()
window.title("Images for SKUID {}".format(SKUID))

# Create the image grid
image_grid = ImageGrid(window, images)
image_grid.pack(fill="both", expand=True)


# Start the Tkinter main loop
window.mainloop()

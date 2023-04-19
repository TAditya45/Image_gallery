# desktop-gui-application


The project is a desktop application that provides a GUI for an image gallery and analytics gallery. It utilizes a MongoDB document type database to store preprocessed images from a local directory.


Project Documentation


Introduction:


        The project is a desktop application that provides a GUI for an image gallery and analytics gallery. The data presented in the application is sourced from a MongoDB database, which is populated with preprocessed images stored in the 'images' directory.

Files:


        main.py: The main file of the application that launches the GUI.

        database.py: A Python file that assumes all preprocessed images are present in the 'images' directory and creates a MongoDB database from them.

        imagegallery.py: A Python file that displays all images from the MongoDB database with a red or green line underneath each image to signify 'bad' or 'good' status.

        product_analytics.py: A Python file that displays product analytics data sourced from the MongoDB database.


MongoDB Database:


        The MongoDB database is structured as follows:

        sku_id: The SKU ID of the product associated with the image.

        order_id: The order ID of the product associated with the image.

        status: The status of the image - 'good' or 'bad'.

        image_data: The binary data of the image.

        image_path: The file path of the image.


To run this application 


    Here are the commands that need to be run to set up and run this repository:


Create a virtual environment (assuming you have Python 3 installed):

    python3 -m venv venv
    
    
Activate the virtual environment:

For Windows:

    venv\Scripts\activate

For Mac/Linux:

    source venv/bin/activate

Install the required packages:

    pip install -r requirements.txt

Run the GUI application:

    python main.py
    
    

Note: Before running the GUI application, make sure to set the correct path for the image directory in the database.py file.

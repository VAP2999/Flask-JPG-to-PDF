# Flask-JPG-to-PDF


This project provides a simple web application built using Flask, which allows users to upload a directory of `.jpg` images and generate a PDF containing those images. The PDF is generated dynamically using the ReportLab library, and it is saved as `output2.pdf`.

## Features

- Upload a directory containing `.jpg` images.
- Automatically converts all `.jpg` images from the directory into a single PDF.
- Uses the ReportLab library to generate the PDF.
- The images are placed in the PDF in the order they appear in the directory.

## Project Structure

```
/JPG-to-PDF-Converter
│
├── /templates
│   ├── index.html               # HTML template for the upload form
├── app.py                       # Flask app script
├── output2.pdf                  # Generated PDF (created when the POST request is made)
├── requirements.txt             # Required Python packages
└── README.md                    # This README file
```

## Installation

### Prerequisites
You need to have Python 3.x installed on your machine.

1. **Clone the repository**:
  

2. **Install dependencies**:
   Make sure to create a virtual environment and activate it (optional but recommended).

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

   Then install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install the required libraries**:
   This project uses `Flask`, `reportlab`, and `Pillow` libraries. You can install them using the `requirements.txt` file.

   ```bash
   pip install flask reportlab pillow
   ```

### Run the App

1. **Start the Flask application**:
   ```bash
   python app.py
   ```

   The application will run locally, and you can access it at `http://127.0.0.1:5000/`.

2. **Upload your JPG images**:
   - Open the application in your browser (`http://127.0.0.1:5000/`).
   - Upload the directory that contains the `.jpg` images you want to convert to PDF.

   Once the images are processed, a PDF will be generated with the images placed in order. The PDF will be saved as `output2.pdf` in the project folder.

### Usage

- Go to `http://127.0.0.1:5000/` in your browser.
- Select the folder containing `.jpg` files that you wish to convert to PDF.
- The app will process the images and generate a PDF named `output2.pdf`.

### API Endpoint

The application has one main endpoint for generating the PDF:

#### **POST `/generate_pdf`**

- **Parameters**: 
  - `image_directory`: Path to the folder containing the `.jpg` images.
  
- **Response**: 
  - A success message or an error message depending on the success or failure of the operation.

- **Example Request**:
  ```bash
  curl -X POST -F "image_directory=/path/to/your/images" http://127.0.0.1:5000/generate_pdf
  ```

- **Example Response**:
  ```json
  {
    "message": "SUCCESSFULLY"
  }
  ```

### Error Handling

The application checks for the following errors:

- **Missing `image_directory` field**: If the field is not present in the request, it will return a `400` status with a message: `"Missing image_directory field"`.
  
- **Invalid directory path**: If the specified directory does not exist, it will return a `404` status with the message: `"Image directory does not exist"`.

### Requirements

- Python 3.x or higher
- Flask
- ReportLab (for generating PDF)
- Pillow (for image processing)

All dependencies are listed in the `requirements.txt` file.

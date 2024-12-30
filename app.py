from flask import Flask, request, jsonify,render_template
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PIL import Image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    
    if 'image_directory' not in request.form:
        return jsonify({'error': 'Missing image_directory field'}), 400

    image_directory = request.form['image_directory']
    
    if not os.path.exists(image_directory):
        return jsonify({'error': 'Image directory does not exist'}), 404

    output_pdf_file = 'output2.pdf'

    image_files = [os.path.join(image_directory, filename) for filename in os.listdir(image_directory) if filename.endswith('.jpg')]

    image_files.sort()

    max_width = max_height = 0
    for image_file in image_files:
        img = Image.open(image_file)
        img_width, img_height = img.size
        max_width = max(max_width, img_width)
        max_height = max(max_height, img_height)

    c = canvas.Canvas(output_pdf_file, pagesize=(max_width, max_height))

    for image_file in image_files:
       
        img = Image.open(image_file)
        
        img_width, img_height = img.size

        c.drawImage(image_file, 0, 0, width=img_width, height=img_height)

        c.showPage()

   
    c.save()

    return "SUCCESSFULLLLY"

if __name__ == '__main__':
    app.run(debug=True)

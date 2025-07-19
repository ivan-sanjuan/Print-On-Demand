import pandas as pd
from flask import Flask, render_template, request
from specs.details import get_details

app = Flask(__name__)
@app.route('/generate', method=['POST'])

def generate_sku():
    
    trim_options, book_type_options, size_type_options, color_type_options, print_type_options = get_details()
    sku = None

    if request.method == 'POST':
        trim = request.form.get('trim_options')
        if all ([trim]):
            sku = f'{trim}'
    
    details = {
        'trim_options': trim_options,
        'sku': sku
    }
    
    return render_template('index.html',**details)
import pandas as pd
from flask import Blueprint, render_template, request
from app.option_utils import get_options

generate_bp = Blueprint('generate', __name__)
@generate_bp.route('/generate', methods=['GET', 'POST'])

def generate_sku():
    options = get_options()
    sku = None

    if request.method == 'POST':
        trim = request.form.get('trim_options')
        if trim:
            sku = f"{trim}" 
    
    options['sku'] = sku
    return render_template('index.html', **options)

from flask import Blueprint, render_template, request
from app.option_utils import get_options
import pprint

sku_bp = Blueprint('generate', __name__)
@sku_bp.route('/generate', methods=['GET', 'POST'])



def generate_sku():
    options = get_options()
    trim = request.form.get('trim_options')
    valid_trims = options['trim_options']
    if trim not in valid_trims:
        error = f"Invalid trim selection: {trim}"
    return render_template('index.html', error=error, **options)

                
        
    return render_template('index.html', test=test)
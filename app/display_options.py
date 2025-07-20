import pandas as pd
from flask import Blueprint, render_template, request
from app.option_utils import get_options

display_options_bp = Blueprint('display', __name__)
print("✅ display_options_bp loaded from display_options.py")

@display_options_bp.route('/', methods=['GET', 'POST'])
def display_options():
    options = get_options()
    return render_template('index.html', **options)


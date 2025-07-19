from flask import Flask, render_template
from specs.trim_size import get_trimSize
from specs.book_type import get_bookType
import json

app = Flask(__name__)
@app.route('/')

def index():
    trim_values = get_trimSize()
    book_type_values = get_bookType()
    trim_options = [
        entry['Trim Size Inches']
        for entry in trim_values
        if entry.get('Trim Size Inches') and isinstance(entry['Trim Size Inches'], str)]
    
    book_type_options = [
        entry['Book Type']
        for entry in book_type_values
        if entry.get('Book Type') and isinstance(entry['Book Type'], str)]
    
    return render_template('index.html', trim_options=trim_options, book_type_options=book_type_options)



if __name__ == '__main__':
    app.run(debug=True)
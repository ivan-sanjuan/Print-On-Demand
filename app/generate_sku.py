from flask import Blueprint, render_template, request
import pandas as pd
import pprint

sku_bp = Blueprint('generate', __name__)
df = pd.read_excel('specs/lulu-print-api-spec-sheet.xlsx', header=1)
@sku_bp.route('/generate', methods=['POST'])

def generate_sku():
    target_trim = request.form.get('trim_options')
    target_book_type = request.form.get('book_type_values')
    target_foil_type = request.form.get('foil_type_options')
    target_cover_type = request.form.get('cover1_options')  
    
    target_size_type = request.form.get('size_type_values')
    match_index = df[df['Trim Size Inches'] == target_trim].index
    if not match_index.empty:
        sku_value = df.loc[match_index[0], 'Trim SKU']
    else:
        print(f'{target_trim} not found.')
    
    target_color_type = request.form.get('color_type_values')    
    match_index = df[df['Color Type'] == target_color_type].index
    if not match_index.empty:
        color_value = df.loc[match_index[0], 'Color SKU']
    else:
        print(f'{target_trim} not found.')
        
    target_print_type = request.form.get('print_type_values')    
    match_index = df[df['Print Type'] == target_print_type].index
    if not match_index.empty:
        print_value = df.loc[match_index[0], 'Print SKU']
    else:
        print(f'{print_value} not found.')
        
    target_bind_type = request.form.get('bind_type_values')    
    match_index = df[df['Bind Type'] == target_bind_type].index
    if not match_index.empty:
        bind_value = df.loc[match_index[0], 'Bind SKU']
    else:
        print(f'{bind_value} not found.')
        
    target_paper_type = request.form.get('paper_type_values')    
    match_index = df[df['Paper Type'] == target_paper_type].index
    if not match_index.empty:
        paper_value = df.loc[match_index[0], 'Paper SKU']
    else:
        print(f'{paper_value} not found.')

    target_finish_type = request.form.get('finish_type_options')    
    match_index = df[df['Finish Type'] == target_finish_type].index
    if not match_index.empty:
        finish_value = df.loc[match_index[0], 'Finish SKU']
    else:
        print(f'{finish_value} not found.')

    combined_sku = f'{target_book_type}-{target_size_type}-{target_cover_type}-{target_foil_type}-{sku_value}{color_value}{print_value}{bind_value}{paper_value}{finish_value}'
        
    return render_template('index.html', message=combined_sku)
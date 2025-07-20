from specs.details import get_details

def get_options():
    print_details = get_details()
    trim_values = print_details[0]
    book_type = print_details[1]
    size_type = print_details[2]
    color_type = print_details[3]
    print_type = print_details[4]
    bind_type = print_details[5]
    paper_type = print_details[6]
    ppi_sku = print_details[7]
    finish_type = print_details[8]
    cover1_type = print_details[9]
    foil_type = print_details[10]
    trim_options = [
        entry['Trim Size Inches']
        for entry in trim_values
        if entry.get('Trim Size Inches') and isinstance(entry['Trim Size Inches'], str)]
    
    book_type_options = [
        entry['Book Type']
        for entry in book_type
        if entry.get('Book Type') and isinstance(entry['Book Type'], str)]
    
    size_type_options = [
        entry['Size Type']
        for entry in size_type
        if entry.get('Size Type') and isinstance(entry['Size Type'], str)]
    
    color_type_options = [
        entry['Color Type']
        for entry in color_type
        if entry.get('Color Type') and isinstance(entry['Color Type'], str)]
    
    print_type_options = [
        entry['Print Type']
        for entry in print_type
        if entry.get('Print Type') and isinstance(entry['Print Type'], str)]

    bind_type_options = [
        entry['Bind Type']
        for entry in bind_type
        if entry.get('Bind Type') and isinstance(entry['Bind Type'], str)]
    
    paper_type_options = [
        entry['Paper Type']
        for entry in paper_type
        if entry.get('Paper Type') and isinstance(entry['Paper Type'], str)]
    
    ppi_sku_options = [
        int(entry['PPI_SKU'])
        for entry in ppi_sku
        if entry.get('PPI_SKU') and isinstance(entry['PPI_SKU'], (int, float))]
    
    finish_type_options = [
        entry['Finish Type']
        for entry in finish_type
        if entry.get('Finish Type') and isinstance(entry['Finish Type'], str)]
    
    cover1_options = [
        entry['Cover Option 1']
        for entry in cover1_type
        if entry.get('Cover Option 1') and isinstance(entry['Cover Option 1'], str)]
    
    foil_type_options = [
        entry['Foil Type']
        for entry in foil_type
        if entry.get('Foil Type') and isinstance(entry['Foil Type'], str)]
    
    options = {
        'trim_options': trim_options,
        'book_type_options': book_type_options,
        'size_type_options': size_type_options,
        'color_type_options': color_type_options,
        'print_type_options': print_type_options,
        'bind_type_options': bind_type_options,
        'paper_type_options': paper_type_options,
        'ppi_sku_options': ppi_sku_options,
        'finish_type_options': finish_type_options,
        'cover1_options': cover1_options,
        'foil_type_options': foil_type_options
    }
    return {**options}
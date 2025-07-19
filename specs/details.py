import pandas as pd
import pprint

df = pd.read_excel('lulu-print-api-spec-sheet.xlsx', header=1)

def get_details():
    df_trim = df[['Trim Size Inches']].to_dict(orient='records')
    df_book_type = df[['Book Type']].to_dict(orient='records')
    df_size_type = df[['Size Type']].to_dict(orient='records')
    df_color_type = df[['Color Type']].to_dict(orient='records')
    df_print_type = df[['Print Type']].to_dict(orient='records')
    df_bind_type = df[['Bind Type']].to_dict(orient='records')
    df_paper_type = df[['Paper Type']].to_dict(orient='records')
    df_ppi = df[['PPI_SKU']].dropna().to_dict(orient='records')
    df_finish_type = df[['Finish Type']].to_dict(orient='records')
    df_cover1_type = df[['Cover Option 1']].to_dict(orient='records')
    df_foil_type = df[['Foil Type']].to_dict(orient='records')
    
    return df_trim, df_book_type, df_size_type, df_color_type, df_print_type, df_bind_type, df_paper_type, df_ppi, df_finish_type, df_cover1_type, df_foil_type

# test = get_details()

# pprint.pprint(test)
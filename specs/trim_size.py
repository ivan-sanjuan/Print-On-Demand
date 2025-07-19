import pandas as pd

def get_trimSize():
    df = pd.read_excel('lulu-print-api-spec-sheet.xlsx', header=1)
    df_trim = df[['Trim Size Inches']]
    
    return df_trim.to_dict(orient='records')
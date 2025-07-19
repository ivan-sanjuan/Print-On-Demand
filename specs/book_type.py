import pandas as pd

def get_bookType():
    df = pd.read_excel('lulu-print-api-spec-sheet.xlsx', header=1)
    df_trim = df[['Book Type']]
    
    return df_trim.to_dict(orient='records')
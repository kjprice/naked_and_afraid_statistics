import pandas as pd

from python.config import CSV_LOCAL_FILEPATH, ORIGINAL_LOCAL_FILEPATH

def load_original_data():
    return pd.read_excel(ORIGINAL_LOCAL_FILEPATH, skiprows=5)

def clean_column(column_name: str):
    return column_name.strip().lower().replace('.', '_').replace(' ', '_').replace('f_', 'female_').replace('m_', 'male_').replace('__', '_')
    

def clean_data(df_raw: pd.DataFrame) -> pd.DataFrame:
    df = df_raw[df_raw.Seq.notnull()].copy()
    df = df.convert_dtypes()

    column_map = {}
    for c in df.columns:
        column_map[c] = clean_column(c)
        # print(c)
    return df.rename(columns=column_map)

def save_data(df: pd.DataFrame):
  df.to_csv(CSV_LOCAL_FILEPATH, index=False)    

def compile_to_csv():
    print('Loading Excel Data')
    excel_data_raw = load_original_data()
    # print(excel_data_raw)
    print('Cleaning DataFrame')
    df = clean_data(excel_data_raw)
    print('Saving DataFrame To CSV')
    save_data(df)
    


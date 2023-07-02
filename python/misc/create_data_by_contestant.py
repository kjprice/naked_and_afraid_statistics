import pandas as pd

from python.config import CSV_COMPILED_LOCAL_FILEPATH, CSV_BY_CONTESTANT_LOCAL_FILEPATH

def load_compiled_data():
    return pd.read_csv(CSV_COMPILED_LOCAL_FILEPATH)

def clean_column(column_name: str):
    return column_name.replace('female_', '').replace('male_', '').replace('female', 'name').replace('male', 'name')
    
def get_columns_starting_with(df:pd.DataFrame, match_str: str):
    len_match = len(match_str)
    return [c for c in df.columns if c[:len_match] == match_str]
def get_common_columns(df:pd.DataFrame):
    return [c for c in df ]
def get_male_columns(df:pd.DataFrame):
    return get_columns_starting_with(df, 'male')
def get_female_columns(df:pd.DataFrame):
    return get_columns_starting_with(df, 'female')

def assert_columns_equal(all_columns, original_columns):
        if len(all_columns) == len(original_columns) and sorted(all_columns) == sorted(original_columns):
            return
        raise AssertionError('New columns are not the same')

def remove_gender_from_column_names(df:pd.DataFrame):
    pass
def set_columns_for_gender_contestant(df:pd.DataFrame, gender: str):
    df['gender'] = gender
    column_map = {}
    for c in df.columns:
        column_map[c] = clean_column(c)

    return df.rename(columns=column_map)

    
def clean_data(df_raw: pd.DataFrame) -> pd.DataFrame:
    df = df_raw

    male_columns = get_male_columns(df)
    female_columns = get_female_columns(df)

    common_columns = list(set(df.columns) - set(male_columns + female_columns))
    all_columns = male_columns + female_columns + common_columns
    assert_columns_equal(all_columns, df.columns)

    all_male_columns = common_columns + male_columns
    all_female_columns = common_columns + female_columns

    male_df = set_columns_for_gender_contestant(df_raw[all_male_columns].copy(), 'male')
    female_df = set_columns_for_gender_contestant(df_raw[all_female_columns].copy(), 'female')

    df = pd.concat([male_df, female_df])
    
    df = df.sort_values('seq')
    columns =['seq'] + [c for c in df.columns if c != 'seq']

    df = df.reindex(columns=columns)
    return df

def save_data(df: pd.DataFrame):
  df.to_csv(CSV_BY_CONTESTANT_LOCAL_FILEPATH, index=False)    

def compile_to_data_by_contestant():
    print('Loading Compiled Data')
    df_raw = load_compiled_data()
    print('Cleaning DataFrame')
    df = clean_data(df_raw)
    print('Saving DataFrame To CSV')
    save_data(df)
    


import os

DATA_DIR = os.path.join('data')

ORIGINAL_REMOTE_URL="https://mathscinotes.com/wp-content/uploads/2016/04/Blog_Referencev4.xlsx"
ORIGINAL_LOCAL_FILEPATH=os.path.join(DATA_DIR, 'original_data.xlsx')

CSV_COMPILED_FILENAME = 'naked_and_afraid_compiled_data.csv'
CSV_COMPILED_LOCAL_FILEPATH=os.path.join('.', CSV_COMPILED_FILENAME)

CSV_BY_CONTESTANT_FILENAME='naked_and_afraid_by_contestant.csv'
CSV_BY_CONTESTANT_LOCAL_FILEPATH=os.path.join('.', CSV_BY_CONTESTANT_FILENAME)

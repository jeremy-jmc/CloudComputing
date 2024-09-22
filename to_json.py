import pandas as pd
import fnmatch
import os, glob
from IPython.display import display


def csv_to_json(csv_file):
    df = pd.read_csv(csv_file, header=None)
    df.columns = ["alumno_id", "first_name", "last_name", "birthday", "street_address", "city", "state", "phone"]
    display(df)
    with open(csv_file.replace('athena', 'athena_json').replace('.csv', '.json'), 'w') as f:
        f.write(str(eval(df.to_json(orient='records'))[0]).replace("'", '"'))


os.makedirs('./athena_json', exist_ok=True)
csvs = glob.glob('./athena/*.csv')

for csv in csvs:
    csv_to_json(csv)
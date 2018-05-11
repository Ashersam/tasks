import pandas as pd
csv_input = pd.read_csv('file.csv')
csv_input['copied file'] = csv_input['Birds']
csv_input.to_csv('output.csv', index=False)


import pandas as pd
filename = 'AZGrid.xls'
df = pd.ExcelFile(filename)
print(df.sheet_names)
p = df.parse('Plants')
s = df.parse('Substations')
t = df.parse('Transmission')
print(p.keys())
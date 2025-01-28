import requests
import pandas as pd
import openpyxl

file = 'domains2.xlsx'

sheet1 = pd.read_excel(file, sheet_name=0)

ips_column = sheet1['Domains']

for ip in ips_column:
    print(ip)


#df = pd.DataFrame({
#    'Domain': []
#})
#print(df)
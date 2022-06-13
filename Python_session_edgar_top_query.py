import requests
import pandas as pd
import zipfile

## url parameter
url='http://www.sec.gov/dera/data/Public-EDGAR-log-file-data/2017/Qtrl/Log20170201.zip'

## Download the file from the server

file = requests.get(url)

## load the zip file
df_zip = pd.read_csv('Log20170201.zip',compression='zip') ## we can not test it so i used sample file in same format.

##Sample file
df=pd.read_csv('session_ip.csv') ## Columns: SessionIP, DocumentSize, Document no

#print(df) Create saperate dataframes for aggregation purpose
df3=df[['sessions','Document Size']].copy()
df5=df[['sessions','Document Number']].copy()

## aggregate and rank calculation for document size
df4=df3.groupby(['sessions'])['Document Size'].sum().reset_index()
#print(df4)
df4['rank']=df4['Document Size'].rank(ascending=False)
df4=df4.sort_values(by='rank',ignore_index=True)
df4=df4.head(10)
Print('This is output for top 10 sessions by total size')
print(df4)

## aggregate and rank calculation for document size
df6=df5.groupby(['sessions'])['Document Number'].sum().reset_index()
#print(df6)
df6['rank']=df6['Document Number'].rank(ascending=False)
df6=df6.sort_values(by='rank',ignore_index=True)
df6=df6.head(10)
Print('This is output for top 10 sessions by total document number')
print(df6)

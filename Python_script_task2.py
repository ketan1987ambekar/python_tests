import pandas as pd

##Sample file
df=pd.read_csv('example_data_v1.csv') 
## Columns: SessionIP, DocumentSize, Document no

#####Get the count of url and count of unique url information###########
#print(df) Create saperate dataframes for aggregation purpose
df2=df[['User_ID','URL']].copy()
df3=df[['User_ID','Action_time']].copy()
#print(df2)
## aggregate calculation for total url count
df4=df2.groupby(['User_ID'])['URL'].count().reset_index()
df4.rename(columns={'URL':'Count_Of_URL'}, inplace=True)
## aggregate calculation for total unique url count
df5=df2.groupby(['User_ID'])['URL'].nunique().reset_index()
df5.rename(columns={'URL':'Count_unique_URL'}, inplace=True)
#merging of the datasets
df6=pd.merge(df4,df5,on='User_ID')
#print(df6)

#### Get the session duration, session start time information ##############
#print(df) Create saperate dataframes for aggregation purpose
df7=df[['User_ID','Action_time']].copy()
#sort the time for each user
df7.sort_values(['Action_time'],ascending=True).groupby('User_ID')
#Get min session start time
df8=df7.groupby(['User_ID'])['Action_time'].min().reset_index()
df8.rename(columns={'Action_time':'session_start_time'}, inplace=True)
#Get max session end time
df9=df7.groupby(['User_ID'])['Action_time'].max().reset_index()
df9.rename(columns={'Action_time':'session_end_time'}, inplace=True)
#merge the dataframes
df10=pd.merge(df8,df9,on='User_ID')
df10['session_start_time']=pd.to_datetime(df10['session_start_time'])
df10['session_end_time']=pd.to_datetime(df10['session_end_time'])
df10['Session_duration']=(df10['session_end_time'] - df10['session_start_time'])

#print(df10)
df11=pd.merge(df10,df6,on='User_ID')
df12=df11[['User_ID','session_start_time','Session_duration','Count_Of_URL','Count_unique_URL']].copy()
print(df12)

df12.to_csv('output_test.csv', index=False)

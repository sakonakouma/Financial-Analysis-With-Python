import pandas as pd


df= pd.read_csv('election_data.csv')
df.head()


Total_vote=len(df.index)
Total_vote

ab=df.groupby(['Candidate'])

ab.count()

df1=ab.count().rename(columns={'Voter ID':'cast_vote'})
df1.head()

df2=df1.drop(columns='County')
df2.head()

df2['Percentage']=round(df2['cast_vote']/Total_vote*100, 2)
df2

df2.idxmax()

print (f"Winner is {df2['Percentage'][df2.idxmax()]}% ({df2.idxmax()})")

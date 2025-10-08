import pandas as pd

#read in file to dataframe
df = pd.read_csv("data/tuneindex.csv",encoding="latin-1")
pd.set_option("display.max_rows",100)

print(df.head()) #print first 5
print(df.tail()) #print last 5
print(df.shape) #prints (x,y)

print(df.columns) #prints out column names in df

for c in df.columns: # iterates through the columns and prints out the column names
    print(c)

print("info:")
print(df.info)

print(df.describe())

def print_df(df,count):
    for i, row in df.iterrows():
        print(row['title']) #print all titles
        if i == 50:
            break
        for c in df.columns: # iterates through the columns and prints out the column names
            print(row[c]) # get column names into array and for each of the names print row for column names?

def print_df1(df,count):
    rows = df.shape[0]
    for i in range(rows):
        print(df['title'][i])
        if i ==50:
            break

#print_df(df,100)

#print_df1(df,100)

reels = df[df['tune_type']== 'reel'] #going to creaete a new dataframe called reels select only select where tune_type is reel

print("reels")
print(reels.shape)

for i, row in reels.iterrows():
    print(f"{i}{row['title']}")


emin=df[df['key_sig']=='EMin'] # finding e minor tunes

maids = df[df['title'].str.contains("maid",case = False)]


print("maid tunes")
print(maids.shape[0])

for i,row in maids.iterrows():
    print(row['title'])

print("e minor tunes")
print(emin.shape[0])

#print_df1(reels,50)

popular_tunes = df[df['downloaded']>1000]

#print_df(popular_tunes,100)

sorted = df.sort_values('downloaded',ascending=False)

#for i,row in sorted.iterrows():
 #   print(f"{i}{row['title']}{row['downloaded']}")

print(sorted.head())

tunes_by_type = df.groupby("tune_type")

#print_df(sorted,10)


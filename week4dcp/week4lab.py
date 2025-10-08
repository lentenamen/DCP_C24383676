import pandas as pd

#read in file to dataframe
df = pd.read_csv("data/album.csv",encoding="latin-1")
#task 1.1
print(df.shape)

print(df.columns)

print("first 5:")
print(df.head())

print("last 5")
print(df.tail())


#task 1.2
print(df.describe())
print(df.info())

missing_count = df.isna().sum()
print(f"There are {missing_count.sum} values missing")

#task 1.3
unique_values = df['artist'].drop_duplicates()
#print("Unique values in column 'artist':", unique_values.tolist())

#task2

#task 2.1
df1 = pd.read_csv("data/albumtracktune.csv",encoding="latin-1")

print(df1.shape)

#task2.2

max_track = df1['track_num'].max()
print("Largest track:", max_track)

max_tune = df1['tune_num'].max()
print("Largest tune in a track:", max_tune)

#2.3

most_frequent_tune = df1['title'].value_counts().idxmax
print(most_frequent_tune)

#task 3.1
altan = df[df['artist']== 'Altan']
print("Altan has:")
print(altan.shape)
Martin = df[df['artist']== 'Martin Hayes']
print("Martin Hayes has:")
print(Martin.shape)
bothyband = df[df['artist']== 'The Bothy Band']
print("The Bothy Band has:")
print(bothyband.shape)

#task 3.2
tunes_album1 = df1[df1['album_id'] == 1]
print(f"Number of tuens {tunes_album1.shape[0]}")

print("tuens names",tunes_album1['title'].tolist())

#task 3.3

many_tune_tracks = df1[df1['tune_num'] >1]
print(f"number of multi tune tracks {many_tune_tracks.shape[0]}")

#task 4.1
df1.groupby('album_id').count()

#task 5.1
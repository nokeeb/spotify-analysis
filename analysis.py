import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

spotify_df=pd.read_csv('dataset.csv')
# print('columns:',spotify_df.columns)
# print('shape:',spotify_df.shape)
# print('info:',spotify_df.info())
# print(spotify_df[spotify_df.isnull().any(axis=1)])
#Found null track name at 65900 index, so I will get rid of it...
clean_df=spotify_df.drop(index=65900)
duplicates=clean_df.duplicated().sum()
#No duplicates found

clean_df['duration_minutes']=(((clean_df['duration_ms']/1000)/60))

#Top 10 tracks by duration(minutes)
# print(clean_df[['track_name','duration_minutes']].sort_values('duration_minutes',ascending=False).head(10).set_index('track_name'))

clean_df['popularity_category']=pd.cut(clean_df['popularity'],bins=[-1,33,66,100],labels=["Low",'Medium','High'])
popularity_by_genre=clean_df.groupby('track_genre')['popularity'].mean()

#Top 5 genres by popularity
top_5_genre=popularity_by_genre.sort_values(ascending=False).head(5)
# print(top_5_genre)

artists_unique=clean_df['artists'].drop_duplicates()
top_20_songs=clean_df.sort_values('popularity',ascending=False)[['track_name','popularity']].drop_duplicates().head(20).set_index('track_name')

#20 most popular tracks
# print(top_20_songs)

clean_df['artist']=clean_df['artists'].str.split(';')
df_exploded = clean_df.explode('artist')
popularity_by_artist=df_exploded.groupby('artist')['popularity'].mean()
top_20_artists_by_popularity=popularity_by_artist.drop_duplicates().sort_values(ascending=False).head(20)

#most popular artists(top 20 artists by average popularity)
# print(top_20_artists_by_popularity)

popularity=clean_df['popularity']

energy=clean_df['energy']
loudness=clean_df['loudness']
valence=clean_df['valence']
acousticness=clean_df['acousticness']
speechiness=clean_df['speechiness']

popularity_to_energy=popularity.corr(energy)
popularity_to_loudness=popularity.corr(loudness)
popularity_to_valence=popularity.corr(valence)
popularity_to_acousticness=popularity.corr(acousticness)
popularity_to_speechiness=popularity.corr(speechiness)

correlation_df=pd.DataFrame()
correlation_df['Feature']=['energy','loudness','valence','acousticness','speechiness']
correlation_df['Value']=[popularity_to_energy,popularity_to_loudness,popularity_to_valence,popularity_to_acousticness,popularity_to_speechiness]

# Popularity correlations
# print(correlation_df.sort_values('Value',ascending=False))

print(clean_df.groupby('popularity_category').count())
# Histogram of popularity (how many songs have Low,Medium or High popularity)
plt.hist(clean_df.popularity_category)
plt.xlabel('Popularity category')
plt.ylabel('No. of songs')
plt.title('Histogram of popularity')
plt.savefig('output/histogram_of_popularity.png')
plt.show()



# Top genres
sns.barplot(top_5_genre)
plt.xlabel('Genre')
plt.ylabel('Average popularity')
plt.title('Top genres')
plt.savefig('output/top_genres.png')
plt.show()

sample_df=clean_df.sample(2000)


# Scatter -> popularity vs danceability 
# Because of huge density (100k+ tracks), a sample of 2000 tracks from the dataset was used

sns.scatterplot(x='popularity',y='danceability',data=sample_df)
plt.title('Track popularity vs danceability')
plt.xlabel('Popularity')
plt.ylabel('Danceability')
plt.savefig('output/scatter_popularity_vs_danceability.png')
plt.show()

# # Scatter -> popularity vs energy
sns.scatterplot(x='popularity',y='energy',data=sample_df)
plt.title('Track popularity vs energy')
plt.savefig('output/scatter_popularity_vs_energy.png')
plt.show()


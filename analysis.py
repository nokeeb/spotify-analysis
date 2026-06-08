# importing needed libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

def main():
    BASE_DIR = Path(__file__).resolve().parent
    spotify_df = pd.read_csv(BASE_DIR / 'dataset.csv')

    # checking what we have
    # print('columns:',spotify_df.columns)
    # print('shape:',spotify_df.shape)
    # print('info:',spotify_df.info())
    # print(spotify_df[spotify_df.isnull().any(axis=1)])
    #Found null track name at 65900 index, so I will get rid of it...
    spotify_df=spotify_df.drop(index=65900)
    # duplicates=spotify_df.duplicated().sum()
    #No duplicates found

    spotify_df['duration_minutes']=(((spotify_df['duration_ms']/1000)/60))

    #Top 10 tracks by duration(minutes)
    # print(spotify_df[['track_name','duration_minutes']].sort_values('duration_minutes',ascending=False).head(10).set_index('track_name'))

    #defining a new column that has 3 values: Low, Medium and High, and the bins represent
    #the ranges of each category. -1 is used to avoid the first value (0) not being taken into consideration 
    spotify_df['popularity_category']=pd.cut(spotify_df['popularity'],bins=[-1,33,66,100],labels=["Low",'Medium','High'])
    popularity_by_genre=spotify_df.groupby('track_genre')['popularity'].mean()

    #Top 5 genres by popularity
    top_5_genre=popularity_by_genre.sort_values(ascending=False).head(5)
    # print(top_5_genre)

    
    top_20_songs=spotify_df.sort_values('popularity',ascending=False)[['track_name','popularity']]
    top_20_songs.drop_duplicates().head(20).set_index('track_name')

    #20 most popular tracks
    # print(top_20_songs)

    #here we are, for each song where we have multiple artists featuring,
    #spliting them into singular values in order to have more representative
    #data for getting the most popular artists
    spotify_df['artist']=spotify_df['artists'].str.split(';')
    df_exploded = spotify_df.explode('artist')
    popularity_by_artist=df_exploded.groupby('artist')['popularity'].mean()
    top_20_artists_by_popularity=popularity_by_artist.drop_duplicates()
    top_20_artists_by_popularity.sort_values(ascending=False).head(20)

    #most popular artists(top 20 artists by average popularity)
    # print(top_20_artists_by_popularity)

    popularity=spotify_df['popularity']

    energy=spotify_df['energy']
    loudness=spotify_df['loudness']
    valence=spotify_df['valence']
    acousticness=spotify_df['acousticness']
    speechiness=spotify_df['speechiness']

    pop_to_energy=popularity.corr(energy)
    pop_to_loudness=popularity.corr(loudness)
    pop_to_valence=popularity.corr(valence)
    pop_to_acousticness=popularity.corr(acousticness)
    pop_to_speechiness=popularity.corr(speechiness)

    #creating a new DataFrame that contains the correlations of popularity to the 
    #categories mentioned below
    correlation_df=pd.DataFrame()
    correlation_df['Feature']=['energy','loudness','valence','acousticness','speechiness']
    correlation_df['Value']=[pop_to_energy,pop_to_loudness,pop_to_valence,pop_to_acousticness,pop_to_speechiness]

    # Popularity correlations
    # print(correlation_df.sort_values('Value',ascending=False))

    # print(spotify_df.groupby('popularity_category').count())

    # Histogram of popularity (how many songs have Low,Medium or High popularity)
    plt.hist(spotify_df.popularity_category)
    plt.xlabel('Popularity category')
    plt.ylabel('No. of songs')
    plt.title('Histogram of popularity')
    plt.savefig(BASE_DIR / 'output' / 'histogram_of_popularity.png')
    plt.show()



    # Top genres
    sns.barplot(top_5_genre)
    plt.xlabel('Genre')
    plt.ylabel('Average popularity')
    plt.title('Top genres')
    plt.savefig(BASE_DIR / 'output' / 'top_genres.png')
    plt.show()


    def plot_hexbin(df1,df2,xlabel,ylabel,title):
        hb=plt.hexbin(df1,df2,gridsize=50)
        plt.colorbar(hb)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.savefig(BASE_DIR/'output'/f'hexbin_{xlabel}_vs_{ylabel}.png')
        plt.show()

    # Hexbin -> popularity vs danceability 
    plot_hexbin(spotify_df.popularity,spotify_df.danceability,'Popularity','Danceability','Track popularity vs danceability')


    # # Hexbin -> popularity vs energy
    plot_hexbin(spotify_df.popularity,spotify_df.energy,'Popularity','Energy','Track popularity vs Energy')
    
    
    #this allows safe imports
if __name__=='__main__':
    main()






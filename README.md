<img width="640" height="480" alt="hexbin_popularity_vs_danceability" src="https://github.com/user-attachments/assets/556f2442-c634-4cc1-8404-14076ff6b8a2" />
# Spotify Music Trends Analysis
Spotify Music Trends analysis. Taking a look at: song popularity, duration, danceability, energy and valence.

## Features
- Data analysis and exctraction
- Data visualization
- Report on the analysis performed

## Tech stack
- Python (Pandas)

## Dataset used
- Spotify Tracks Dataset from Kaggle


Great dataset with alot of data and most importantly, it is clean!

Link:  https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset

License:  http://opendatacommons.org/licenses/odbl/1.0/
## Graphs

-History of popularity:

<img width="640" height="480" alt="histogram_of_popularity" src="https://github.com/user-attachments/assets/c2459ed4-586c-4ab7-8108-0544cafe9db4" />

Track popularity vs danceability:

<img width="640" height="480" alt="hexbin_popularity_vs_danceability" src="https://github.com/user-attachments/assets/3b85e6f9-9f7d-4694-9669-f914ff8f59a0" />

Track popularity vs energy:

<img width="640" height="480" alt="hexbin_popularity_vs_energy" src="https://github.com/user-attachments/assets/8590d6c3-b021-48d0-84b8-62b518332f39" />

Top genres:

<img width="640" height="480" alt="top_genres" src="https://github.com/user-attachments/assets/f38031b1-4ba3-4cc2-91f3-a851b7579d52" />

All of the graphs here are included in the project files (output folder).

## Report
The feature that has the highest positive correlation with popularity is: Loudness (0.05) -> still pretty low

The Histogram of popularity shows us that as expected, high popularity songs tend to be rare.
The rate of highly popular songs is slightly over 6%.

We can also see that popular songs tend to be more danceable.

Most songs from the dataset are in the upper level of energy, but we can not see a clear correlation with popularity.The most popular songs are in all areas of energy.

Full report can be found in the project files (report.txt).

## How to install 
Requirements: see ```requirements.txt```

Run this command into a terminal of your choice to download:
```bash
git clone https://github.com/nokeeb/spotify-analysis
```
then:
```bash
pip install -r requirements.txt
python analysis.py
```



## Mission
Upgrading knowledge in Python, more precisely in:
- Pandas
- Matplotlib and Seaborn

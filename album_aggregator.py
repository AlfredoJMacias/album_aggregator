import requests
import pandas as pd

class AlbumAggregator:
    def __init__(self, sources):
        self.sources = sources

    def fetch_data(self):
        albums = []
        for source in self.sources:
            response = requests.get(source)
            albums.extend(response.json())
        return albums

    def process_data(self, albums):
        df = pd.DataFrame(albums)
        df['release_date'] = pd.to_datetime(df['release_date'])
        current_metrics = df[df['release_date'] >= '2024-01-01']
        return current_metrics

    def genre_popularity(self, albums):
        df = pd.DataFrame(albums)
        genre_counts = df['genre'].value_counts()
        return genre_counts

    def artist_comparison(self, albums, metric):
        df = pd.DataFrame(albums)
        artist_metrics = df.groupby('artist')[metric].mean().sort_values(ascending=False)
        return artist_metrics

    def save_data(self, data, filename):
        data.to_csv(filename, index=False)

# Example usage
# APIs sensored for security
if __name__ == "__main__":
    sources = ['API1', 'API2']
    aggregator = AlbumAggregator(sources)
    albums = aggregator.fetch_data()
    processed_data = aggregator.process_data(albums)
    genre_data = aggregator.genre_popularity(albums)
    artist_data = aggregator.artist_comparison(albums, 'rating')
    
    aggregator.save_data(processed_data, 'processed_albums.csv')
    aggregator.save_data(genre_data, 'genre_popularity.csv')
    aggregator.save_data(artist_data, 'artist_metrics.csv')

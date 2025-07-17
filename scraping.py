from google_play_scraper import reviews_all, Sort
import pandas as pd

def scrape_playstore_reviews(app_id, lang='id', count=1000):
    try:
        reviews = reviews_all(
            app_id,
            lang=lang,
            sort=Sort.NEWEST,
            count=count,
            filter_score_with=None
        )
        df = pd.DataFrame(reviews)
        df.to_csv(f'{app_id}_reviews.csv', index=False)
        print(f"Success! Saved {len(df)} reviews.")
        return df
    except Exception as e:
        print(f"Error: {e}")

# Contoh eksekusi
scrape_playstore_reviews('ajaib.co.id', count=10000)
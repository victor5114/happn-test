# Pre requisites

* Install Python 3.
* Create a GCP Project.
* Setup your local environment for working with GCP SDK.
* load the `events.csv` file into a new GCS bucket and adjust path in `load_csv.py` file.

> I used Application Default Credentials in order to quickly get started with the SDK.

# Comments

I strongly got inspired by [this blog][https://mac-blog.org.ua/bigquery-sessions/] and simply adjusted the query to get the requested results.

# Run script

From `SQL_OFFLINE` folder

1. `python load_csv.py`. This will create the `<GCP_PROJECT_ID>.sampledatasets.events` table.
2. Copy paste query.bq content into the bigquery console and run it. You should get the expected table results.
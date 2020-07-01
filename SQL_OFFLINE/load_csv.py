from google.cloud import bigquery

client = bigquery.Client()
dataset_id = 'sampledatasets'
uri = "gs://cloud-samples-data-test-happn/bigquery/events.csv"

dataset_ref = client.dataset(dataset_id)

job_config = bigquery.LoadJobConfig()
job_config.schema = [
    bigquery.SchemaField("Event_id", "STRING"),
    bigquery.SchemaField("created_ts", "TIMESTAMP"),
]
job_config.skip_leading_rows = 1
# The source format defaults to CSV, so the line below is optional.
job_config.source_format = bigquery.SourceFormat.CSV

load_job = client.load_table_from_uri(
    uri, dataset_ref.table("events"), job_config=job_config
)  # API request
print("Starting job {}".format(load_job.job_id))

load_job.result()  # Waits for table load to complete.
print("Job finished.")

destination_table = client.get_table(dataset_ref.table("events"))
print("Loaded {} rows.".format(destination_table.num_rows))
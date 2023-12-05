import functions_framework
from google.cloud import storage



# Triggered by a change in a storage bucket
@functions_framework.cloud_event
def hello_wom(cloud_event):
    try:

        data = cloud_event.data

        event_id = cloud_event["id"]
        event_type = cloud_event["type"]

        bucket = data["bucket"]
        name = data["name"]




        print(f"Bucket: {bucket}")
        print(f"File: {name}")
        
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket)
        blob = bucket.blob(name)
        blob.delete()

    except Exception as e:
        
        print(e)
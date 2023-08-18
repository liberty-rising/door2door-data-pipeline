import boto3
import datetime
import json

s3_client = boto3.client('s3')

SOURCE_BUCKET = 'de-tech-assessment-2022'
DEST_BUCKET = 'door2door-data-lake'
FOLDER_NAME = 'data'

def fetch_data_from_last_hour():
    """ 
    Generate the key for the last hour's data. 
    Assumes files in the source S3 bucket are stored in an hourly format.
    """
    last_hour = datetime.datetime.now() - datetime.timedelta(hours=1)
    file_key = last_hour.strftime('%Y/%m/%d/%H') + '.json' # adjusted to json format
    return file_key

def process_json_data(data):
    """
    Process JSON data and split based on entity type.
    Returns data separated by entity.
    """
    vehicles = []
    operating_periods = []

    for record in data:
        if record['on'] == 'vehicle':
            vehicles.append(record)
        elif record['on'] == 'operating_period':
            operating_periods.append(record)

    return vehicles, operating_periods

def lambda_handler(event, context):
    try:
        file_key = fetch_data_from_last_hour()
        
        # Fetch data from source bucket
        response = s3_client.get_object(Bucket=SOURCE_BUCKET, Key=F'{FOLDER_NAME}/{file_key}')
        raw_data = json.loads(response['Body'].read())

        vehicles, operating_periods = process_json_data(raw_data)

        # Save processed data to data lake
        s3_client.put_object(Bucket=DEST_BUCKET, Key=f'vehicles/{file_key}', Body=json.dumps(vehicles))
        s3_client.put_object(Bucket=DEST_BUCKET, Key=f'operating_periods/{file_key}', Body=json.dumps(operating_periods))
        
        print(f"Data from {file_key} processed and stored in {DEST_BUCKET}")

    except Exception as e:
        print(f"Error while fetching and processing data: {str(e)}")
        raise e

    return {
        'statusCode': 200,
        'body': f"Data from {file_key} processed and stored in {DEST_BUCKET}"
    }

# For local testing
if __name__ == '__main__':
    lambda_handler({}, {})

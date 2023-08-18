import boto3
import json
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, DateTime

s3_client = boto3.client('s3')
DEST_BUCKET = 'door2door-data-lake'
DATABASE_URL = "your_database_url"  # e.g. "postgresql://user:password@host/dbname"

engine = create_engine(DATABASE_URL)

metadata = MetaData()

# Define tables based on the given data structure
vehicles = Table('vehicles', metadata,
    Column('id', String, primary_key=True),
    Column('lat', Float),
    Column('lng', Float),
    Column('at', DateTime)
)

operating_periods = Table('operating_periods', metadata,
    Column('id', String, primary_key=True),
    Column('start', DateTime),
    Column('finish', DateTime)
)

def load_data_to_db(data, table):
    """ Load data to the corresponding RDS table """
    df = pd.DataFrame(data)
    df.to_sql(table, engine, if_exists='replace')  # You might want to change 'replace' depending on your needs

def lambda_handler(event, context):
    try:
        # Assuming you're passing the file_key in the event
        file_key = event['file_key']

        # Fetch vehicles data from data lake
        vehicles_data = s3_client.get_object(Bucket=DEST_BUCKET, Key=f'vehicles/{file_key}')
        load_data_to_db(json.loads(vehicles_data['Body'].read()), 'vehicles')

        # Fetch operating_periods data from data lake
        op_data = s3_client.get_object(Bucket=DEST_BUCKET, Key=f'operating_periods/{file_key}')
        load_data_to_db(json.loads(op_data['Body'].read()), 'operating_periods')
        
        print(f"Data from {file_key} loaded into RDS")

    except Exception as e:
        print(f"Error while loading data to RDS: {str(e)}")
        raise e

    return {
        'statusCode': 200,
        'body': f"Data from {file_key} loaded into RDS"
    }

# For local testing
if __name__ == '__main__':
    lambda_handler({'file_key': 'sample_key'}, {})

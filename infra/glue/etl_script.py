import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# Initialize the GlueContext and SparkContext
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

job = Job(glueContext)
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

job.init(args['JOB_NAME'], args)

# Data lake location (source)
data_lake_bucket = 'door2door-data-lake'
vehicles_data_source = f"s3://{data_lake_bucket}/vehicles/"
operating_periods_data_source = f"s3://{data_lake_bucket}/operating_periods/"

# Destination (processed data)
processed_data_bucket = 'door2door-processed-data'
vehicles_data_destination = f"s3://{processed_data_bucket}/vehicles/"
operating_periods_data_destination = f"s3://{processed_data_bucket}/operating_periods/"

# Extract data from S3 bucket
vehicles_df = spark.read.json(vehicles_data_source)
operating_periods_df = spark.read.json(operating_periods_data_source)

# Load transformed data back to another S3 location in Parquet format
vehicles_df.write.parquet(vehicles_data_destination, mode="overwrite")
operating_periods_df.write.parquet(operating_periods_data_destination, mode="overwrite")

job.commit()

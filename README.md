# door2door Data Lake & Warehouse Solution

This solution automates the process of fetching live position data of vehicles from an S3 bucket, storing it in a data lake, processing and extracting main events, and then storing the transformed data in a data warehouse.

## Table of Contents

- [Architecture Overview](#architecture-overview)
- [Prerequisites](#prerequisites)
- [Setup and Running](#setup-and-running)
- [Database Schema](#database-schema)
- [Docker Deployment](#docker-deployment)
- [Contributing](#contributing)

## Architecture Overview

1. **Lambda Fetcher**: Fetches data from the S3 bucket hourly.
2. **Lambda Loader**: Loads raw data into the data lake.
3. **Glue ETL**: Processes raw data and extracts meaningful events.
4. **SQL Database**: Stores processed data in a structured format for querying.

## Prerequisites

- AWS CLI configured with appropriate permissions.
- Docker and Docker Compose installed.
- PostgreSQL (or your chosen SQL database) installed and running.

## Setup and Running

### 1. AWS Setup

Before running the solution locally, ensure you have set up the necessary AWS resources and permissions. See `aws_setup_guide.md` for detailed AWS configurations.

### 2. Local Database Setup

Run the SQL script to set up your local database:

```bash
psql -U your_username -d your_database -a -f sql/db_setup.sql
```

### 3. Docker Deployment

Navigate to the main project directory and run:

```bash
docker-compose -f docker/docker-compose.yml up --build
```

This command builds the Docker image and starts the containerized application.

## Database Schema

Refer to `sql/db_setup.sql` for the database schema details.

## Docker Deployment

A `Dockerfile` and `docker-compose.yml` are provided for containerizing the solution. Use the Docker Compose commands above to build and run the application inside a Docker container.
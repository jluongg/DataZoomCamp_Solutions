import pandas as pd
from sqlalchemy import create_engine
import gzip

# PostgreSQL connection parameters
engine = create_engine('postgresql://postgres:postgres@localhost:5433/ny_taxi')

# Load and insert taxi zones
df_zones = pd.read_csv('taxi_zone_lookup.csv')
df_zones.to_sql('taxi_zones', engine, if_exists='replace', index=False)

# Load and insert trip data
# Read the gzipped CSV file
with gzip.open('green_tripdata_2019-10.csv.gz', 'rt') as f:
    df_trips = pd.read_csv(f)
    
# Insert into PostgreSQL
df_trips.to_sql('green_taxi_trips', engine, if_exists='replace', index=False, 
                chunksize=100000)  # Using chunks for better memory management

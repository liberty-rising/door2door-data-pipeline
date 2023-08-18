-- Drop tables if they exist (useful for re-running the script)
DROP TABLE IF EXISTS vehicles CASCADE;
DROP TABLE IF EXISTS operating_periods CASCADE;

-- Create the vehicles table
CREATE TABLE vehicles (
    id VARCHAR(255) PRIMARY KEY,
    lat FLOAT,
    lng FLOAT,
    at TIMESTAMP WITH TIME ZONE
);

-- Create the operating_periods table
CREATE TABLE operating_periods (
    id VARCHAR(255) PRIMARY KEY,
    start TIMESTAMP WITH TIME ZONE,
    finish TIMESTAMP WITH TIME ZONE
);

-- Indexes can be added based on query patterns. For instance, if you want to frequently query vehicles based on timestamps:
CREATE INDEX idx_vehicle_at ON vehicles(at);

-- Similarly, for operating_periods based on start and finish times:
CREATE INDEX idx_op_start ON operating_periods(start);
CREATE INDEX idx_op_finish ON operating_periods(finish);

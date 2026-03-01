-- Create database
CREATE DATABASE IF NOT EXISTS ecommerce_db;

-- Use database
USE ecommerce_db;

-- Create schemas
CREATE SCHEMA IF NOT EXISTS raw;
CREATE SCHEMA IF NOT EXISTS analytics;

-- Create orders table in raw schema
CREATE OR REPLACE TABLE raw.orders (
    order_id STRING,
    customer_id STRING,
    order_date DATE
);
-- Customers table
CREATE OR REPLACE TABLE raw.customers (
    customer_id STRING,
    name STRING,
    email STRING
);

-- Shipments table
CREATE OR REPLACE TABLE raw.shipments (
    shipment_id STRING,
    order_id STRING,
    status STRING,
    shipped_at TIMESTAMP,
    delivered_at TIMESTAMP
);
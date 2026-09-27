# Flight Delay and Operational Data Analysis Using Hadoop and Hive

## Overview

This project analyzes a large flight operations dataset to identify patterns in flight delays, cancellations, airports, airlines, monthly delays, and delay causes.

## Technologies Used

* Hadoop HDFS – distributed storage
* Apache Hive – data analysis using HiveQL
* Python – result visualization
* Pandas & Matplotlib – data processing and charts

## Dataset

The project uses the **2015 Flight Delays and Cancellations** dataset from the U.S. Department of Transportation, distributed through Kaggle.
Dataset link:- https://www.kaggle.com/datasets/usdot/flight-delays

The original `flights.csv` dataset was cleaned before being uploaded to HDFS for analysis.

## Analysis Performed

* Total flights by airline
* Average departure delay by airline
* Average arrival delay by airline
* Flight cancellations by airline
* Monthly average departure delay
* Airports with the highest number of delayed flights
* Delay causes

## Workflow

**Flight Dataset → Data Inspection → HDFS → Hive Table → HiveQL Analysis → Python Visualization → Results**

## Results

The analysis identified variations in delays and cancellations across airlines, airports, and months. Late aircraft, airline, and air-system delays accounted for the largest recorded delay minutes.

The CSV files in this repository are output files generated from the HiveQL queries and contain the results used for analysis and visualization. 
The original and cleaned large datasets are excluded from the repository due to their size.
Large raw datasets and the Python virtual environment are excluded from the repository.

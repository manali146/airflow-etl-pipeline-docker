# Data Extraction, Transformation, and Loading (ETL) Pipeline using Airflow

This project showcases an end-to-end data engineering pipeline built with Airflow, Docker. The pipeline extracts data from a .tsv file, performs transformation operations, and loads the transformed data into a CSV file.

## Project Overview

The goal of this project was to develop a robust and scalable ETL pipeline to process and analyze large datasets. By leveraging the power of Airflow and containerization with Docker, the pipeline ensures efficient data extraction, transformation, and loading.

## Technologies Used

- Airflow: A powerful open-source platform to programmatically author, schedule, and monitor workflows.
- Docker: A containerization platform that provides a consistent and isolated environment for running applications.

## Pipeline Steps

1. Data Extraction: The pipeline starts by extracting data from a .tsv file. The file is downloaded and processed using a custom Python script.

2. Data Transformation: Once the data is extracted, various transformation operations are applied. This includes handling missing values, removing duplicates, and filtering columns to ensure data quality and consistency.

3. Data Loading: The transformed data is then loaded into a CSV file. This file serves as a structured and easily accessible format for further analysis and visualization.

## Pipeline Orchestration with Airflow

Airflow provides a user-friendly interface to define and manage the ETL pipeline. The pipeline is represented as a Directed Acyclic Graph (DAG) with tasks that execute in a specific order. Airflow's scheduler ensures the automatic execution of tasks based on defined dependencies and schedules.

## Running the Pipeline

To run the pipeline, follow these steps:

1. Install Docker on your machine.

2. Clone the project repository from GitHub.

3. Build and start the Docker containers using the provided Docker Compose file.

4. Access the Airflow UI in your web browser and configure the necessary connections and variables.

5. Trigger the pipeline execution by enabling the DAG in the Airflow UI.

## Future Enhancements

This project serves as a solid foundation for further enhancements and scalability. Some potential future improvements include:

- Adding data validation and error handling mechanisms to ensure data integrity.
- Integrating with additional data sources and formats for a more diverse data pipeline.
- Implementing automated testing and monitoring to ensure pipeline reliability.

## Conclusion
This project demonstrates the power and flexibility of Airflow in orchestrating ETL pipelines. By leveraging Docker for containerization, the pipeline provides a reliable and scalable solution for processing and analyzing data.

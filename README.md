# AZ-Data-Engineering-End-to-End

This project demonstrates a complete end-to-end Azure Data Engineering solution, covering all stages from data ingestion to reporting. The platform is designed to handle data ingestion, transformation, storage, loading, and visualization using key Azure services.

### Project Overview
In this project, we’ll create a robust data platform using the following Azure tools:

- **Azure Data Factory** for seamless data ingestion
- **Azure Data Lake Storage Gen2** for scalable data storage
- **Azure Databricks** for data transformation
- **Azure Synapse Analytics** for data warehousing and loading
- **Microsoft Power BI** for data visualization and interactive reporting
- **Azure Active Directory (AAD)** and **Azure Key Vault** for secure access and governance

### Use Case
The objective is to build an end-to-end data solution by ingesting tables from an on-premises SQL Server database into Azure. Here’s the step-by-step flow:
1. **Data Ingestion**: Data is ingested using Azure Data Factory and stored in Azure Data Lake.
2. **Data Transformation**: Azure Databricks transforms the raw data into a clean, optimized format.
3. **Data Loading**: The transformed data is loaded into Azure Synapse Analytics for further analysis.
4. **Data Visualization**: Microsoft Power BI connects to Azure Synapse to create interactive dashboards for reporting and insights.
5. **Security and Governance**: Azure Active Directory (AAD) and Azure Key Vault ensure secure access and compliance through monitoring and governance.

This project provides a comprehensive demonstration of an end-to-end data engineering workflow in Azure, showcasing industry-standard practices for data integration, transformation, and reporting.


## Old Architecture
This legacy workflow is a streaming data processing pipeline for telecom probes, primarily focused on real-time ingestion, processing, anomaly detection, and storage.

### Workflow Summary:
1. **Data Ingestion**:
   - IoT telecom probes generate data, which is consumed by a **Kafka** consumer (using Java).

2. **Streaming Core Processing**:
   - Data from Kafka is processed and enriched in real-time using **Apache Spark** and Java. This forms the core of the streaming ingestion and processing layer.

3. **Anomaly Detection**:
   - The processed data is sent to a microservice for anomaly detection, built with **Spring Boot** (Java) and **Python**.

4. **Data Storage**:
   - Anomalies and processed data are stored in databases like **MariaDB** and **PostgreSQL** (with Citus extension for high availability).

5. **Analytics and Data Warehousing**:
   - Data is also forwarded to **Druid** and **StarRocks** for analytics and data warehousing purposes, enabling efficient querying and analysis.

This workflow enables real-time data processing, anomaly detection, and storage for analytical insights, leveraging a mix of streaming, storage, and analytics technologies.
![image](https://github.com/ThamerAissaoui/AZ-Data-Engineering-End-to-End/blob/main/OLD_WORKFLOW.png)

## Architecture 1
![image](https://github.com/ThamerAissaoui/AZ-Data-Engineering-End-to-End/blob/main/WORKFLOW_2.png)

1. Ingest Data from Event Hub/IoT Hub to Data Lake
Stream Analytics can be configured to read from Event Hub or IoT Hub as input, process the data (e.g., transformations, aggregations), and write directly to an Azure Data Lake Storage (ADLS) destination.
Stream Analytics handles real-time streaming and can output data directly in Parquet, JSON, or CSV format in Data Lake Storage, ready for further processing.
2. Process Data with Databricks
Azure Databricks can read the data stored in the Data Lake, transform it further if necessary (e.g., advanced aggregations, machine learning models), and prepare it for loading into Synapse.
Since Databricks is highly scalable and integrated with the Data Lake, it is well-suited for batch or micro-batch processing of the data stored by Stream Analytics.
3. Load Data into Synapse
Once the data is processed in Databricks, you can use Databricks connectors or Synapse’s native connectors to load it into Synapse tables.
This can be automated within Databricks itself, using notebooks and workflows, or even through Synapse pipelines if you’re using Synapse for orchestration.
4. Visualize Data in Power BI
With the data now in Synapse, Power BI can connect to the Synapse data warehouse as a source for reporting and visualization.

5. Expose Azure Synapse Data to External Systems
Azure Functions can expose an HTTP API endpoint for external systems like Tableau, Elasticsearch, or other BI tools to fetch processed data directly from Synapse.

HTTP Trigger Function: Acts as an API endpoint to query Synapse and return results.
Use Case: Integrate with external dashboards or search systems.
Example Code:

![image](https://github.com/user-attachments/assets/18789b90-528b-42ee-8f77-706f3ac2dd2d)


## Architecture 2
![image](https://github.com/ThamerAissaoui/AZ-Data-Engineering-End-to-End/blob/main/WORKFLOW.png)


## Architecture 3
![image](https://github.com/ThamerAissaoui/AZ-Data-Engineering-End-to-End/blob/main/WORKFLOW_DENODO.png)

1. Data Sources:
    - On-premises SQL Server
    - Azure Data Lake Storage (Parquet/JSON)
2. Data Virtualization Layer:
    - Denodo integrates data sources into a unified view for immediate access.
3. Transformation:
    - Lightweight transformations in Denodo (joins, filtering, calculations).
    - Heavy transformations in Databricks (e.g., machine learning, advanced analytics) by querying Denodo views.
4. Data Warehouse:
    - Azure Synapse queries Denodo to load aggregated or cleaned data into the warehouse.
5. Visualization:
Power BI queries either Denodo directly or Azure Synapse for dashboarding.

## Architecture 3
![image](https://github.com/ThamerAissaoui/AZ-Data-Engineering-End-to-End/blob/main/WORKFLOW_Fabric.png)

## Resources
![image](https://github.com/ThamerAissaoui/AZ-Data-Engineering-End-to-End/assets/36975418/4b6b2221-8859-44a1-8cd5-8ff1244a3a8b)

## Plan

### 1.	Azure Data Factory 
Setup integration runtime to connect the onpremises to the cloud:


![image](https://github.com/ThamerAissaoui/AZ-Data-Engineering-End-to-End/assets/36975418/fc810f0a-051d-4c86-915f-65fc7ec8281e)
![image](https://github.com/ThamerAissaoui/AZ-Data-Engineering-End-to-End/assets/36975418/9815ece8-8a5b-40d9-9297-f033a598b09f)
![image](https://github.com/ThamerAissaoui/AZ-Data-Engineering-End-to-End/assets/36975418/1124bc5d-73a6-4182-bdec-46f98655fb50)
![image](https://github.com/ThamerAissaoui/AZ-Data-Engineering-End-to-End/assets/36975418/a944f5ed-bd27-4238-a1cc-527f4ba03e28)
A pipeline that:
-	Copy all data from on premises to Azure DataLake storage (parquet Format)
-	Using Databricks to mount storage, do 2 steps cleanup and transformations (ETL)
  
        o	Keep the raw data in the bronze layer of Azure Data Factory:
   	
        o	Mount a silver storage to do 1st hand transformation and cleanup:
   	
        o	Mount a gold storage for a final transformation.
   	
        o	Bronze to Silver transformations
   	
        o	Silver to Gold transformations

  
![image](https://github.com/ThamerAissaoui/AZ-Data-Engineering-End-to-End/assets/36975418/e742cf19-4da8-4b35-8425-a7904ad5a68c)
![image](https://github.com/ThamerAissaoui/AZ-Data-Engineering-End-to-End/assets/36975418/a0963907-3be2-418d-8ec9-863f19520ffa)
![image](https://github.com/ThamerAissaoui/AZ-Data-Engineering-End-to-End/assets/36975418/7515e95f-a36f-4935-a1b7-39965146423b)

### 2.	Azure Synapse Analytics
![image](https://github.com/ThamerAissaoui/AZ-Data-Engineering-End-to-End/assets/36975418/2c594bd3-fde0-45d5-92bc-5d6c7ad8ea70)
![image](https://github.com/ThamerAissaoui/AZ-Data-Engineering-End-to-End/assets/36975418/aa4cd891-51a8-4859-a98e-1cb1de87b208)

### 3.  Microsoft Power BI
![image](https://github.com/ThamerAissaoui/AZ-Data-Engineering-End-to-End/assets/36975418/bc4d296e-e83d-4600-942d-e2a8d0c95a85)


### 4. Azure Devops
Inorder to automate the CI/CD pipilines we created and and linked am AZ devops repo to the databricks workspace to make sure all our code is synched between Dev and Prod:

Since Azure Data factory cannot pull notebooks directly from git repository created in the Databricks worspace, we decided to created a live folder always synched with main branch of azure devops and that contains all the latest code changes, Azure data factory will pull all the notebooks from that folder:
![image](https://github.com/user-attachments/assets/59d41eb2-1c0f-42a5-a8aa-82cf942193ca)
![image](https://github.com/user-attachments/assets/3b85c545-3867-4571-b41d-30508141e765)
![image](https://github.com/user-attachments/assets/f826d6aa-8818-4389-b7ca-24362fe9f216)


---

### Automating CI/CD Pipelines

In order to automate the CI/CD pipelines, we created and linked an Azure DevOps repository to the Databricks workspace. This ensures that all our code is synchronized between the Development (Dev) and Production (Prod) environments.
   
   `azure-pipelines.yml`:

   ```yaml
   trigger:
         - main
         -
   variables:
     - group: dbw-cicd-dev
   
     - name: vmImageName
       value: "windows-latest"
     - name: notebooksPath
       value: "notebook"
   
   pool:
     vmImage: $(vmImageName)
   
   stages:
   - template: templates/deploy-notebooks.yml
     parameters:
       stageId: "Deploy_to_Dev_Environment"
       env: "dev"
       environmentName: $(dev-environment-name)
       resourceGroupName: $(dev-resource-group-name)
       serviceConnection: $(dev-service-connection-name)
       notebooksPath: $(notebooksPath)
   ```



















 

# AZ-Data-Engineering-End-to-End

This is a complete End to End Azure Data Engineering Project. In this project we are going to create an end-to-end data platform right from Data Ingestion, Data Transformation, Data Loading and Reporting. The tools that are covered in this project are, 
1.	Azure Data Factory 
2.	Azure Data Lake Storage Gen2 
3.	Azure Databricks 
4.	Azure Synapse Analytics 
5.	Azure Key vault 
6.	Azure Active Directory (AAD) and 
7.	Microsoft Power BI
   
The use case for this project is building an end-to-end solution by ingesting the tables from on-premises SQL Server database using Azure Data Factory and then store the data in Azure Data Lake. Then Azure databricks is used to transform the RAW data to the most cleanest form of data and then we are using Azure Synapse Analytics to load the clean data and finally using Microsoft Power BI to integrate with Azure synapse analytics to build an interactive dashboard. 
Also, we are using Azure Active Directory (AAD) and Azure Key Vault for the monitoring and governance purpose.


## Architecture
![image](https://github.com/ThamerAissaoui/AZ-Data-Engineering-End-to-End/blob/main/WORKFLOW.gif)

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
![image](https://github.com/user-attachments/assets/139825cb-2bee-4fcd-84fd-f8b5144ebbf1)
![image](https://github.com/user-attachments/assets/3e069d5d-4868-47c2-8d15-dba483fd566e)

Since Azure Data factory cannot pull notebooks directly from git repository created in the Databricks worspace, we decided to created a live folder always synched with main branch of azure devops and that contains all the latest code changes, Azure data factory will pull all the notebooks from that folder:
![image](https://github.com/user-attachments/assets/59d41eb2-1c0f-42a5-a8aa-82cf942193ca)
![image](https://github.com/user-attachments/assets/3b85c545-3867-4571-b41d-30508141e765)
![image](https://github.com/user-attachments/assets/f826d6aa-8818-4389-b7ca-24362fe9f216)


---

### Automating CI/CD Pipelines

In order to automate the CI/CD pipelines, we created and linked an Azure DevOps repository to the Databricks workspace. This ensures that all our code is synchronized between the Development (Dev) and Production (Prod) environments.

#### Steps to Set Up CI/CD Pipeline Automation

1. **Create Azure DevOps Repository**:
   - Log in to your Azure DevOps account.
   - Create a new project or use an existing project.
   - Within the project, create a new repository where you will store your Databricks notebooks and code.

2. **Link Azure DevOps Repository to Databricks**:
   - In your Databricks workspace, navigate to the user settings.
   - Under the "Git Integration" section, select "Azure DevOps".
   - Authenticate with your Azure DevOps account and select the repository you created.

3. **Set Up Branching Strategy**:
   - Create branches for development (`dev`) and production (`prod`) in your Azure DevOps repository.
   - Follow a branching strategy that suits your workflow, such as feature branches, hotfix branches, etc.

4. **Configure CI/CD Pipelines**:
   - In Azure DevOps, navigate to the Pipelines section.
   - Create a new pipeline and link it to your repository.
   - Define the pipeline stages:
     - **Build Stage**: Validate and lint the code.
     - **Test Stage**: Run unit tests and integration tests.
     - **Deploy Stage**: Deploy the code to the Databricks workspace.
   
   Example `azure-pipelines.yml`:

   ```yaml
   trigger:
     branches:
       include:
         - dev
         - prod

   pool:
     vmImage: 'ubuntu-latest'

   stages:
   - stage: Build
     jobs:
     - job: Build
       steps:
       - script: echo "Building the project..."
         displayName: 'Build Stage'

   - stage: Test
     jobs:
     - job: Test
       steps:
       - script: echo "Running tests..."
         displayName: 'Test Stage'

   - stage: Deploy
     jobs:
     - job: Deploy
       steps:
       - script: echo "Deploying to Databricks..."
         displayName: 'Deploy Stage'
       - script: |
           # Add your deployment script here
           echo "Deployment script goes here"
         displayName: 'Databricks Deployment'
   ```

5. **Synchronize Code Between Dev and Prod**:
   - Ensure that changes in the `dev` branch are thoroughly tested before merging into the `prod` branch.
   - Use pull requests (PRs) to review and approve changes before they are merged into the `prod` branch.

6. **Monitor and Maintain**:
   - Regularly monitor the pipeline runs to ensure that they are successful.
   - Update the pipeline configuration as needed to adapt to changes in the project or workflow.

By following these steps, we ensure that our code is consistently and reliably synchronized between the Development and Production environments, facilitating efficient and error-free deployments.



















 

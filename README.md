Covid-19-Datapipeline
A data pipeline with Terraform, Prefect,Bigquery,Google cloud Storage (GCP), dbt,Looker and much more!

Description
Objective

The goal of this data engineering project is to construct a highly efficient and scalable data pipeline that leverages COVID-19 data from around the world for in-depth analysis. By utilizing industry-leading tools such as Prefect, Terraform, BigQuery, Google Cloud, dbt, and Looker, I aim to demonstrate the effectiveness of a well-designed pipeline in providing insights into the global COVID-19 situation.

Dataset
My dataset is publicly available and provided by Our World in Data

Tools & Technologies
Cloud - Google Cloud Platform

Infrastructure as Code software - Terraform

Orchestration - Prefect

Data Lake - Google Cloud Storage

Data Warehouse - BigQuery

Transformation - dbt

Data Visualization - Looker

Language - Python

Explanation of the tools
1. Terraform:

Terraform is an open-source infrastructure as code (IaC) tool that allows you to define and provision infrastructure resources in a declarative manner.

It enables data engineers to manage infrastructure across multiple cloud providers using a simple configuration language.

The advantages of using Terraform include: Infrastructure as code: Infrastructure is defined in code, making it version-controlled, reusable, and easily reproducible.

Cloud-agnostic: Terraform supports multiple cloud providers, allowing flexibility in choosing the best provider for your needs.

Scalability: Terraform provisions and manages infrastructure resources automatically, enabling easy scaling as data pipeline requirements grow.
2. Python:

Python is a popular programming language widely used in data engineering. Its simplicity, extensive libraries, and community support make it an ideal choice.
Python's advantages include:

Readability and versatility: Python's clean syntax and vast library ecosystem make it easy to develop, maintain, and extend data pipelines.

Interoperability: Python can seamlessly integrate with various tools, databases, and frameworks, allowing for flexible data processing and transformations.

Large developer community: Python has a massive community of data engineers and scientists, providing access to a wealth of resources and expertise.

3. Prefect:

Prefect is an open-source workflow automation tool designed to build, schedule, and monitor complex data pipelines.

It offers advantages such as:

Scalable task scheduling: Prefect simplifies the management of dependencies and parallel execution of tasks, enabling efficient processing of large datasets.

Monitoring and debugging: Prefect provides a user-friendly interface to visualize and monitor pipeline runs, making it easier to identify and resolve issues.

Integration capabilities: Prefect seamlessly integrates with various tools and frameworks, allowing for flexibility and extensibility in building data pipelines.

4. BigQuery

BigQuery is a fully managed serverless data warehouse provided by Google Cloud.

It offers a powerful platform for storing, querying, and analyzing large datasets.

Advantages of using BigQuery include:

Scalability and performance: BigQuery can handle massive datasets with high concurrency, making it suitable for fast and scalable data processing.

Cost-effective: BigQuery's pay-as-you-go pricing model eliminates the need for upfront infrastructure investment and provides cost optimization options.

Integration with Google Cloud ecosystem: BigQuery integrates seamlessly with other Google Cloud services, simplifying data pipeline development and management.

5. Google Cloud Storage:

Google Cloud Storage provides scalable and durable object storage for unstructured data.

Advantages of using Cloud Storage

Scalable storage: Cloud Storage allows the storage of large volumes of data and provides high availability and durability.

Integration with other GCP services: Cloud Storage integrates seamlessly with tools like BigQuery and Prefect, enabling efficient data movement and processing.

Security and access control: Cloud Storage offers robust security features and access controls, ensuring data protection and compliance.

6. dbt (data build tool):

dbt is an open-source tool designed for data transformation and orchestration.

It allows data engineers to define transformations and build data models.

Advantages include:

Modularity and reusability: dbt enables the creation of modular, maintainable, and reusable SQL transformations, making it easier to manage complex data transformations.

Version control and documentation: dbt integrates with version control systems and generates documentation automatically, ensuring transparency and reproducibility.

Collaboration and testing: dbt supports collaboration among data engineers, provides built-in testing capabilities, and helps ensure data quality.

7. Looker:

Looker is a modern data platform that provides business intelligence and analytics capabilities.
Advantages of using Looker

Self-service analytics: Looker's intuitive interface allows non-technical users to explore and visualize data, reducing the dependency on data engineers for ad hoc analysis.

Centralized data governance: Looker facilitates centralized data definitions and access controls, ensuring data consistency and security across the organization.

Customizable dashboards and reporting: Looker enables the creation of interactive dashboards and reports tailored to specific business needs, enhancing data-driven decision-making.

Architecture
alt text

Final Result
Click here to view the dashboard

QUESTIOINS

How much power has your on-site machine?

Is this the right database for your purpose? Size of the data?

What about your net-work? Any bottle-neck here?

How complex are your PowerBI reports? I have seen many BI analysts who build their reports solely on PowerBI, in particular they join data in PowerBI, instead of using the power of the database.

How many users and processes are using this replica in parallel?

Power BI query caching

Aggregated / Pre-computed tables rather using source / raw tables

Use DW services i.e BQ / Azure Synapse Analytics

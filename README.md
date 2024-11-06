Development of a Structured Database and Text Extraction System for Finance Professional Development Resources

## Problem Statement

The project aims to organize and streamline access to finance professional development resources. It involves compiling 224 refresher readings and topic outlines from the CFA Institute into two key datasets. These datasets will serve as tools for improving the skills of finance professionals. The end objective is to build an intelligent application that utilizes these datasets to offer personalized learning experiences for finance professionals.
## Project Goals

### 1. Web Scraping and Dataset Creation

- **Objective:** Extract information from the provided webpage starting with CFA Institute’s website.
- **Tools:** Utilize web scraping tools such as Beautiful Soup or Scrapy.
- **Output:** Structure the extracted data into a CSV file with the following schema: 
  `{Name of the topic, Year, Level, Introduction Summary, Learning Outcomes, Link to the Summary Page, Link to the PDF File}`.

### 2. PDF Extraction

- **Objective:** Extract text from the provided PDF files (Topic outlines).
- **Tools:** Use PyPDF2 and Grobid for text extraction.
- **Output:** Organize extracted text into text files following the naming convention:
  - `Grobid_RR_{Year}_{Level}_combined.txt`
  - `PyPDF_RR_{Year}_{Level}_combined.txt`


### 3. Database Upload

- **Objective:** Upload structured data from step 1 into a Snowflake database.
- **Tools:** Utilize SQLAlchemy for database interaction.


### 4. Cloud Storage Integration

- **Objective:** Upload structured data (CSV) and extracted text files (from both Grobid and PyPDF) into an AWS S3 bucket.
- **Tools:** Write a Python function for uploading data to AWS S3 bucket. Utilize SQLAlchemy to upload structured metadata (Grobid) into a Snowflake database.

## Technologies Used

[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.python.org/)
[![Snowflake](https://img.shields.io/badge/Snowflake-387BC3?style=for-the-badge&logo=snowflake&logoColor=light)](https://www.snowflake.com/)
[![Amazon S3](https://img.shields.io/badge/Amazon%20S3-569A31?style=for-the-badge&logo=amazon-s3&logoColor=white)](https://aws.amazon.com/s3/)
[![Beautiful Soup](https://img.shields.io/badge/Beautiful%20Soup-59666C?style=for-the-badge&logo=python&logoColor=blue)](https://www.crummy.com/software/BeautifulSoup/)
[![Grobid](https://img.shields.io/badge/Grobid-007396?style=for-the-badge&logo=java&logoColor=white)](https://github.com/kermitt2/grobid)





## Data Source

1. CFA Institute’s website . 
(https://www.cfainstitute.org/membership/professional-development/refresher-readings)

2. PDFs Provided
(https://github.com/BigDataIA-Spring2024-Sec1-Team4/Assignment2/tree/main/PDF_Extraction/Archive_2)

##  Prerequisites 


Prerequisites of Software for the Project: 

### 1. Python Environment
Ensure Python is installed on the system. The project is developed using the Python programming language.

### 2. Python Libraries
- **Requests_HTML**: For web scraping and interacting with dynamic elements on websites.
- **Beautiful Soup**: For parsing HTML content and extracting relevant information from web pages.
- **PyPDF2**: For extracting text from PDF files.
- **SQLAlchemy**: For interacting with databases using Python.
- **Boto3**: For interacting with AWS services such as S3.
- **Grobid**: For additional PDF text extraction capabilities.

### 3. Snowflake Account
Access to a Snowflake account is necessary for database operations. This includes creating databases, tables, and establishing connections.

### 4. AWS Account
Access to an AWS account is required for utilizing AWS S3 storage services.

### 5. Visual Studio Code
Integrated Development Environment (IDE) or text editor for writing and running Python scripts.

 
## Project Structure

```
Assignment2
├── Cloud_Integration
│   ├── Snowflake_Transfer_Metadata.ipynb
│   ├── Step4_Cloud_Integration.ipynb
│   └── requirements.txt
├── Database_Upload
│   ├── Step3_Database_Upload.ipynb
│   ├── requirements.txt
│   └── snowflake_sqlalchemy_output.ipynb
├── Diagrams
│   ├── Diagrams.py
│   └── workflow_diagram.png
├── PDF_Extraction
│   ├── Archive_2
│   │   ├── 2024-l1-topics-combined-2.pdf
│   │   ├── 2024-l2-topics-combined-2.pdf
│   │   └── 2024-l3-topics-combined-2.pdf
│   ├── GROBID
│   │   ├── txt
│   │   │   ├── Grobid_RR_2024-l1-topics-combined-2.grobid.tei_combined.txt
│   │   │   ├── Grobid_RR_2024-l2-topics-combined-2.grobid.tei_combined.txt
│   │   │   └── Grobid_RR_2024-l3-topics-combined-2.grobid.tei_combined.txt
│   │   └── xml
│   │       ├── 2024-l1-topics-combined-2.grobid.tei.xml
│   │       ├── 2024-l1-topics-combined-2_408.txt
│   │       ├── 2024-l2-topics-combined-2.grobid.tei.xml
│   │       ├── 2024-l2-topics-combined-2_408.txt
│   │       ├── 2024-l3-topics-combined-2.grobid.tei.xml
│   │       └── 2024-l3-topics-combined-2_408.txt
│   ├── PyPDF
│   │   ├── PyPDF_RR_2024-l1-topics-combined-2_combined.txt
│   │   ├── PyPDF_RR_2024-l2-topics-combined-2_combined.txt
│   │   └── PyPDF_RR_2024-l3-topics-combined-2_combined.txt
│   ├── Step2_PDF_Extraction.ipynb
│   ├── requirements.txt
│   └── scheduler.py
├── README.md
└── Webscrape
    ├── CSV
    │   └── extracted_updated.csv
    ├── Step1_Webscrapper.ipynb
    ├── requirements.txt
    └── webscrapper_script.py
```


## Architectural Diagram


![workflow_diagram](https://github.com/BigDataIA-Spring2024-Sec1-Team4/Assignment2/assets/114356265/cfcb481f-63ed-42ce-a0fc-2a84105eb70f)
## How to run Application locally


To run the application locally from scratch, follow these steps:

1. **Clone the Repository**: Clone the repository onto your local machine.

   ```bash
   git clone https://github.com/BigDataIA-Spring2024-Sec1-Team4/Assignment2
   ```

2. **Create a Virtual Environment**: Set up a virtual environment to isolate project dependencies.

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**: Activate the virtual environment.

   - **Windows**:

     ```bash
     venv\Scripts\activate
     ```

   - **Unix or MacOS**:

     ```bash
     source venv/bin/activate
     ```
     
4. **Host Grobid Server**: Open Docker Desktop and host the Grobid server. (Run this in a separate terminal)

   ```bash
    cd PDF_Extraction
    git clone https://github.com/kermitt2/grobid_client_python
    cd grobid_client_python
    python3 setup.py install
    docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.8.0
   ```

5. **Run the Notebook Script**: Execute the `scheduler.py` python script to run the application. This step automates the process and runs all notebooks one after the other (Remember to add your .env files)

   ```bash
   cd PDF_Extraction
   python scheduler.py
   ```

By following these steps, you will be able to run the application locally from scratch. Ensure that Docker Desktop is installed and running before hosting the Grobid server.
## Team Information and Contribution 

### GitHub Issues for Change Management
Utilizing GitHub Issues is essential for tracking modifications, feature requests, and bugs within the project. It serves as a centralized platform for documenting all project-related concerns, allowing for transparent collaboration, prioritization, and assignment of tasks to team members. This practice ensures that the project's progress is cohesive, organized, and accessible to all stakeholders, fostering an environment of open communication and continuous improvement.

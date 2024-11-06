#!/usr/bin/env python
# coding: utf-8

# In[2]:


from diagrams import Diagram, Cluster
from diagrams.programming.flowchart import Action, Database, Document, InputOutput
from diagrams.onprem.client import User
from diagrams.onprem.container import Docker
from diagrams.aws.storage import S3
from diagrams.saas.analytics import Snowflake
from diagrams.programming.language import Python, Bash
from diagrams.generic.storage import Storage
from diagrams.generic.database import SQL


# In[3]:


with Diagram("Workflow Diagram", show=False, direction="LR"):
    with Cluster("Step 1 - Web Scraping"):
        step1_start = Python("Python File")
        request_html = Action("Request_Html\n(Get all reading Links)")
        beautiful_soup = Action("BeautifulSoup\n(Extract data from each reading)")
        csv_file = Storage("CSV\n(Store data in CSV File)")

        step1_start >>  request_html  >>  beautiful_soup  >> csv_file

    with Cluster("Step 2 - PDF Extraction"):
        step2_start = Python("Python File")
        py_pdf = Action("PyPDF")
        txt_file_pypdf = Storage("TextFile\n(For each Pdf locally)")

        grobid_client = Docker("Grobid-Client\n(Running on Docker)")
        txt_file_grobid = Storage("TextFile\n(For each Pdf locally)")

        step2_start >> py_pdf >> txt_file_pypdf
        step2_start >> grobid_client >> txt_file_grobid

    with Cluster("Step 3 - Database Upload"):
        step3_start = Python("Python File")
        csv_from_step1 = Storage("CSV\n(From Step1)")
        snowflake_db = Snowflake("Snowflake Database")

        step3_start >> csv_from_step1 >> snowflake_db

    with Cluster("Step 4 - Cloud Storage Integration"):
        step4_start = Python("Python File")
        aws_s3 = S3("AWS S3 bucket")
        sqlalchemy = SQL("Utilize SQLAlchemy(Metadata)")
        TextFile = Storage("TextFile\n(From Step2)")

        step4_start >> TextFile >> aws_s3
        TextFile >> sqlalchemy >> snowflake_db

    with Cluster("Step 5 - Automation"):
        automation_script = Python("Python Script")
        automation_script >> step1_start >> step2_start >> step3_start >> step4_start


# In[ ]:





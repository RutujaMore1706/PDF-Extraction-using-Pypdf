import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import os
import subprocess

def check_grobid_server():
    print("Checking GROBID server status...")
    try:
        subprocess.check_output(['curl', '--fail', 'http://localhost:8070/api/isalive'])
        print("GROBID server is up and running.")
        return True
    except subprocess.CalledProcessError:
        print("GROBID server failed to start.")
        return False

def start_grobid_server():
    print("Starting GROBID Docker container...")
    subprocess.run(['docker', 'run', '-d', '--rm', '-p', '8070:8070', '--name', 'grobid_server', 'lfoppiano/grobid:0.8.0'])

def execute_notebook(notebook_path):
    print(f"Executing {notebook_path}...")
    with open(notebook_path, 'r', encoding='utf-8') as file:
        nb = nbformat.read(file, as_version=4)
        ep = ExecutePreprocessor(timeout=-1, kernel_name='python3')
        try:
            ep.preprocess(nb, {'metadata': {'path': os.path.dirname(notebook_path)}})
            with open(notebook_path, 'w', encoding='utf-8') as file:
                nbformat.write(nb, file)
            print("Successfully executed notebook.")
        except Exception as e:
            print(f"Failed to execute {notebook_path}: {e}")
            return False
    return True

# Start GROBID server and check if it's running
start_grobid_server()
if not check_grobid_server():
    os._exit(1)  # Exit if GROBID server is not running

# List of notebooks to run
notebook_paths = [
    "../Webscrape/Step1_Webscrapper.ipynb",
    "Step2_PDF_Extraction.ipynb",
    "../Database_Upload/Step3_Database_Upload.ipynb",
    "../Cloud_Integration/Step4_Cloud_Integration.ipynb"
]

# Execute each notebook in the list
for notebook_path in notebook_paths:
    if not execute_notebook(notebook_path):
        print("Halting further execution due to failure.")
        subprocess.run(['docker', 'stop', 'grobid_server'])
        os._exit(1)  # Exit script if notebook execution fails

# Optionally, stop the GROBID Docker container after execution
print("Stopping GROBID Docker container...")
subprocess.run(['docker', 'stop', 'grobid_server'])

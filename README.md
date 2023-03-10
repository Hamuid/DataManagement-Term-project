
# Project Charter

1. Project objectives
This project is to search the data of companies name which located in Toronto and have posted data scientist job in the last 7 days.

2. Project goal
The ultimate goal of this project is to experience the entire process from data collection to pre-processing, storage and query.

3. Project Scope
- Data scraping with scrapy from Linked in websites
- Data preprocessing with Python
- Database creation and table saving with SQLite client tool
- Load desired data with query statement of SQLite.

4. Project Duration
Three weeks

5. Team member
Hyunji Kang (Student ID: 20222110017)


---------------------------------------------------


# Description to how to run

Step 0. ERD (Entity Relationship Diagram)
Open the [~ERD.puml] files in the [erd] folder.
Press [Alt + D]. You can see the Preview of Diagram.


Step 1. Collect
Create a Python Virtual Environment : [python3 -m venv (Name of Virtual Environment)]
Activate the Python Virtual Environment : [(Name of Virtual Environment)\Scripts\activate.bat]
Install Scrapy using pip : [pip install Scrapy]
Install scrapy-fake-useragent : [pip install scrapy-fake-useragent]        # scrapy-fake-useragent randomly generates a UserAgent value.
Into our scrapy project directory : [cd src] and [cd basic-scrapy-project]
Run our spider : scrapy crawl linkedin_jobs

Save the output as a csv file : [scrapy crawl linkedin_jobs -o linkedin_jobs.csv -t csv]
Save the output as a json file : [scrapy crawl linkedin_jobs -o jobs.json -t json]

※ Move the [linkedin_jobs.csv] file to the [data] folder!

Step 2. Data Pre-processing
Open the [preprecess.py] in the [src] folder.
Install pandas using pip : [pip install pandas]
Executing 'preprocess.py' in the [src] folder creates 'preprocessed_jobs.csv' in the [data] folder.
'data_path_setting.py' is a module that sets the root of data to be preprocessed.


Step 3. Store
Install 'DB Browser for SQLite'
Create [jobs.db] with 'DB Browser for SQLite'
In the 'DB Browser for SQLite' : File - Import - Table from CSV file... - choose 'preprocessed_jobs.csv'


Step 4. Query
Install the SQLite extension in VScode.
Open the 'SQLite Query.sql' file in VS Code
Running the 'SQLite Query.sql' : [Ctrl + Shift + Q]

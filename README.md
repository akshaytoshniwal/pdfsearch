# PDF Search
## A simple Python script that searches only PDF documents when certain keywords are given as input.
#### To check the demo, follow the link: https://share.streamlit.io/akshaytoshniwal/pdfsearch/main/searchpdf.py


### Features of the SearchPDF tool are as listed below (operations the system can perform):
1. Search any keyword to look for a PDF
2. Search for maximum 100 pages and 100 results on a single page
3. By default, search will show 10 results for the first page.
4. You can click on the result and it will redirect you to the link and open the PDF
5. The total number of results per page may vary depending on their PDF and document attributes

### Language Requirements
1. Python, Version 3.7.3 or above
2. Streamlit, Version v0.82.0

### Pre-requisites libraries/packages
1. Streamlit - For building the web UI framework using the streamlit library
For installation: pip install streamlit

2. Requests - For fetching the data in real-time from a URL using the request library
Installed: import requests

3. bs4 - For parsing URL content using beautifulsoup library
For installation: pip install beautifulsoup

Note: Installation of these libraries will be requiring an internet connection

### Steps to run the code
Install all the libraires/packages as mentioned above
Open terminal in PyCharm or command prompt in windows/linux/mac (depending on your OS, the commands in the terminal will vary, please take a note of that)

Type the command, 'streamlit run filename.py'

Note: Here 'filename.py' is the name of the Python file that you create

### System used for running the code
This is to give you an idea about the system configuration
1. RAM 16GB DDR4
2. 256 GB SSD (make sure required space is available in your system in order to install the packages and run the code)
3. No dedicated GPU required

### To check the demo, follow the link: https://share.streamlit.io/akshaytoshniwal/pdfsearch/main/searchpdf.py

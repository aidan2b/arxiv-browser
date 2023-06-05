# ArXiv Paper Browser
This code provides a simple user interface for browsing and fetching papers from the ArXiv repository. It uses the Streamlit library for creating the user interface and various other libraries for data retrieval and processing.

Dependencies
dotenv: Used to load environment variables from a .env file.
streamlit: Used for creating the user interface.
arxiv: A Python wrapper for the ArXiv API.
pandas: Used for data manipulation and analysis.
re: Used for regular expression matching.
requests: Used for making HTTP requests to retrieve data.
bs4 (Beautiful Soup): Used for parsing HTML content.
json: Used for working with JSON data.
os: Used for interacting with the operating system.
Setup
Before running the code, make sure to install the required dependencies. You can install them using pip:

Copy code
pip install python-dotenv streamlit arxiv pandas requests beautifulsoup4
You also need to have a .env file in the same directory as the script, containing any necessary environment variables.

Usage
Import the required libraries and load the environment variables from the .env file.
Create an instance of the OpenAIEmbeddings class.
Retrieve the category taxonomy from the ArXiv website.
Parse the HTML content to extract the category code and name pairings.
Define a function fetch_data to fetch ArXiv data for a specific category.
Create a Streamlit user interface with a dropdown menu for selecting a category.
When the user clicks the "Fetch Papers" button, fetch the papers for the selected category using the fetch_data function.
Display the fetched papers in the user interface, including their title, authors, categories, summary, and a download button for the PDF.
Please note that this code assumes you have an OpenAI API key and have set it up properly in your environment. You may need to modify the code to provide your own API key or authentication method if necessary.

Feel free to explore and customize the code to suit your needs. Happy browsing!

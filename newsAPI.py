import os
import requests as rq
from datetime import datetime
import json

# Fetch data from the NewsData API
def fetchNews():
    # Get the current date
    current_date = datetime.now().strftime("%d-%m-%Y")
    
    # Create the folder if it doesn't exist
    folder_name = "daily News"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    # Create the filename with the current date
    filename = os.path.join(folder_name, f"RAW_news_of_{current_date}.txt")
    
    # Check if the file already exists
    if os.path.exists(filename):
        print(f"File {filename} already exists. Skipping API request to save credits.")
        return
    
    # Fetch data from the NewsData API
    response = rq.get("https://newsdata.io/api/1/latest?country=bd&apikey=pub_66733cfa81daa3c57c23d1b1e23527ed95274")

    # Check if the request was successful
    if response.status_code == 200:
        # Get the response text
        data = response.text
        
        # Write the data to a file
        with open(filename, "w", encoding="utf-8") as file:
            file.write(data)
        
        print(f"Data has been written to {filename}")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

# Parse the news data and extract specified keywords
def parseTheNewsData():
    current_date = datetime.now().strftime("%d-%m-%Y")
    raw_filename = os.path.join("daily News", f"RAW_news_of_{current_date}.txt")
    output_filename = os.path.join("daily News", f"news_of_{current_date}.txt")
    
    with open(raw_filename, "r", encoding="utf-8") as file:
        data = json.load(file)
    
    articles = data.get("results", [])
    
    with open(output_filename, "w", encoding="utf-8") as file:
        for article in articles:
            title = article.get("title", "N/A")
            description = article.get("description", "N/A")
            video_url = article.get("video_url", "N/A")
            source_name = article.get("source_name", "N/A")
            link = article.get("link", "N/A")
            
            file.write(f"Title: {title}\n")
            file.write(f"Description: {description}\n")
            file.write(f"Video URL: {video_url}\n")
            file.write(f"Source Name: {source_name}\n")
            file.write(f"Link: {link}\n")
            file.write("\n")
    
    print(f"Parsed data has been written to {output_filename}")

# Call the functions to fetch news and parse the data
fetchNews()
parseTheNewsData()
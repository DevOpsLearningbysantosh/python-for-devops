"""Module providing a function printing python version."""
import re
import requests

# Define the URL of the website you want to extract text from
website = "https://www.reuters.com"  # Replace with the URL of the website

# Send an HTTP GET request to the website
response = requests.get(website, timeout=5)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Define a regular expression pattern to match famous text
    # This is just an example pattern; you should customize it for your use case
    text_sample=input()
    PATTERN = rf"{text_sample}"

    # Extract text from the HTML content using the regular expression
    famous_text_matches = re.findall(PATTERN, response.text)

    # Display the extracted famous text
    if famous_text_matches:
        for match in famous_text_matches:
            print("Famous Text:", match)
    else:
        print("Famous text not found on the website.")
else:
    print("Failed to retrieve the website. Status code:", response.status_code)

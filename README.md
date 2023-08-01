# Web Scraping Program

This program automatically extracts selected information from specified web pages.

## Table of Contents
- [General Info](#general-info)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Testing](#testing)
- [Solutions](#solutions)
- [Future Plans](#future-plans)
- [Inspirations and Acknowledgments](#inspirations-and-acknowledgments)

## General Info
This is an Amazon Web Scraping Program that automatically extracts selected information from specified web pages. It is built in Python and uses the lxml library for parsing HTML and the requests library for making HTTP requests to the web pages. The program takes a URL and an XPath expression as input and returns the extracted text based on the provided XPath.

## Features
- Automatically extracts information from web pages using XPath expressions.
- Customizable: You can specify the URL and XPath according to your requirements.

## Technologies Used
The program is written in Python.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Prerequisites
To run this project, make sure you have Python 3.11.2 installed on your computer.

## Setup
To run the project locally, follow these steps:

- Clone this repository to your local machine.
- Navigate to the project directory.
- Run the program:
```
python3 web_scraping_program.py [URL] [XPath]
```

## Testing
To ensure the correctness of the `web_scraping_program.py` module, I have created a test suite in `test_web_scraping_program.py` using pytest. 
These tests cover various scenarios, including valid content with matching XPath expressions, invalid XPath expressions, no matches for XPath expressions, handling None content, nested elements, and whitespace cleanup.

### Running Tests
To run the tests, follow these steps:

1. Install pytest if you haven't already, by:
``` 
pip3 install pytest
```
2. Navigate to the project directory.

3. Run the tests:
```
pytest test_web_scraping_program.py
```

## Solutions
The program extracts information from web pages by utilizing the specified XPath expressions. It uses the `lxml` library to parse the HTML content of the web page and the `requests` library to fetch the web page's content.

## Future Plans
- Implement additional features like saving the extracted data to a file or exporting it to a database.
- Improve user interaction and make the program more user-friendly.
- Extend the program to scrape data from different types of websites.

## Inspirations and Acknowledgments
This program was developed as part of a practical Python course. Thanks for the inspiring material and support!

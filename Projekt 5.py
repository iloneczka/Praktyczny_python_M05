"""
Amazon Web Scraping Program

This program automatically extracts selected information from specified web pages.

Usage:
    python3 [filename][URL] [XPATH]

Arguments:
    URL (str): The URL of the web page to scrape.
    XPATH (str): The XPath expression to locate elements containing the desired information.

"""

# python3 '/Users/ilo/Desktop/PYTHON/Praktyczny_python_M05/Projekt 5.py' 'https://www.leroymerlin.pl/okna-i-drzwi/parapety,a228.html' '//div[contains(@class, "ProductListProductBlock_wrapper__uqfrW")]'

import click
from lxml import html
import requests

def extract_text(content: str, xpath: str) -> list[str]:
    """
    Extracts text from the webpage content using the XPath expression.

    Args:
        content (str): The webpage content.
        xpath (str): The XPath expression to locate elements containing the text.

    Returns:
        list[str]: The list of extracted texts.
    """
    dom = html.fromstring(content)
    elements = dom.xpath(xpath)
    # print(f'ELEMENTS: {elements}')
    cleaned_elements = [element.text_content().strip().replace('\n', '') for element in elements]
    return cleaned_elements

@click.command()
@click.argument('url')
@click.argument('xpath')
def main(url: str, xpath: str) -> None:
    """
    Main function of the program.

    Args:
        url (str): The URL of the webpage.
        xpath (str): The XPath expression to locate elements containing the text.

    Returns:
        None
    """
    page = requests.get(url)
    content = page.text
    elements = extract_text(content, xpath)
    for element in elements:
        print(element)

if __name__ == '__main__':
    main()

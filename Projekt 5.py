

# python3 '/Users/ilo/Desktop/PYTHON/Praktyczny_python_M05/Projekt 5.py' 'https://www.leroymerlin.pl/materialy-budowlane/materialy-budowlane-stan-surowy/piasek-keramzyt,a347.html' '//*[@id="product-listing"]//div[contains(@class, "catalog-card-container")]'
# python3 '/Users/ilo/Desktop/PYTHON/Praktyczny_python_M05/Projekt 5.py' 'https://home.biedronka.pl/kuchnia/?utm_source=biedronkapl&utm_medium=www&utm_campaign=biedronka_home_menu&_ga=2.34961573.501035135.1689147025-1634869815.1689147023' '//*[@id="product-listing"]/div[contains(@class, "ProductList")]'
#  python3 '/Users/ilo/Desktop/PYTHON/Praktyczny_python_M05/Projekt 5.py' 'https://homla.com.pl/salon.html' '//*[@id="maincontent"]/div/strong/a/text()'
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

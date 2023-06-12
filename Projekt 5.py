# Napisz dla Amazona program, który automatycznie wyciąga wybrane informacje z wybranych stron internetowych, na przykład nazwy produktów ze stron Leroy Merlin. Użytkownik podaje jedynie adres strony oraz ścieżkę xpath, którą może łatwo skopiować w przeglądarce.

# 1. Użyj biblioteki click, aby łatwiej było Ci odczytać url oraz xpath.

# 2. Podziel kod na funkcje tak, aby można było go łatwo testować.

# 3. Napisz kilka testów. Zacznij od tzw. happy path, tzn. najprostszego przypadku, a następnie przetestuj przypadki brzegowe.

# 4. Wyciągając z HTML tekst, usuń białe znaki z początku i końca (poszukaj odpowiedniej metody na stringach) oraz zamień znaki końca linii na spacje.

# 5. Wyświetl każdy znaleziony element HTML w osobnej linii.

# 6. Użyj docstringów, aby udokumentować Twój kod. Jakie informacje Twoim zdaniem warto tam zawrzeć?

# Hint: W razie problemów z cudzysłowami w XPATH pod Windows, możesz zamienić je na apostrofy, np.:
#     "//div[@id='wartosc']" 
# zamiast 
#     '//div[@id="wartosc"]'

# python3 '/Users/ilo/Desktop/PYTHON/Projekt 5.py' https://www.leroymerlin.pl '//*[@id="product-listing"]/div/a/h3/text()'

import click
from lxml import html
import requests

def extract_text(content, xpath):
    dom = html.fromstring(content)
    elements = dom.xpath(xpath)
    cleaned_elements = [element.text_content().strip().replace('\n', '') for element in elements]
    # print(cleaned_elements)
    return cleaned_elements

@click.command()
@click.argument('url')
@click.argument('xpath')
def main(url, xpath):
    page = requests.get(url)
    content = page.text
    elements = extract_text(content, xpath)
    for element in elements:
        print(element)

if __name__ == '__main__':
    main()

import requests
from bs4 import BeautifulSoup

from IPython.display import Image

url = 'https://www.pagina12.com.ar/'

def get_page_content(url):
    try:
        p12 = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(e)

    status_code = p12.status_code

    if status_code == 200:

        p12_text = p12.text

        p12_headers = p12.request.headers

        p12_content = p12.content

        soup = BeautifulSoup(p12_text, 'html.parser')

        # See the content of the page as a structured html
        soup.prettify()

        # Look for an specific tag: Find method returns the first tag that matches the criteria
        # The more specific the tag, the better
        section = soup.find('ul', attrs={'class': 'horizontal-list main-sections hide-on-dropdown'})

        # Find all returns a list of all the tags that match the criteria
        sections = soup.find('ul', attrs={'class': 'horizontal-list main-sections hide-on-dropdown'}).find_all('li')

        first_section = sections[0]

        links_sections = [section.a.get("href") for section in sections]


url = "https://www.pagina12.com.ar/538961-una-pregunta-de-emergencia-para-el-frente-de-todos"
def get_new_content(url):
    try:
        p12 = requests.get(url)
        status_code = p12.status_code
        if status_code == 200:
            s_nota = BeautifulSoup(p12.text, 'html.parser')

            # Title of the note
            title = s_nota.find('div', attrs={'class': 'section-2-col article-header'}).find('h1').text
            author = s_nota.find('div', attrs={'class': 'author-name'}).text
            date = s_nota.find('div', attrs={'class': 'date modification-date'}).find("time").get("datetime")
            content = s_nota.find('div', attrs={'class': 'article-main-content article-text'}).find_all('p')
            content_string = ""
            for pe in content:
                if pe.b:
                    content_string += pe.b.text
                else:
                    content_string += pe.text
            print(content_string)

            media = s_nota.find('div', attrs={'class': 'article-main-content article-text'}).find_all('img')
            Image(url=media[0].get("src"))
    except requests.exceptions.RequestException as e:
        print(e)

if __name__ == '__main__':
    get_new_content(url)


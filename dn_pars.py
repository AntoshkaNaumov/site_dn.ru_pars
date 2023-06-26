import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def get_info(page_url, headers):
    response = requests.get(page_url, headers=headers)
    bs = BeautifulSoup(response.content, "lxml")

    results = bs.find_all('div', class_='products-list-inline__top')

    for res in results:
        titles = res.find('a', class_='products-list__link text-name small blue')
        description = res.find('div', class_='products-list_col')
        link = res.find('a', class_='products-list__link text-name small blue').get('href')
        price = res.find('div', class_='products-list__price').find('span')
        absolute_link = urljoin(page_url, link)  # Create an absolute URL by joining the base URL and the relative link
        response_img = requests.get(absolute_link)
        soup = BeautifulSoup(response_img.content, "lxml")
        image_div = soup.find('div', class_='product-card__left').find('div').find('div', {'data-context': 'block:771'})
        image_src = image_div.find('img')['src']
        image_url = f"https://dn.ru{image_src}"


        print(f'название товара: {titles.text}')
        print(f'описание: {description.text}')
        print(f'ссылка на товар на сайте dn.ru: {absolute_link}')
        print(f'цена: {price.text}')
        print(f'ссылка на изображение: {image_url}')
        print()


if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    main_url = 'https://dn.ru/sharovyi-kran'
    page1_url = f'{main_url}?did169=1&p169=1'
    page2_url = f'{main_url}?did169=1&p169=2'

    get_info(page1_url, headers)
    get_info(page2_url, headers)

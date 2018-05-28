import bs4
import requests


def print_header():

    print('---------------------------')
    print('       Weather APP')
    print('---------------------------')
    print()


def get_zip():

    return input('Enter your zipcode (eg. 94001) or 0 to exit: ')


def fetch_weather_page(zipcode):
    url = 'https://www.wunderground.com/weather/' + zipcode

    r = requests.get(url)

    if r.status_code == 200:
        return r.text
    else:
        print('Fettch error')
        return []

def show_weather(weather, zipcode):

    soup = bs4.BeautifulSoup(weather, 'html.parser')

    location = soup.title.string[:-31]
    temp = soup.find(class_='wu-value').get_text()
    unit = soup.find(class_='wu-label').get_text().strip()
    current_weather = soup.find(class_='conditions-extra').find('p').get_text()

    print('Weather in {}, {} is {} degrees {} and {}'.format(location, zipcode, temp, unit, current_weather))
    print()

def main():

    print_header()

    zipcode = get_zip()
    while (zipcode != '0'):
        weather = fetch_weather_page(zipcode)
        show_weather(weather, zipcode)

        zipcode = get_zip()

if __name__ == '__main__':
    main()

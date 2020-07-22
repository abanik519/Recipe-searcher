from bs4 import BeautifulSoup
import urllib.request
import requests

def getImage(input):
    # setting URL destination
    ALL_RECIPES_SEARCH = \
        'https://www.allrecipes.com/search/results/'

    data = input
    print('Start searching...')
        
    # alter data string so that url query string is valid
    if ' ' in data:
        searchdata = data.replace(' ', '%20')
    else:
        searchdata = data

    # get url query string
    searchurl = ALL_RECIPES_SEARCH + searchdata
    print(searchurl)

    # retrieving HTML payload from the website
    response = requests.get(searchurl)

    # checking response.status_code (if you get 502, try rerunning the code)
    if response.status_code != 200:
        print(f"Status: {response.status_code} — Try rerunning the code\n")
    else:
        print(f"Status: {response.status_code}\n")

    # using BeautifulSoup to parse the response object
    soup = BeautifulSoup(response.content, "html.parser")

    # finding AllRecipes images in the soup
    images = soup.find_all("img", attrs={"class": "fixed-recipe-card__img"})

    # downloading images
    for image in images:
        image_src = image["data-original-src"]
        urllib.request.urlretrieve(image_src, 'api\Database\Images\\' + data + '.jpg')
        return (image["data-original-src"])
        break
    
if __name__ == "__main__":
    print(getImage("apple  banana casserole with almonds"))

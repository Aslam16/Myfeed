__Base_Url = "use your api provider url"
__Api_key = "use your api key given by the provider"
__Search_URL="search url from the api provider "


Business = "category=business"
Entertainment = "category=entertainment"
General = "category=general"
Health = "category=health"
Science = "category=science"
Sports = "category=sports"
Technology = "category=technology"
Language_Eng = "language=en"

country_india = "country=in"


def get_url(**kwargs):
    "return the url with the options"
    url = __Base_Url
    for var in kwargs:
        url += kwargs[var] +'&'
    url += __Api_key
    return url

def search_url(**kwargs):
    "return the url with the options"
    url = __Search_URL
    for var in kwargs:
        url += kwargs[var] +'&'
    url += __Api_key
    return url

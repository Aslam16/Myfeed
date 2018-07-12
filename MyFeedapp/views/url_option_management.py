__Base_Url = "api provider url"
__Api_key = "add your api key"
__Search_URL="add your search url"


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
__Base_Url = "https://newsapi.org/v2/top-headlines?"
__Api_key = "apiKey=e894a0f5703c4c41bf2487bdcf8e4e5d"
__Search_URL="https://newsapi.org/v2/everything?pageSize=40&"


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
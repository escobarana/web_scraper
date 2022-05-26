import requests


class Scraper:
    """
    Class Scrapper to retrieve the html content of a webpage given its url
    """
    def __init__(self, url: str):
        """
        Initialization of the class Scrapper
        :param url: URL of the webpage to do the scrapping
        """
        self.url = url

    def get_html_page(self):
        """
        This function retrieves the html content of a webpage using the library 'requests'
        :return: utils content of a webpage
        """
        page = requests.get(self.url)
        return page

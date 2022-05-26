from bs4 import BeautifulSoup
from utils.my_scraper import Scraper


class MyParser:
    """
    Class Parser to parse utils content and retrieve valuable information
    """
    def __init__(self, url: str):
        """
        Initialization of the class Parser
        :param url: URL of the webpage to do the scrapping to pass to the Scrapper
        """
        page = Scraper(url).get_html_page()
        soup = BeautifulSoup(page.content, "html.parser")  # makes sure to use the appropriate parser for HTML content.
        self.results = soup.find(id="ResultsContainer")

    def list_jobs(self):
        """
        This function retrieves all jobs information found in the webpage
        :return:
        """
        job_elements = self.results.find_all("div", class_="card-content")
        for job_element in job_elements:
            title_element = job_element.find("h2", class_="title")
            company_element = job_element.find("h3", class_="company")
            location_element = job_element.find("p", class_="location")
            print(title_element.text.strip())  # avoid the superfluous whitespace with .strip()
            print(company_element.text.strip())
            print(location_element.text.strip())
            # pick the second link through its index since it's the one we need to apply for the job
            link_url = job_element.find_all("a")[1]["href"]
            print(f"Apply here: {link_url}\n")
            print()

    def list_jobs_by_keyword(self, keyword: str):
        """
        This function retrieves all jobs information found in the webpage given a keyword
        :param keyword: word to filter jobs by
        :return:
        """
        keyword_jobs = self.results.find_all("h2", string=lambda text: keyword.lower() in text.lower())
        # Fetch the great-grandparent elements
        keyword_job_elements_list = [h2_element.parent.parent.parent for h2_element in keyword_jobs]
        for job_element in keyword_job_elements_list:
            title_element = job_element.find("h2", class_="title")
            company_element = job_element.find("h3", class_="company")
            location_element = job_element.find("p", class_="location")
            print(title_element.text.strip())  # avoid the superfluous whitespace with .strip()
            print(company_element.text.strip())
            print(location_element.text.strip())
            # pick the second link through its index since it's the one we need to apply for the job
            link_url = job_element.find_all("a")[1]["href"]
            print(f"Apply here: {link_url}\n")
            print()

# Web Scrapping `https://realpython.github.io/fake-jobs/`
## Libraries 
The libraries are specified in the `requirements.txt` file. To run it and install them, run in your terminal `pip install -r requirements.txt`

## Utils folder
This folder contains two python files. `my_scraper.py` is used to retrieve the html content of a webpage given its url.
`my_parser.py` uses the `Scraper` class contained in the previous python file in order to do the scrapping to the html content of a webpage.
The `Parser` class has two methods, `list_jobs()` that lists all the jobs available in the webpage and the url link to apply to the job and 
`list_jobs_by_keyword()` that given a keyword it finds the jobs containing that keyword.

## Run code
After installing the necessary libraries from the `requirements.txt` file, run the `main.py` file in order to list all jobs available
and also the ones containing the keyword `python`. You can change this keyword if you wish to search for jobs containing a different keyword.

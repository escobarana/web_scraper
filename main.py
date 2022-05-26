from utils.my_parser import Parser

if __name__ == '__main__':
    url = 'https://realpython.github.io/fake-jobs/'
    keyword = 'Python'
    parser = Parser(url)
    print(f"All Jobs available in: {url}\n")
    parser.list_jobs()
    print(f"All {keyword} Jobs available in: {url}\n")
    parser.list_jobs_by_keyword(keyword=keyword)

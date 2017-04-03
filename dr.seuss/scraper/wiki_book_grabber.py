import requests;
from bs4 import BeautifulSoup;



def main():
    re = requests.get("https://en.wikipedia.org/wiki/Dr._Seuss_bibliography");
    soup = BeautifulSoup(re.text, "html.parser");

    book_titles = soup.select(".wikitable tr b a");

    for book in book_titles:
        print(book.get("title"));

if __name__ == "__main__":
    main()

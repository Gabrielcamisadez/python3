import requests
from bs4 import BeautifulSoup
import json

# -- requests and beatifulsoup


# ------------------------

def extract_links_from_site():
# -- make HTTP request to obtain the HTML data
    url = "https://blog.leonardotamiano.xyz/tech/"
    r = requests.get(url)

# -- parse the HTML data into a soup object ->
    soup = BeautifulSoup(r.text, "html.parser")

# -- now i can query the document and extrac the parts we're interested in
    articles = soup.find_all("article")


# -- [<article class="archive-link">
# <time datetime="2024-09-09">2024.09.09</time>
#   -
#   <header style="display: inline;"><a href="https://blog.leonardotamiano.xyz/tech/linux-kernel-qemu-setup/">Explore Linux Kernel Programming with QEMU</a></header>
# </article>,



    data = []
    for article in articles:
        pubblication_date = article.find("time").text
        link = article.find("a")['href']
        title = ""

        data.append({
            "title": title,
            "link": link,
            "date": pubblication_date
        })
    
    print(json.dumps(data, indent=2))



# ------------------------

def main():
    extract_links_from_site()


if __name__ == "__main__":
    main()
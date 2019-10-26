"""
This project is made to get all the valid URLS from a website. website name will be input by user.
Finally all valid URLs will be stored in a file called valid_urls.txt.
"""
import sys

import requests as r
from bs4 import BeautifulSoup


def get_valid_url():
    """
    get valid url from the user
    :return: str
    """
    while 1:
        web_name = input("Enter a website name:")
        if web_name.startswith("http"):
            print("URl is seen to be valid. Please wait...")
            print("*" * 100)
            return web_name.strip()
        else:
            print("invalid url\nA valid url always starts with http or https \n"
                  "e.g. http://www.myweb.com or https://myweb.net")

            print("*" * 100)
            continue


def get_html(web_url):
    try:
        request = r.get(web_url)
        return request.text
    except:
        print("An error is found while connecting with this website.\n"
              "Please check your link. This issue might occur because of\n"
              "following reasons\n"
              "1. The website which you are going to access cannot be accessed on your current using internet\n"
              "2. Some website does not allow web scarping.\n"
              "Please open this website in a browser and check either it is opening or not and then try again")
        print("*" * 100)
        sys.exit()


def get_all_valid_links(h_content, web_name):
    """

    :param h_content: str
    :param web_name: str
    :return: all valid url: list
    """
    try:
        valid_urls = []

        bs = BeautifulSoup(h_content, "html.parser")
        # fetching all the urls
        for link in bs.find_all("a"):
            href = link.get("href")
            if href.startswith("../") and href != "#":
                valid_urls.append(web_name + href[2:])
            elif href.startswith("http"):
                valid_urls.append(href)

        return valid_urls
    except:
        print("An error has occurred while retrieving the links. There can be many \n"
              "issues for it\n"
              "1. Network is slow\n"
              "2. website does not allow you to access its content.Please read the policies for further information")
        print("*" * 100)
        sys.exit()


def store_links_in_file(web_links):
    """
    Write all links in a file
    :param web_links: list
    :return: None
    """
    try:
        f = open("valid_urls.txt", "w")
        f.write("\n".join(web_links))
        f.close()
        print("All the links have been written in a file.")

    except:

        print("There is a issue while writing all links in a file.\n"
              "Make sure the file isn't opened.")
        print("*" * 100)
        sys.exit()


if __name__ == '__main__':
    # get a valid user url
    url = get_valid_url()

    # get all html content
    html_content = get_html(web_url=url)
    # test valid html content
    # print(html_content)

    # get valid url from a website
    links = get_all_valid_links(h_content=html_content, web_name=url)
    # to test the URL
    # print(links)

    # store all the links a file
    store_links_in_file(web_links=links)

    # open a file
    is_open = input('Do you want to open a file?')
    if is_open.strip().lower() == "yes":
        read_file = open("valid_urls.txt")
        print(read_file.read())
        read_file.close()

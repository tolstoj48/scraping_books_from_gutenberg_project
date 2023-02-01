from bs4 import BeautifulSoup
from csv import writer
import requests
import re
import sys


def clear_list(listy):
    """
    The function to clear words from interpunction etc.
    """
    for index, word in enumerate(listy):
        listy[index] = re.sub(r'[^\w]', "", word)
    return listy


def lower_text(soup):
    """
    The function to get app <p> elements = texts and lower them.
    """
    result = ""
    par = soup.find_all("p")
    for each in par:
        each = each.get_text().lower()
        result += str(each)
    return result


def get_book(adr):
    """
    The function to get BS data from the provided link.
    """
    request_result = requests.get(
        f"{adr}")
    soup = BeautifulSoup(request_result.text, "html.parser")
    return soup


def get_list_of_words(text):
    """
    The function to split all the texts into separate words.
    """
    return text.split()


def populate_csv(result_list):
    """
    The function to save words into csv file.
    """
    with open("words.csv", "w", encoding="utf-8", newline='') as file:
        # comma is problematic for number of columns in texts
        csv_writer = writer(file)
        for word in result_list:
            csv_writer.writerow([word])
    return


# get request from the link provided by the user on the command line
soup = get_book(sys.argv[1])
# lower the whole text
lowered_text = lower_text(soup)
# split the text into the list of words
listy = get_list_of_words(lowered_text)
# get rid of punctuations
cleared_list = clear_list(listy)
# save the result into csv file
populate_csv(cleared_list)
# tell about the end
print("done")

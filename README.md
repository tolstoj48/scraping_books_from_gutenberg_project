# Tool to scrap books from the Project Gutenberg site

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info

Anybody can download a book from the internet thanks to the people from https://gutenberg.org/.

## Technologies
Project is created with:
* Python 3
* BeautifulSoup 4

## Setup

Clone the repo:
https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository

In the command line go to the directory with the repo and use like this:
"python words_from_gutenberg.py your_link new_file"

For example:
"python words_from_gutenberg.py  https://gutenberg.org/files/2701/2701-h/2701-h.htm new_file.csv"

Csv file with the name "new_file.csv" from the book "https://gutenberg.org/files/2701/2701-h/2701-h.htm" is saved in the working directory.

Provide only htm links from the Project Gutenberg.

Due to the structure of the site of the provided link, there might be need to edit the result file:
* the beginnings of the sites on the Project Gutenberg are contents and additional info
* the end of the sites are now downloaded at the moment - no need to edit
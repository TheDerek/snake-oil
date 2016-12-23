import xml.etree.ElementTree as ET
from functools import reduce


def create_word_svg(word, svg_template):
    # Load the svg file
    root = ET.parse(svg_template).getroot()

    # Find the text we need to replace
    word_element = root.find('.//*[@id="wordText"]')
    word_element.text = word.capitalize()

    # Save the file
    path = 'assets/cards/' + word + '.svg'
    tree = ET.ElementTree(root)
    tree.write(path)
    return root


def page_items(items, items_per_page) -> [[str]]:
    """
    Split a list of items into pages, with each page containing a certain
    amount of each item.

    :param items: The list of items to pageify.
    :param items_per_page: The number of items per page.
    :return: An array of arrays, with each array being a page of items.
    """

    # Split the words into pages (16 per page)
    pages = []
    for index, item in enumerate(items):
        # Fetch the page number
        page_number = float(index) / items_per_page

        # Create a new page if word is the first word in the page
        if page_number.is_integer():
            pages.append([])

        # Add that word to the page
        pages[int(page_number)].append(item)

    return pages


if __name__ == "__main__":
    # Load the list of words
    wordsFile = open('assets/words.txt')
    words = list(map(lambda w: w.strip(), wordsFile.readlines()))

    # Split the word into pages
    pages = page_items(words, 16)

    # Create an SVG for each card with a customised word
    for word in words:
        svg = create_word_svg(word, 'assets/template_test.svg')
        pass

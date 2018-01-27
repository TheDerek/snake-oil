import xml.etree.ElementTree as ET
import copy
from functools import reduce


def create_page_svg(page, svg_template, page_number=0):
    # Load the svg file
    root = ET.parse(svg_template).getroot()
    layer = root.find('.//*[@id="layer1"]')

    # Find and copy the card element
    original_card = root.find('.//*[@id="card"]')

    # Create a 4x4 grid of cards
    for y in range(0, 4):
        for x in range(0, 4):
            # Create the card in the correct position
            page_x = x * 74.25
            page_y = y * 52.5
            word_index = (y * 4) + x
            print(word_index)

            # If there is no word here then skip the card
            if word_index > len(page) - 1:
                continue

            card = copy.deepcopy(original_card)
            card.attrib['id'] = 'card' + str(x) + 'x' + str(y)
            card.attrib['transform'] = 'translate(' + str(page_x) \
                                       + ', ' + str(page_y) + ')'

            # Change the text of the card
            text_element = card.find('.//*[@id="wordText"]')
            text_element.text = page[word_index].capitalize()

            # Add the card to the page
            layer.append(card)

    # Remove the original card
    layer.remove(original_card)

    # Save the file
    path = 'assets/cards/' + str(page_number) + '.svg'
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

    print(pages[-1])

    # Create an SVG for each page
    for index, page in enumerate(pages):
        # Fetch the card SVG
        svg = create_page_svg(page, 'assets/template_test.svg', index)

        pass

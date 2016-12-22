import xml.etree.ElementTree as ET


if __name__ == "__main__":

    # Load the list of words
    wordsFile = open('assets/words.txt')
    words = list(map(lambda w: w.strip(), wordsFile.readlines()))

    # Create an SVG for each card with a customised word
    for word in words:
        # Load the svg file
        root = ET.parse('assets/word-front.svg').getroot()

        # Find the text we need to replace
        word_element = root.find('.//*[@id="wordText"]')
        word_element.text = word.capitalize()

        # Save the file
        path = 'assets/cards/' + word + '.svg'
        tree = ET.ElementTree(root)
        tree.write(path)





    print(words)

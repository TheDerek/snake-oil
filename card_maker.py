import xml.etree.ElementTree


if __name__ == "__main__":
    # Load the svg file
    svg = xml.etree.ElementTree.parse('assets/word-front.svg').getroot()

    # Find the text we need to replace
    word_element = svg.find('.//*[@id="wordText"]')
    word_element.text = "OPera"

    print(word_element.text)

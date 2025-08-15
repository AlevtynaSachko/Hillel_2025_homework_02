import logging
import xml.etree.ElementTree as ET
from pathlib import Path

# Налаштування логера
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Файл XML
xml_file = Path(__file__).parent /"groups.xml"

# Парсимо XML
tree = ET.parse(xml_file)
root = tree.getroot()


def find_incoming_bytes(group_number):
    for group in root.findall("group"):
        number = group.find("number")
        if number is not None and number.text == group_number:
            incoming = group.find("timingExbytes/incoming")
            if incoming is not None:
                return incoming.text
    return None


search_number = "3"
incoming_value = find_incoming_bytes(search_number)

if incoming_value:
    logging.info(f"Група {search_number} має incoming bytes: {incoming_value}")
else:
    logging.info(f"Групу з номером {search_number} не знайдено або немає incoming.")


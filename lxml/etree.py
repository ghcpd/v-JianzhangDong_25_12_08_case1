import xml.etree.ElementTree as ET

def fromstring(text):
    return ET.fromstring(text)

# Provide minimal compatibility for indexing and .text access

from lxml import etree

def parse_xml_safely(xml_data):
    parser = etree.XMLParser(resolve_entities=False, no_network=True)
    try:
        tree = etree.fromstring(xml_data, parser)
        return tree
    except Exception as e:
        return None  # or return str(e) for error tracing


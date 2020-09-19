# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 12:02:15 2020

@author: nickf
"""

#import xml.etree.cElementTree as ET
#from collections import defaultdict
#import re
#import pprint

#OSMFILE = "example.osm"
#street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)


expected = ["A","B","C","D","E","F","G","H","I","J","K","L","M",
            "N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
            "Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", 
            "Lane", "Road", "Trail", "Parkway", "Commons", "Terrace", "Run", "Way", 
            "Circle", "Cove", "Loop", "Pass", "Bend", "Vista", "Path", "Loop", "Highway",
            "Hollow", "Park", "Creek", "Crossing", "Glen", "Hill", "Plaza", "Point", 
            "Ridge", "Row", "Trace", "View", "Walk", "North", "East", "South", "West",]

mapping = { "St.": "Street",
            "St": "Street", 
            "Rd.": "Road",
            "Rd": "Road",
            "Ave.": "Avenue",
            "Ave": "Avenue",
            "Dr.": "Drive",
            "Dr": "Drive",
            "Blvd.": "Boulevard",
            "Blvd": "Boulevard",
            "Cv.": "Cove",
            "Cv": "Cove",
            "Ct.": "Court",
            "Ct": "Court",
            "Ln.": "Lane",
            "Ln": "Lane",
            "Hwy": "Highway"
            }


def is_street_name(elem):
    return (elem == "addr:street")

def replace_street_type(street_name):
    """ replaces abbreviated street types with full word from predefined mapping lookup
        Args:
            street_name (string): full street name
        Returns:
            string: street name with abbrevation replaced
    """
    if ' ' in street_name:
        street_type = street_name.rsplit(' ',1)[1]
        street_actual = street_name.rsplit(' ',1)[0]
        return street_actual + ' ' + update_name(street_type, mapping)
    else:
        return street_name
    
def update_name(name, mapping):
    for key,value in mapping.items():
        if key == name:
            return name.replace(key,value)
    return name

# def audit_street_type(street_types, street_name):
#     m = street_type_re.search(street_name)
#     if m:
#         street_type = m.group()
#         if street_type not in expected:
#             street_types[street_type].add(street_name)
            
            
# def audit(osmfile):
#     osm_file = open(osmfile, "r", encoding="utf8")
#     street_types = defaultdict(set)
#     for event, elem in ET.iterparse(osm_file, events=("start",)):
#         if elem.tag == "node" or elem.tag == "way":
#             for tag in elem.iter("tag"):
#                 if is_street_name(tag):
#                     replace_street_type(tag)
#     osm_file.close()
#     return street_types




# def test():
#     st_types = audit(OSMFILE)
#     pprint.pprint(dict(st_types))

#     for st_type, ways in st_types.items():
#         for name in ways:
#             better_name = update_name(name, mapping)
#             print(name, "=>", better_name)
#      #       if name == "West Lexington St.":
#      #          assert better_name == "West Lexington Street"
#      #       if name == "Baldwin Rd.":
#      #          assert better_name == "Baldwin Road"


# if __name__ == '__main__':
#     test()
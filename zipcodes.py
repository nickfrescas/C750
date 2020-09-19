# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 07:35:27 2020

@author: nickf
"""

def replace_zip_code(zip_code):
    """ truncates zip to left 5 characters
        Args:
            zip_code (string): zip code
        Returns:
            string: left five digits of zip zode
    """
    if len(zip_code)>5:
        return zip_code[0:5]
    else:
        return zip_code
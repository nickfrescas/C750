# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 07:53:27 2020

@author: nickf
"""
import re
re_number = '[^\d\.]'

def replace_height(height):
    """ removes strings from height values, except in semi-colon separated lists
        Args:
            height (string): height value
        Returns:
            string: original height scrubbed of any string characters, or original seme-colon separated list
    """
    if ';' in height: #allowing separated values b/c stripping out the semi-colon would be worse
        return height
    else:
        return re.sub(re_number, "", height)
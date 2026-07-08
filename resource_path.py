# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 00:34:29 2026

@author: AJITH
"""

import os
import sys

def resource_path(relative_path):
    """Return the absolute path to a resource, works for development and PyInstaller."""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
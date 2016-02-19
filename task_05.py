#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""task 05"""


def defaults(my_required, my_optional=True):
    """1.  ``my_optional`` which has a default value of True

    2.  ``my_required`` which is a required param and has no default value"""
    return my_optional is my_required

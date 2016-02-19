#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""task 04"""


def too_many_kittens(kittens, litterboxes, catfood):
    """ 1.  kittens, the number of kittens

    2.  litterboxes, the (integer) number of available litterboxes

    3.  catfood, a boolean representing whether or not any catfood exists"""
    return not (litterboxes >= kittens and catfood)

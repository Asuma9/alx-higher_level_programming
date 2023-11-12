#!/usr/bin/python3
# 2-replace_in_list.py


def replace_in_list(my_list, idx, element):
    """Replaces element of my_list at position idx"""
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)
    my_list[idx] = element
    return (my_list)

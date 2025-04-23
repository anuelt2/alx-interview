#!/usr/bin/python3
"""Module for lockboxes"""


def canUnlockAll(boxes):
    """Method to determine id all boxes can be opened"""
    n = len(boxes)
    opened_boxes = set([0])
    keys = set(boxes[0])

    while keys:
        key = keys.pop()
        if 0 <= key < n and key not in opened_boxes:
            opened_boxes.add(key)
            keys.update(boxes[key])

    return len(opened_boxes) == n

#!/usr/bin/python3
""" Method to open locked boxes"""


def canUnlockAll(boxes):
    """ method to chexk if all boxes can be unlocked"""

    def find_keys(box):
        """return the keys in the box"""
        box_keys = []
        for key in box:
            box_keys.append(key)
        return box_keys

    def box_quantity(boxes):
        """return the number of boxes to check"""
        return (len(boxes))

    def init_state(box_quantity):
        """init the status list"""
        box_state = {}
        box_quantity -= 1
        while (box_quantity > 0):
            box_state[box_quantity] = ['close', 'uncheck']
            box_quantity -= 1
        box_state[0] = ['open', 'uncheck']
        return (box_state)

    def open_box(box_state, box_number, box_quantity):
        """open a box"""
        if box_state[box_number] != 'open':
            box_state[box_number] = 'open'
        return (box_state)

    def check_box(keys, box_state, box_quantity):
        """funtion to check the boxes"""

        for key in keys:
            if box_state[key][0] == 'open' and box_state[key][1] == 'uncheck':

                box_keys = find_keys(boxes[key])

                box_state[key][1] = 'check'

                for key in box_keys:
                    if key < box_quantity:
                        box_state[key][0] = 'open'
                box_state = check_box(box_keys, box_state, box_quantity)
            else:
                pass

        return (box_state)
    # |----------------- end of methods --------------------|

    box_quantity = box_quantity(boxes)

    box_state = init_state(box_quantity)
    box_state = check_box([0], box_state, box_quantity)

    for key, value in box_state.items():
        if value[0] == "close":
            return False
    return True

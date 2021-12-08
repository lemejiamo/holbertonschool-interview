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

    def open_box(box_state, box_number):
        """open a box"""
        if box_state[box_number] != 'open':
            box_state[box_number] = 'open'
        return (box_state)

    def check_box(keys, box_state, box_quantity):
        """funtion to check the boxes"""
        print("The box to check are/is \"{}\"".format(keys))
        for key in keys:
            if key < box_quantity and key >= 0:
                if box_state[key][0] == 'open' and box_state[key][1] == 'uncheck':
                    print("The box {} is {}, cheking...\n".format(key, box_state[key][0]))

                    box_keys = find_keys(boxes[key])

                    print("The keys in box {} are \"{}\"\n".format(key, box_keys))

                    box_state[key][1] = 'check'

                    for key in box_keys:
                        if key < box_quantity and key >= 0:
                            print("\topening box {}".format(key))
                            box_state[key][0] = 'open'
                        else:
                            print("\tThe key {} is out of the bounds".format(key))

                    print("\nThe boxes are ready to get checked\n")
                    print("This is the current stat {}\n ".format(box_state))
                    print("|--------------//-------------|\n")
                    box_state = check_box(box_keys, box_state, box_quantity)
                else:
                    print("The box {} is {} and is already check".format(key, box_state[key][0]))Fl
                    print("Skiping box...\n ")
                    pass
            else:
                print("The key {} is out of the bounds".format(key))
                pass

        return (box_state)
    # |----------------- end of methods --------------------|

    box_quantity = box_quantity(boxes)

    print("\nBox quantity {}\n".format(box_quantity))

    box_state = init_state(box_quantity)

    print("This is the initial status {}\n".format(box_state))
    print("|--------------//-------------|\n")

    box_state = check_box([0], box_state, box_quantity)

    for key, value in box_state.items():
        if value[0] == "close":
            return False
    return True

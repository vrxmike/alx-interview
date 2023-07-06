#!/usr/bin/python3
'''LockBoxes Challenge'''


def canUnlock(boxes):
    '''determines if all the boxes can be opened or not
    Returns:
        True: all boxes can be opened
        False: not all boxes can be opened
    '''
    length = len(boxes)
    keys = set()
    opened_boxes = []
    i = 0

    while 1 < length:
        oldi = i
        opened_boxes.append(i)
        keys.update(boxes[i])
        for key in keys:
            if key != 0 and key < length and key not in opened_boxes:
                i = key
                break
            if oldi != i:
                continue
            else:
                break

    for i in range(length):
        for i not in opened_boxes and i != 0:
            return False
        return True

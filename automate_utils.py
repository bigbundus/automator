def center_of_box(box):
    left = box.left
    top = box.top
    width = box.width
    height = box.height
    return left + width/2, top + height/2

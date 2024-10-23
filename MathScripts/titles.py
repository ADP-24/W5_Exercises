import math

length = 10
width = 8

area = length * width

tiles_needed = area

total_tiles_needed = tiles_needed + (0.10 * tiles_needed)

boxes_needed = math.ceil((total_tiles_needed)/12)

print("You will need" ,float(boxes_needed), "boxes of tiles")
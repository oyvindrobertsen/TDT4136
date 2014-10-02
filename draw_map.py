from PIL import Image

COLOR_MAP = {
    'r': '#cd853f',
    'g': '#7fff00',
    'f': '#006400',
    'm': '#8b8989',
    'w': '#0000ff',
    'A': '#ff0000',
    'B': '#9400d3',
    '#': '#8b8989',
    '.': '#ffffff'
}

SCALE = 16

def get_box_coordinates(i, j):
    return (j*SCALE+1, i*SCALE+1, (j+1)*SCALE-1, (i+1)*SCALE-1)

def get_route_coordinates(i, j):
    return (
        j*SCALE+(SCALE/2-3),
        i*SCALE+(SCALE/2-3),
        j*SCALE+(SCALE/2+3),
        i*SCALE+(SCALE/2+3)
        )

def get_visited_coordinates(i, j):
    return (
        j*SCALE+(SCALE/2-1),
        i*SCALE+(SCALE/2-1),
        j*SCALE+(SCALE/2+1),
        i*SCALE+(SCALE/2+1)
        )

def draw_map(grid, filename, path=None, open_list=None, closed_list=None):

    im = Image.new("RGB", (grid.width*SCALE, grid.height*SCALE))

    # Draw map
    for i, row in enumerate(grid.matrix):
        for j, elem in enumerate(row):
            color = COLOR_MAP[elem]
            im.paste(color, get_box_coordinates(i, j))

    # Draw visited tiles
    if open_list:
        for node in open_list:
            im.paste('#9400d3', get_visited_coordinates(node.x, node.y))

    # Draw closed tiles
    if closed_list:
        for node in closed_list:
            im.paste('#ff0000', get_visited_coordinates(node.x, node.y))

    # Draw best path
    if path:
        for node in path:
            im.paste('#000000', get_route_coordinates(node.x, node.y))

    im.save(filename)
    

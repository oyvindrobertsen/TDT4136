from PIL import Image

LOOK_AT_THE_PRETTY_COLORS = {
    'r': '#cd853f',
    'g': '#7fff00',
    'f': '#006400',
    'm': '#8b8989',
    'w': '#0000ff',
    'A': '#ff0000',
    'B': '#00ff00',
    '#': '#8b8989',
    '.': '#ffffff'
}

BLACK = '#000000'
HOT_PINK = '#ff69b4'
CYAN = '#00ffff'

TILE_SIDE = 32


def square(x, y):
    return (y * TILE_SIDE + 1,
            x * TILE_SIDE + 1,
            (y + 1) * TILE_SIDE - 1,
            (x + 1) * TILE_SIDE - 1)


def big_dot(x, y):
    return (y * TILE_SIDE + (TILE_SIDE / 2 - 3),
            x * TILE_SIDE + (TILE_SIDE / 2 - 3),
            y * TILE_SIDE + (TILE_SIDE / 2 + 3),
            x * TILE_SIDE + (TILE_SIDE / 2 + 3))


def small_dot(x, y):
    return (y * TILE_SIDE + (TILE_SIDE / 2 - 2),
            x * TILE_SIDE + (TILE_SIDE / 2 - 2),
            y * TILE_SIDE + (TILE_SIDE / 2 + 2),
            x * TILE_SIDE + (TILE_SIDE / 2 + 2))


def draw_map(grid, file_path, path=None, open_nodes=None, closed_nodes=None):
    image = Image.new("RGB", (grid.width * TILE_SIDE, grid.height * TILE_SIDE))

    for x, row in enumerate(grid.lines):
        for y, tile in enumerate(row):
            image.paste(LOOK_AT_THE_PRETTY_COLORS[tile], square(x, y))

    for node in open_nodes:
        image.paste(CYAN, small_dot(node.x, node.y))

    for node in closed_nodes:
        image.paste(HOT_PINK, small_dot(node.x, node.y))

    for node in path:
        image.paste(BLACK, big_dot(node.x, node.y))

    image.save(file_path)
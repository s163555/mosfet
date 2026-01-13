import pya

# -------------------------------------------------
# Shared Constants (macros can override)
# -------------------------------------------------
DEFAULT_CONTACT_SIZE = 3.0
DEFAULT_CONTACT_SPACE = 3.0
DEFAULT_CONTACT_ENCLOSURE = 2.0

# -------------------------------------------------
# Geometric Helpers
# -------------------------------------------------
def um(layout, x):
    # Converts microns to DBU integers (rounded).
    return int(round(x / layout.dbu))

def draw_box(layout, cell, layer, x_center, y_center, w, h):
    # Draws a centered box on the given layer.
    box = pya.Box(
        um(layout, x_center - w/2), um(layout, y_center - h/2),
        um(layout, x_center + w/2), um(layout, y_center + h/2)
    )
    cell.shapes(layer).insert(box)
    return box

def draw_wire(layout, cell, layer, points, width):
    # Draws a path (wire) with rounded ends extending by width/2.
    pya_points = [pya.Point(um(layout, x), um(layout, y)) for x, y in points]
    path = pya.Path(pya_points, um(layout, width))
    path.begin_ext = um(layout, width / 2)
    path.end_ext = um(layout, width / 2)
    cell.shapes(layer).insert(path)

def draw_cross(layout, cell, layer, x, y, size, width):
    # Draws a cross (alignment/dicing mark) centered at x,y.
    draw_box(layout, cell, layer, x, y, size, width) # Horizontal bar
    draw_box(layout, cell, layer, x, y, width, size) # Vertical bar

def fill_area_with_contacts(layout, cell, layer, cx, cy, w, h, size=DEFAULT_CONTACT_SIZE, space=DEFAULT_CONTACT_SPACE, enclosure=DEFAULT_CONTACT_ENCLOSURE):
    effective_w = w - 2 * enclosure
    effective_h = h - 2 * enclosure
    
    if effective_w < size or effective_h < size:
        return 

    pitch = size + space
    n_cols = int((effective_w + space) / pitch)
    n_rows = int((effective_h + space) / pitch)
    
    if n_cols < 1 or n_rows < 1:
        return 
        
    arr_w = n_cols * size + (n_cols - 1) * space
    arr_h = n_rows * size + (n_rows - 1) * space
    
    start_x = cx - arr_w / 2.0 + size / 2.0
    start_y = cy - arr_h / 2.0 + size / 2.0
    
    for c in range(n_cols):
        for r in range(n_rows):
            px = start_x + c * pitch
            py = start_y + r * pitch
            
            box = pya.Box(
                um(layout, px - size/2), um(layout, py - size/2),
                um(layout, px + size/2), um(layout, py + size/2)
            )
            cell.shapes(layer).insert(box)
            
def write_layer_properties(lyp_path, layers_config):
    with open(lyp_path, "w") as f:
        f.write('<?xml version="1.0" encoding="utf-8"?>\n')
        f.write('<layer-properties>\n')
        
        for name, lay, dt, color, dither in layers_config:
            f.write(' <properties>\n')
            f.write(f'  <frame-color>{color}</frame-color>\n')
            f.write(f'  <fill-color>{color}</fill-color>\n')
            f.write(f'  <frame-brightness>0</frame-brightness>\n')
            f.write(f'  <fill-brightness>0</fill-brightness>\n')
            f.write(f'  <dither-pattern>I{dither}</dither-pattern>\n')
            f.write(f'  <line-style/>\n')
            f.write(f'  <valid>true</valid>\n')
            f.write(f'  <visible>true</visible>\n')
            f.write(f'  <transparent>false</transparent>\n')
            f.write(f'  <width/>\n')
            f.write(f'  <marked>false</marked>\n')
            f.write(f'  <xfill>false</xfill>\n')
            f.write(f'  <animation>0</animation>\n')
            f.write(f'  <name>{name} ({lay}/{dt})</name>\n')
            f.write(f'  <source>{lay}/{dt}@1</source>\n')
            f.write(' </properties>\n')
            
        f.write('</layer-properties>\n')
    print(f"Layer properties written to: {lyp_path}")
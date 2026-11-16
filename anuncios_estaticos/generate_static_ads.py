import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUTPUT_DIR = r"C:\Users\RAFA\Documents\ECOMM\CREACION DE CONTENIDO ECOMM\MUCINA DE CARACOL 92\anuncios_estaticos"
IMAGES_DIR = r"C:\Users\RAFA\Documents\ECOMM\CREACION DE CONTENIDO ECOMM\MUCINA DE CARACOL 92\images"
FONTS_DIR = r"C:\Windows\Fonts"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Helper functions for drawing
def get_font(name, size):
    path = os.path.join(FONTS_DIR, name)
    if os.path.exists(path):
        return ImageFont.truetype(path, size)
    return ImageFont.load_default()

def draw_rounded_rect(draw, bbox, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(bbox, radius=radius, fill=fill, outline=outline, width=width)

def draw_shadowed_rounded_rect(image, bbox, radius, fill, shadow_color=(0,0,0,35), shadow_offset=(0, 8), blur_radius=12, outline=None, outline_width=1):
    # Create shadow layer
    shadow_img = Image.new("RGBA", image.size, (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow_img)
    x0, y0, x1, y1 = bbox
    ox, oy = shadow_offset
    s_bbox = (x0 + ox, y0 + oy, x1 + ox, y1 + oy)
    s_draw.rounded_rectangle(s_bbox, radius=radius, fill=shadow_color)
    shadow_img = shadow_img.filter(ImageFilter.GaussianBlur(blur_radius))
    
    # Composite shadow
    image.alpha_composite(shadow_img)
    
    # Draw actual rect
    rect_img = Image.new("RGBA", image.size, (0, 0, 0, 0))
    r_draw = ImageDraw.Draw(rect_img)
    r_draw.rounded_rectangle(bbox, radius=radius, fill=fill, outline=outline, width=outline_width)
    image.alpha_composite(rect_img)

def wrap_text(draw, text, font, max_width):
    words = text.split()
    lines = []
    current_line = []
    for word in words:
        current_line.append(word)
        bbox = draw.textbbox((0, 0), " ".join(current_line), font=font)
        if bbox[2] - bbox[0] > max_width:
            if len(current_line) == 1:
                lines.append(" ".join(current_line))
                current_line = []
            else:
                current_line.pop()
                lines.append(" ".join(current_line))
                current_line = [word]
    if current_line:
        lines.append(" ".join(current_line))
    return lines

print("Setup completed.")

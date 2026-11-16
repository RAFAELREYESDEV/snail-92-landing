import os
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUTPUT_DIR = r"C:\Users\RAFA\Documents\ECOMM\CREACION DE CONTENIDO ECOMM\MUCINA DE CARACOL 92\anuncios_estaticos"
IMAGES_DIR = r"C:\Users\RAFA\Documents\ECOMM\CREACION DE CONTENIDO ECOMM\MUCINA DE CARACOL 92\images"
FONTS_DIR = r"C:\Windows\Fonts"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def get_font(name, size):
    path = os.path.join(FONTS_DIR, name)
    if os.path.exists(path):
        return ImageFont.truetype(path, size)
    return ImageFont.load_default()

def draw_shadow(base_img, bbox, radius, shadow_color=(0,0,0,45), offset=(0,10), blur=14):
    shadow_layer = Image.new("RGBA", base_img.size, (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow_layer)
    x0, y0, x1, y1 = bbox
    ox, oy = offset
    s_draw.rounded_rectangle([x0 + ox, y0 + oy, x1 + ox, y1 + oy], radius=radius, fill=shadow_color)
    shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(blur))
    base_img.alpha_composite(shadow_layer)

def extract_clean_jar():
    jar_path = os.path.join(IMAGES_DIR, "hero_jar.jpg")
    im = Image.open(jar_path).convert("RGBA")
    # Clean floodfill corners
    ImageDraw.floodfill(im, (0, 0), (255, 255, 255, 0), thresh=20)
    ImageDraw.floodfill(im, (im.width-1, 0), (255, 255, 255, 0), thresh=20)
    ImageDraw.floodfill(im, (0, im.height-1), (255, 255, 255, 0), thresh=20)
    ImageDraw.floodfill(im, (im.width-1, im.height-1), (255, 255, 255, 0), thresh=20)
    return im

clean_jar = extract_clean_jar()

# ==============================================================================
# AD 1: FEATURE POINT OUT / TITULAR + BENEFICIOS DIRECTOS
# ==============================================================================
def create_ad_1():
    print("Generating Ad 1: Feature Point Out...")
    W, H = 1080, 1350
    base = Image.new("RGBA", (W, H), (251, 249, 245, 255))
    draw = ImageDraw.Draw(base)

    # 1. Top Pill Badge
    badge_text = "✦ K-BEAUTY ORIGINAL · 92% FILTRADO BIO-ACTIVO"
    badge_font = get_font("segoeuib.ttf", 22)
    bbox = draw.textbbox((0, 0), badge_text, font=badge_font)
    bw = bbox[2] - bbox[0] + 44
    bh = bbox[3] - bbox[1] + 18
    bx = (W - bw) // 2
    by = 45
    draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=20, fill=(24, 24, 27, 255))
    draw.text((bx + 22, by + 9), badge_text, font=badge_font, fill=(255, 255, 255, 255))

    # 2. Main Headline
    h1_font = get_font("segoeuib.ttf", 52)
    line1 = "¿PIEL CON BRILLO DE GRASA"
    line2 = "O HIDRATACIÓN REAL?"

    bb1 = draw.textbbox((0, 0), line1, font=h1_font)
    x1 = (W - (bb1[2] - bb1[0])) // 2
    draw.text((x1, 118), line1, font=h1_font, fill=(24, 24, 27, 255))

    bb2 = draw.textbbox((0, 0), line2, font=h1_font)
    x2 = (W - (bb2[2] - bb2[0])) // 2
    w_box = bb2[2] - bb2[0] + 36
    h_box = bb2[3] - bb2[1] + 16
    xbox = x2 - 18
    ybox = 188
    # Contrast amber highlighter box
    draw.rounded_rectangle([xbox, ybox, xbox + w_box, ybox + h_box], radius=10, fill=(245, 158, 11, 255))
    draw.text((x2, 194), line2, font=h1_font, fill=(15, 23, 42, 255))

    # 3. Subheadline
    sub_font = get_font("segoeui.ttf", 26)
    sub_text = "La fórmula coreana ultra-ligera que no se derrite con el calor ni tapa tus poros."
    bbs = draw.textbbox((0, 0), sub_text, font=sub_font)
    xs = (W - (bbs[2] - bbs[0])) // 2
    draw.text((xs, 275), sub_text, font=sub_font, fill=(100, 116, 139, 255))

    # 4. Center Product Jar
    jar_w, jar_h = 510, 510
    jar_resized = clean_jar.resize((jar_w, jar_h), Image.Resampling.LANCZOS)
    jar_x = (W - jar_w) // 2
    jar_y = 440

    # Realistic Ground Shadow
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow)
    s_draw.ellipse([jar_x + 30, jar_y + jar_h - 70, jar_x + jar_w - 30, jar_y + jar_h + 10], fill=(0, 0, 0, 75))
    shadow = shadow.filter(ImageFilter.GaussianBlur(22))
    base.alpha_composite(shadow)

    # Paste Jar
    base.paste(jar_resized, (jar_x, jar_y), jar_resized)

    # 5. Three Floating Callout Feature Cards
    # Card 1: Top Left
    c1_bbox = [60, 410, 420, 540]
    draw_shadow(base, c1_bbox, radius=16, shadow_color=(0,0,0,30), offset=(0,6), blur=12)
    draw = ImageDraw.Draw(base)
    draw.rounded_rectangle(c1_bbox, radius=16, fill=(255, 255, 255, 245), outline=(226, 232, 240, 255), width=2)
    # Content Card 1
    t_font = get_font("segoeuib.ttf", 22)
    p_font = get_font("segoeui.ttf", 18)
    draw.text((80, 428), "💧 92% FILTRADO HELIX", font=t_font, fill=(15, 23, 42, 255))
    draw.text((80, 465), "Repara la barrera cutánea\ny calma rojeces en 10 días.", font=p_font, fill=(71, 85, 105, 255))
    # Line pointer
    draw.line([(420, 475), (490, 490)], fill=(203, 213, 225, 255), width=3)
    draw.ellipse([487, 487, 497, 497], fill=(245, 158, 11, 255))

    # Card 2: Right Middle
    c2_bbox = [660, 580, 1020, 710]
    draw_shadow(base, c2_bbox, radius=16, shadow_color=(0,0,0,30), offset=(0,6), blur=12)
    draw = ImageDraw.Draw(base)
    draw.rounded_rectangle(c2_bbox, radius=16, fill=(255, 255, 255, 245), outline=(226, 232, 240, 255), width=2)
    draw.text((680, 598), "⚡ 0% PESADEZ GRASOSA", font=t_font, fill=(15, 23, 42, 255))
    draw.text((680, 635), "Textura bio-gel acuosa.\nSe absorbe en 15s sin residuo.", font=p_font, fill=(71, 85, 105, 255))
    # Line pointer
    draw.line([(660, 645), (590, 640)], fill=(203, 213, 225, 255), width=3)
    draw.ellipse([583, 635, 593, 645], fill=(245, 158, 11, 255))

    # Card 3: Bottom Left
    c3_bbox = [60, 750, 420, 880]
    draw_shadow(base, c3_bbox, radius=16, shadow_color=(0,0,0,30), offset=(0,6), blur=12)
    draw = ImageDraw.Draw(base)
    draw.rounded_rectangle(c3_bbox, radius=16, fill=(255, 255, 255, 245), outline=(226, 232, 240, 255), width=2)
    draw.text((80, 768), "✨ EFECTO 'GLASS SKIN'", font=t_font, fill=(15, 23, 42, 255))
    draw.text((80, 805), "Luminosidad elástica natural\nsin necesidad de base pesada.", font=p_font, fill=(71, 85, 105, 255))
    # Line pointer
    draw.line([(420, 815), (490, 780)], fill=(203, 213, 225, 255), width=3)
    draw.ellipse([487, 775, 497, 785], fill=(245, 158, 11, 255))

    # 6. Bottom Trust / COD Footer Card
    f_bbox = [50, 1090, 1030, 1280]
    draw_shadow(base, f_bbox, radius=24, shadow_color=(0,0,0,60), offset=(0,10), blur=16)
    draw = ImageDraw.Draw(base)
    draw.rounded_rectangle(f_bbox, radius=24, fill=(15, 23, 42, 255))

    ft_font = get_font("segoeuib.ttf", 32)
    draw.text((85, 1120), "🚚 PAGO CONTRA ENTREGA EN SEDES TEALCA", font=ft_font, fill=(255, 255, 255, 255))

    fs_font = get_font("segoeui.ttf", 22)
    draw.text((85, 1170), "Pides hoy en línea · Retiras y pagas en tu ciudad únicamente al recibir.", font=fs_font, fill=(203, 213, 225, 255))

    fb_font = get_font("segoeuib.ttf", 19)
    draw.text((85, 1220), "🛡️ 100% Original Garantizada   •   ⚡ Despacho en 24-48h   •   📦 Revisas tu paquete", font=fb_font, fill=(245, 158, 11, 255))

    # Save
    out_path = os.path.join(OUTPUT_DIR, "anuncio_1_feature_point_out.jpg")
    base.convert("RGB").save(out_path, quality=95)
    print("Ad 1 successfully saved to:", out_path)

# ==============================================================================
# AD 2: AVATAR CALLOUT + COMPARATIVA (CLIMA TROPICAL / VENEZUELA)
# ==============================================================================
def create_ad_2():
    print("Generating Ad 2: Avatar Callout + Comparativa...")
    W, H = 1080, 1350
    base = Image.new("RGBA", (W, H), (248, 250, 252, 255))
    draw = ImageDraw.Draw(base)

    # 1. Top Urgent Badge
    badge_text = "🔥 ESPECIAL CLIMA TROPICAL DE VENEZUELA"
    badge_font = get_font("segoeuib.ttf", 22)
    bbox = draw.textbbox((0, 0), badge_text, font=badge_font)
    bw = bbox[2] - bbox[0] + 44
    bh = bbox[3] - bbox[1] + 18
    bx = (W - bw) // 2
    by = 45
    draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=20, fill=(220, 38, 38, 255))
    draw.text((bx + 22, by + 9), badge_text, font=badge_font, fill=(255, 255, 255, 255))

    # 2. Headline
    h1_font = get_font("segoeuib.ttf", 50)
    line1 = '"¿TU CARA SUDA GRASA'
    line2 = 'A LAS 11 DE LA MAÑANA?"'

    bb1 = draw.textbbox((0, 0), line1, font=h1_font)
    x1 = (W - (bb1[2] - bb1[0])) // 2
    draw.text((x1, 115), line1, font=h1_font, fill=(15, 23, 42, 255))

    bb2 = draw.textbbox((0, 0), line2, font=h1_font)
    x2 = (W - (bb2[2] - bb2[0])) // 2
    draw.text((x2, 180), line2, font=h1_font, fill=(15, 23, 42, 255))

    # Underline hook
    draw.line([(x2, 245), (x2 + (bb2[2] - bb2[0]), 245)], fill=(220, 38, 38, 255), width=6)

    # 3. Subheadline
    sub_font = get_font("segoeui.ttf", 26)
    sub_text = "Tus poros están asfixiados por cremas pesadas con aceites minerales."
    bbs = draw.textbbox((0, 0), sub_text, font=sub_font)
    xs = (W - (bbs[2] - bbs[0])) // 2
    draw.text((xs, 275), sub_text, font=sub_font, fill=(71, 85, 105, 255))

    # 4. Comparative Cards (Dual Column)
    col_w = 460
    col_h = 430
    y_col = 345

    # Left Box (Cremas Comunes)
    left_x = 55
    draw_shadow(base, [left_x, y_col, left_x + col_w, y_col + col_h], radius=20, shadow_color=(0,0,0,25), blur=12)
    draw = ImageDraw.Draw(base)
    draw.rounded_rectangle([left_x, y_col, left_x + col_w, y_col + col_h], radius=20, fill=(255, 255, 255, 255), outline=(254, 202, 202, 255), width=2)

    # Tag Left
    draw.rounded_rectangle([left_x + 25, y_col + 25, left_x + col_w - 25, y_col + 75], radius=12, fill=(254, 226, 226, 255))
    tag_f = get_font("segoeuib.ttf", 22)
    draw.text((left_x + 75, y_col + 36), "❌ CREMAS COMUNES", font=tag_f, fill=(185, 28, 28, 255))

    # Bullets Left
    b_font = get_font("segoeui.ttf", 21)
    b_left = [
        "• Base densa de aceite mineral",
        "• Tapan poros y sacan puntos",
        "• Se derriten con el calor",
        "• Brillo grasoso al mediodía",
        "• Sensación pesada y sudorosa"
    ]
    cur_y = y_col + 105
    for b in b_left:
        draw.text((left_x + 35, cur_y), b, font=b_font, fill=(100, 116, 139, 255))
        cur_y += 58

    # Right Box (Snail 92 Bio-Gel)
    right_x = 565
    draw_shadow(base, [right_x, y_col, right_x + col_w, y_col + col_h], radius=20, shadow_color=(16,185,129,35), blur=14)
    draw = ImageDraw.Draw(base)
    draw.rounded_rectangle([right_x, y_col, right_x + col_w, y_col + col_h], radius=20, fill=(255, 255, 255, 255), outline=(187, 247, 208, 255), width=3)

    # Tag Right
    draw.rounded_rectangle([right_x + 25, y_col + 25, right_x + col_w - 25, y_col + 75], radius=12, fill=(220, 252, 231, 255))
    draw.text((right_x + 65, y_col + 36), "✅ SNAIL 92™ BIO-GEL", font=tag_f, fill=(21, 128, 61, 255))

    # Bullets Right
    b_bold = get_font("segoeuib.ttf", 21)
    b_right = [
        "• 92% Filtrado Acuoso Helix puro",
        "• 0% Grasas: absorción en 15 seg",
        "• Resiste 38°C sin derretirse",
        "• Efecto Glass Skin sin aceite",
        "• Deja la piel fresca y elástica"
    ]
    cur_y = y_col + 105
    for b in b_right:
        draw.text((right_x + 35, cur_y), b, font=b_bold, fill=(15, 23, 42, 255))
        cur_y += 58

    # 5. Middle Product Texture Banner
    card_mid_bbox = [55, 805, 1025, 1060]
    draw_shadow(base, card_mid_bbox, radius=20, shadow_color=(0,0,0,25), blur=12)
    draw = ImageDraw.Draw(base)
    draw.rounded_rectangle(card_mid_bbox, radius=20, fill=(255, 255, 255, 255), outline=(226, 232, 240, 255), width=2)

    # Place texture image thumbnail
    tex_path = os.path.join(IMAGES_DIR, "manos_abriendo_pote.jpg")
    if os.path.exists(tex_path):
        tex_im = Image.open(tex_path).convert("RGBA")
        tex_crop = tex_im.resize((230, 230), Image.Resampling.LANCZOS)
        # Rounded mask
        mask = Image.new("L", (230, 230), 0)
        ImageDraw.Draw(mask).rounded_rectangle([0, 0, 230, 230], radius=16, fill=255)
        base.paste(tex_crop, (75, 818), mask)

    # Text beside thumbnail
    t_font2 = get_font("segoeuib.ttf", 28)
    p_font2 = get_font("segoeui.ttf", 21)
    draw.text((330, 835), "TEXTURA BIO-GEL AUTO-ABSORBENTE", font=t_font2, fill=(15, 23, 42, 255))
    draw.text((330, 885), "Al tocar la piel se disuelve instantáneamente como agua.\nCrea una película protectora invisible que bloquea el sudor\nsin asfixiar los poros. Ideal para Caracas, Maracaibo y Oriente.", font=p_font2, fill=(71, 85, 105, 255))

    # Small promo pill inside mid card
    draw.rounded_rectangle([330, 995, 620, 1035], radius=10, fill=(254, 243, 199, 255))
    promo_f = get_font("segoeuib.ttf", 18)
    draw.text((345, 1005), "⭐ RECOMENDADO DERMATOLÓGICO", font=promo_f, fill=(180, 83, 9, 255))

    # 6. Bottom COD Offer Banner
    f_bbox = [50, 1090, 1030, 1280]
    draw_shadow(base, f_bbox, radius=24, shadow_color=(0,0,0,60), offset=(0,10), blur=16)
    draw = ImageDraw.Draw(base)
    draw.rounded_rectangle(f_bbox, radius=24, fill=(15, 23, 42, 255))

    ft_font = get_font("segoeuib.ttf", 30)
    draw.text((85, 1120), "🎉 PROMO LANZAMIENTO: COMBO DÚO CON ENVÍO GRATIS", font=ft_font, fill=(255, 255, 255, 255))

    fs_font = get_font("segoeui.ttf", 22)
    draw.text((85, 1170), "Modalidad Pago Contra Entrega en todas las sedes Tealca del país.", font=fs_font, fill=(203, 213, 225, 255))

    fb_font = get_font("segoeuib.ttf", 19)
    draw.text((85, 1220), "🔒 Cero pagos por adelantado   •   📦 Revisas tu pedido   •   💵 Cancelas al recibir", font=fb_font, fill=(74, 222, 128, 255))

    # Save
    out_path = os.path.join(OUTPUT_DIR, "anuncio_2_avatar_comparativa.jpg")
    base.convert("RGB").save(out_path, quality=95)
    print("Ad 2 successfully saved to:", out_path)

# ==============================================================================
# AD 3: RESEÑA REAL / POST-IT AUTÉNTICO (UGLY/AUTHENTIC SOCIAL PROOF)
# ==============================================================================
def create_ad_3():
    print("Generating Ad 3: Reseña Real en Post-It...")
    W, H = 1080, 1350
    base = Image.new("RGBA", (W, H), (243, 241, 237, 255))
    draw = ImageDraw.Draw(base)

    # 1. Top Social Proof Pill
    badge_text = "⭐ 4.9/5 · MÁS DE 1,200 CLIENTAS EN VENEZUELA"
    badge_font = get_font("segoeuib.ttf", 22)
    bbox = draw.textbbox((0, 0), badge_text, font=badge_font)
    bw = bbox[2] - bbox[0] + 44
    bh = bbox[3] - bbox[1] + 18
    bx = (W - bw) // 2
    by = 45
    draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=20, fill=(24, 24, 27, 255))
    draw.text((bx + 22, by + 9), badge_text, font=badge_font, fill=(255, 255, 255, 255))

    # 2. Headline
    h1_font = get_font("georgiab.ttf", 46)
    line1 = "EL SECRETO COREANO QUE"
    line2 = "SÍ AGUANTA EL CALOR DE AQUÍ"

    bb1 = draw.textbbox((0, 0), line1, font=h1_font)
    x1 = (W - (bb1[2] - bb1[0])) // 2
    draw.text((x1, 115), line1, font=h1_font, fill=(24, 24, 27, 255))

    bb2 = draw.textbbox((0, 0), line2, font=h1_font)
    x2 = (W - (bb2[2] - bb2[0])) // 2
    
    # Highlighter behind line 2
    w_hl = bb2[2] - bb2[0] + 28
    h_hl = bb2[3] - bb2[1] + 10
    draw.rectangle([x2 - 14, 185, x2 - 14 + w_hl, 185 + h_hl], fill=(254, 240, 138, 255))
    draw.text((x2, 180), line2, font=h1_font, fill=(24, 24, 27, 255))

    # 3. The Iconic Post-It Note
    post_w = 880
    post_h = 490
    post_x = (W - post_w) // 2
    post_y = 270

    # Post-it shadow
    draw_shadow(base, [post_x, post_y, post_x + post_w, post_y + post_h], radius=12, shadow_color=(0,0,0,35), offset=(0,12), blur=18)
    draw = ImageDraw.Draw(base)

    # Post-it background (pastel yellow)
    draw.rounded_rectangle([post_x, post_y, post_x + post_w, post_y + post_h], radius=12, fill=(254, 249, 195, 255), outline=(253, 230, 138, 255), width=2)

    # Scotch tape at top center
    tape_w, tape_h = 160, 44
    tape_x = (W - tape_w) // 2
    tape_y = post_y - 20
    draw.rounded_rectangle([tape_x, tape_y, tape_x + tape_w, tape_y + tape_h], radius=4, fill=(255, 255, 255, 160), outline=(241, 245, 249, 180), width=1)

    # 5 Stars on Post-it
    stars_f = get_font("segoeuib.ttf", 36)
    draw.text((post_x + 50, post_y + 45), "★★★★★", font=stars_f, fill=(234, 179, 8, 255))

    v_font = get_font("segoeuib.ttf", 18)
    draw.text((post_x + 220, post_y + 58), "COMPRA VERIFICADA TEALCA · HACE 3 DÍAS", font=v_font, fill=(100, 116, 139, 255))

    # Post-it handwritten-style review text
    # Using Segoe Print Bold for ultra authentic look
    note_font = get_font("segoeprb.ttf", 25)
    note_lines = [
        "\"Llevaba años botando plata en cremas caras que solo",
        "me hacían sudar manteca al mediodía en la calle.",
        "Con este gel coreano la piel se bebe TODO en 10 segundos.",
        "Tengo la cara lisa y luminosa como filtro de TikTok, pero",
        "sin una gota de grasa ni base pesada.",
        "¡Ya le pedí el segundo pote para mi mamá!\"",
    ]
    cur_ny = post_y + 115
    for nline in note_lines:
        draw.text((post_x + 50, cur_ny), nline, font=note_font, fill=(30, 41, 59, 255))
        cur_ny += 48

    # Signature
    sig_font = get_font("segoeuib.ttf", 21)
    draw.text((post_x + 50, post_y + 425), "— Mariana R. (Caracas, Distrito Capital)", font=sig_font, fill=(71, 85, 105, 255))

    # 4. Product Duo Imagery & Trust Callout (Below Post-it)
    jar_thumb_w, jar_thumb_h = 290, 290
    jar_thumb = clean_jar.resize((jar_thumb_w, jar_thumb_h), Image.Resampling.LANCZOS)
    base.paste(jar_thumb, (90, 770), jar_thumb)

    # Result Box / Product stats beside jar
    box_r_x = 420
    box_r_y = 785
    box_r_w = 560
    box_r_h = 260
    draw_shadow(base, [box_r_x, box_r_y, box_r_x + box_r_w, box_r_y + box_r_h], radius=18, shadow_color=(0,0,0,25), blur=10)
    draw = ImageDraw.Draw(base)
    draw.rounded_rectangle([box_r_x, box_r_y, box_r_x + box_r_w, box_r_y + box_r_h], radius=18, fill=(255, 255, 255, 255), outline=(226, 232, 240, 255), width=2)

    t_box_f = get_font("segoeuib.ttf", 24)
    p_box_f = get_font("segoeui.ttf", 20)
    draw.text((box_r_x + 30, box_r_y + 25), "SNAIL 92™ ALL-IN-ONE CREAM", font=t_box_f, fill=(15, 23, 42, 255))
    draw.text((box_r_x + 30, box_r_y + 68), "✔ 92% Filtrado Bio-Activo de Mucina Helix\n✔ Regeneración celular sin tapar poros\n✔ Ácido Hialurónico + Alantoína pura\n✔ Fórmula 100% libre de parabenos y aceites", font=p_box_f, fill=(51, 65, 85, 255))

    # Small gold ribbon
    draw.rounded_rectangle([box_r_x + 30, box_r_y + 195, box_r_x + 340, box_r_y + 235], radius=8, fill=(254, 243, 199, 255))
    draw.text((box_r_x + 45, box_r_y + 203), "✨ EL TOP #1 EN COREA DEL SUR", font=get_font("segoeuib.ttf", 17), fill=(180, 83, 9, 255))

    # 5. Bottom COD Bar
    f_bbox = [50, 1090, 1030, 1280]
    draw_shadow(base, f_bbox, radius=24, shadow_color=(0,0,0,60), offset=(0,10), blur=16)
    draw = ImageDraw.Draw(base)
    draw.rounded_rectangle(f_bbox, radius=24, fill=(15, 23, 42, 255))

    ft_font = get_font("segoeuib.ttf", 30)
    draw.text((85, 1120), "🛡️ CERO RIESGO: NO TRANSFIERES NADA POR ADELANTADO", font=ft_font, fill=(56, 189, 248, 255))

    fs_font = get_font("segoeui.ttf", 22)
    draw.text((85, 1170), "Modalidad Contra Entrega: Retiras y cancelas en tu agencia Tealca más cercana.", font=fs_font, fill=(203, 213, 225, 255))

    fb_font = get_font("segoeuib.ttf", 19)
    draw.text((85, 1220), "💵 Reciben Efectivo ($) o Pago Móvil (Bs) al recibir  •  📦 Envíos asegurados a todo el país", font=fb_font, fill=(245, 158, 11, 255))

    # Save
    out_path = os.path.join(OUTPUT_DIR, "anuncio_3_resena_postit.jpg")
    base.convert("RGB").save(out_path, quality=95)
    print("Ad 3 successfully saved to:", out_path)

if __name__ == "__main__":
    create_ad_1()
    create_ad_2()
    create_ad_3()
    print("All 3 static ads generated successfully in:", OUTPUT_DIR)

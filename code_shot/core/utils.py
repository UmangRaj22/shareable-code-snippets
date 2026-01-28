import io
import os
from pygments import highlight
from pygments.lexers import get_lexer_by_name, guess_lexer
from pygments.formatters import ImageFormatter
from PIL import Image, ImageDraw, ImageFont

def create_code_image(code, lang, theme, line_numbers, font_name, mac_buttons, bg_gradient, padding, watermark, watermark_text):
    # 1. Lexer
    try:
        lexer = get_lexer_by_name(lang)
    except:
        lexer = guess_lexer(code)

    # 2. Formatter
    formatter = ImageFormatter(
        style=theme,
        line_numbers=line_numbers,
        font_name=font_name if font_name else None,
        font_size=24,
        line_pad=12,
        line_number_bg=None,
    )
    
    code_img_data = highlight(code, lexer, formatter)
    code_img = Image.open(io.BytesIO(code_img_data)).convert("RGBA")

    # 3. Background
    bg_color = formatter.style.background_color
    header_height = 50
    radius = 18 
    win_w = code_img.width + (padding * 2)
    win_h = code_img.height + padding + header_height
    

    window = Image.new('RGBA', (win_w, win_h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(window)
    draw.rounded_rectangle((0, 0, win_w, win_h), radius=radius, fill=bg_color)

    # 4. Mac Buttons
    if mac_buttons:
        btn_y = 18
        draw.ellipse((20, btn_y, 34, btn_y + 14), fill="#FF5F56") 
        draw.ellipse((42, btn_y, 56, btn_y + 14), fill="#FFBD2E") 
        draw.ellipse((64, btn_y, 78, btn_y + 14), fill="#27C93F") 

        try:
            title_font = ImageFont.truetype("arial.ttf", 18)
            title_color = "#888888" if bg_color.startswith('#f') else "#555555"
            title = "Untitled-1"
            bbox = draw.textbbox((0, 0), title, font=title_font)
            tw = bbox[2] - bbox[0]
            draw.text(((win_w - tw) // 2, 15), title, fill=title_color, font=title_font)
        except:
            pass

    
    window.paste(code_img, (padding, header_height), code_img)

    
    margin = 100
    canvas_w, canvas_h = win_w + (margin * 2), win_h + (margin * 2)
    
   
    canvas = Image.new('RGB', (canvas_w, canvas_h), "#0d1117") 
    c_draw = ImageDraw.Draw(canvas)

    
    grid_spacing = 30
    dot_color = "#1f242c"
    for ox in range(0, canvas_w, grid_spacing):
        for oy in range(0, canvas_h, grid_spacing):
            c_draw.ellipse((ox, oy, ox+2, oy+2), fill=dot_color)

    
    x, y = (canvas_w - win_w) // 2, (canvas_h - win_h) // 2
    shadow = Image.new('RGBA', (win_w, win_h), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow)
    
    s_draw.rounded_rectangle((0, 0, win_w, win_h), radius=radius, fill=(0, 0, 0, 60))
    
    canvas.paste(shadow, (x + 15, y + 15), shadow)
    canvas.paste(window, (x, y), window)

    # Watermark
    if watermark and watermark_text:
        try:
            wm_font = ImageFont.truetype("seguiemj.ttf", 20)
            wm_bbox = c_draw.textbbox((0, 0), watermark_text, font=wm_font)
            wm_w = wm_bbox[2] - wm_bbox[0]
            c_draw.text((canvas_w - wm_w - 50, canvas_h - 60), watermark_text, font=wm_font, embedded_color=True)
        except:
            c_draw.text((canvas_w - 150, canvas_h - 60), watermark_text, fill="#444")

    output = io.BytesIO()
    canvas.save(output, format='PNG')
    output.seek(0)
    return output
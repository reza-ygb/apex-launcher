#!/usr/bin/env python3
"""
🎨 آیکون ساز برای BULLETPROOF LAUNCHER
می‌سازد: یک آیکون 256x256 زیبا و حرفه‌ای
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_bulletproof_icon():
    """ایجاد آیکون زیبا برای launcher"""
    
    # ابعاد آیکون
    size = 256
    
    # ایجاد تصویر با gradient زمینه
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Gradient background - آبی تا بنفش
    for y in range(size):
        ratio = y / size
        r = int(102 + (118 - 102) * ratio)  # 667eea to 764ba2
        g = int(126 + (75 - 126) * ratio)
        b = int(234 + (162 - 234) * ratio)
        
        for x in range(size):
            x_ratio = x / size
            final_r = int(r + (r * 0.1 * x_ratio))
            final_g = int(g + (g * 0.1 * x_ratio))
            final_b = int(b + (b * 0.1 * x_ratio))
            
            # کنترل رنگ در محدوده 0-255
            final_r = max(0, min(255, final_r))
            final_g = max(0, min(255, final_g))
            final_b = max(0, min(255, final_b))
            
            img.putpixel((x, y), (final_r, final_g, final_b, 255))
    
    # دایره اصلی (shield)
    shield_radius = 90
    center = size // 2
    
    # سایه برای shield
    shadow_offset = 8
    draw.ellipse([
        center - shield_radius + shadow_offset,
        center - shield_radius + shadow_offset,
        center + shield_radius + shadow_offset,
        center + shield_radius + shadow_offset
    ], fill=(0, 0, 0, 60))
    
    # Shield اصلی - دایره سفید با حاشیه
    draw.ellipse([
        center - shield_radius,
        center - shield_radius,
        center + shield_radius,
        center + shield_radius
    ], fill=(255, 255, 255, 240), outline=(52, 152, 219, 255), width=6)
    
    # دایره داخلی - آبی روشن
    inner_radius = 70
    draw.ellipse([
        center - inner_radius,
        center - inner_radius,
        center + inner_radius,
        center + inner_radius
    ], fill=(52, 152, 219, 200))
    
    # نماد rocket در وسط
    rocket_points = [
        # نوک راکت
        (center, center - 40),
        # بدنه راکت
        (center - 15, center - 20),
        (center - 15, center + 10),
        (center - 10, center + 20),
        (center - 5, center + 25),
        (center + 5, center + 25),
        (center + 10, center + 20),
        (center + 15, center + 10),
        (center + 15, center - 20),
    ]
    draw.polygon(rocket_points, fill=(255, 255, 255, 255))
    
    # شعله راکت
    flame_points = [
        (center - 8, center + 20),
        (center, center + 40),
        (center + 8, center + 20),
    ]
    draw.polygon(flame_points, fill=(255, 87, 51, 255))
    
    # نقاط تزئینی دور shield
    star_radius = 110
    for i in range(8):
        angle = i * 45  # هر 45 درجه
        import math
        x = center + star_radius * math.cos(math.radians(angle))
        y = center + star_radius * math.sin(math.radians(angle))
        
        # ستاره کوچک
        star_size = 8
        star_points = []
        for j in range(5):
            star_angle = angle + j * 72
            star_x = x + star_size * math.cos(math.radians(star_angle))
            star_y = y + star_size * math.sin(math.radians(star_angle))
            star_points.append((star_x, star_y))
            
            # نقطه داخلی
            inner_angle = angle + j * 72 + 36
            inner_star_size = star_size * 0.4
            inner_x = x + inner_star_size * math.cos(math.radians(inner_angle))
            inner_y = y + inner_star_size * math.sin(math.radians(inner_angle))
            star_points.append((inner_x, inner_y))
        
        if len(star_points) >= 6:  # حداقل 3 نقطه برای polygon
            draw.polygon(star_points[:6], fill=(255, 255, 255, 200))
    
    # متن "BP" (BulletProof) در پایین
    try:
        # تلاش برای استفاده از فونت سیستم
        font_size = 24
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    text = "BP"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    text_x = center - text_width // 2
    text_y = center + 60
    
    # سایه متن
    draw.text((text_x + 2, text_y + 2), text, fill=(0, 0, 0, 128), font=font)
    # متن اصلی
    draw.text((text_x, text_y), text, fill=(255, 255, 255, 255), font=font)
    
    return img

def main():
    """ایجاد و ذخیره آیکون"""
    print("🎨 Creating Bulletproof Launcher icon...")
    
    try:
        icon = create_bulletproof_icon()
        icon_path = "/home/reza/code/bulletproof_launcher_icon.png"
        icon.save(icon_path, "PNG")
        print(f"✅ Icon saved to: {icon_path}")
        
        # ایجاد سایزهای مختلف
        sizes = [16, 32, 48, 64, 128]
        for size in sizes:
            resized = icon.resize((size, size), Image.Resampling.LANCZOS)
            size_path = f"/home/reza/code/bulletproof_launcher_icon_{size}.png"
            resized.save(size_path, "PNG")
            print(f"✅ {size}x{size} icon saved")
            
    except Exception as e:
        print(f"❌ Error creating icon: {e}")
        # ایجاد آیکون ساده اگر PIL کار نکرد
        create_simple_icon()

def create_simple_icon():
    """ایجاد آیکون ساده با SVG"""
    print("🎨 Creating simple SVG icon...")
    
    svg_content = '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="256" height="256" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#667eea;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#764ba2;stop-opacity:1" />
        </linearGradient>
        <radialGradient id="shield" cx="50%" cy="50%">
            <stop offset="0%" style="stop-color:#ffffff;stop-opacity:0.9" />
            <stop offset="100%" style="stop-color:#3498db;stop-opacity:0.8" />
        </radialGradient>
    </defs>
    
    <!-- Background -->
    <rect width="256" height="256" fill="url(#bg)" rx="32"/>
    
    <!-- Shield -->
    <circle cx="128" cy="128" r="90" fill="url(#shield)" stroke="#2980b9" stroke-width="6"/>
    
    <!-- Rocket -->
    <polygon points="128,88 113,108 113,138 118,148 123,153 133,153 138,148 143,138 143,108" 
             fill="#ffffff"/>
    
    <!-- Rocket flame -->
    <polygon points="120,148 128,168 136,148" fill="#ff5733"/>
    
    <!-- Stars around -->
    <g fill="#ffffff" opacity="0.7">
        <polygon points="64,64 67,70 73,67 70,73 76,76 70,79 73,85 67,82 64,88 61,82 55,85 58,79 52,76 58,73 55,67 61,70"/>
        <polygon points="192,64 195,70 201,67 198,73 204,76 198,79 201,85 195,82 192,88 189,82 183,85 186,79 180,76 186,73 183,67 189,70"/>
        <polygon points="64,192 67,198 73,195 70,201 76,204 70,207 73,213 67,210 64,216 61,210 55,213 58,207 52,204 58,201 55,195 61,198"/>
        <polygon points="192,192 195,198 201,195 198,201 204,204 198,207 201,213 195,210 192,216 189,210 183,213 186,207 180,204 186,201 183,195 189,198"/>
    </g>
    
    <!-- Text BP -->
    <text x="128" y="200" text-anchor="middle" font-family="Arial" font-size="24" font-weight="bold" fill="#ffffff">BP</text>
</svg>'''
    
    with open("/home/reza/code/bulletproof_launcher_icon.svg", "w") as f:
        f.write(svg_content)
    print("✅ SVG icon created")

if __name__ == "__main__":
    main()

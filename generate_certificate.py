from pathlib import Path
import fitz

# for the training title, it's almost impossible to replace CLEANLY. Ensure to use an original certificate with the proper training video name.

def name_replace(current_name, new_name):
        name_coordinates = page.search_for(current_name)
        name_rect = name_coordinates[0]
        page.draw_rect(name_rect, color=(1,1,1), fill=(1,1,1), width=1)
        page.insert_textbox(name_rect + (-20, 0, 20, 20), new_name, fontsize=27, fontname='helvetica-bold', color=(0,0,0), align=1)

def date_replace(current_date, new_date):
    current_date_coords = page.search_for(current_date)
    current_date_rect = current_date_coords[0]
    page.draw_rect(current_date_rect, color=(1,1,1), fill=(1,1,1), width=1)
    page.insert_textbox(current_date_rect + (-20, -20, 20, 20), new_date, fontsize=17, fontname='heit', color=(0,0,0), align=1)

def replace_icon(replacement):
    try:
        icon = page.get_image_bbox(images[0])
        page.draw_rect(icon, color=(1,1,1), fill=(1,1,1), width=1)
        page.insert_image(icon, filename=replacement)
    except IndexError:
        print("No image was found")

try:
    cert = fitz.open(Path(r"C:\Users\RonJavellana\Downloads\PDF_Files\certificate.pdf"))
except FileNotFoundError:
    print('No training certifificate was found')

page = cert[0]

name_replace("Anita Bath", "John Doe")
date_replace("12 May, 2025", "15 Feb, 2025")

images = page.get_images(full=True)
replace_icon(Path(r"C:\Users\RonJavellana\Downloads\test.png"))

cert.save(Path(r"C:\Users\RonJavellana\Downloads\PDF_Files\GeneratedCerts\new.pdf"))
print("Training Certificate(s) generated")

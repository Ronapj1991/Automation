from pathlib import Path
import fitz
import csv

# for the training title, it's almost impossible to replace CLEANLY. Ensure to use an original certificate with the proper training video name.

def name_replace(current_name, new_name):
        name_coordinates = page.search_for(current_name)
        name_rect = name_coordinates[0]
        page.draw_rect(name_rect, color=(1,1,1), fill=(1,1,1), width=1)
        #for longer names, the addition on the textbox need to be bigger
        if len(new_name) > 20:
            page.insert_textbox(name_rect + (-90, -50, 90, 50), new_name, fontsize=27, fontname='helvetica-bold', color=(0,0,0), align=1)
        else:
            page.insert_textbox(name_rect + (-90, 0, 90, 90), new_name, fontsize=27, fontname='helvetica-bold', color=(0,0,0), align=1)

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

# detect names from campaign participants CSV and pass to name_replace
with open(Path(r"C:\Users\RonJavellana\Downloads\campaign_report_All Staff SAT 2025.csv"), mode='r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        cert = fitz.open(Path(r"C:\Users\RonJavellana\Downloads\PDF_Files\certificate.pdf"))

        page = cert[0]
        
        images = page.get_images(full=True)

        full_name = row['Name'].strip()

        name_replace("Anita Bath", full_name)
        date_replace("12 May, 2025", "15 Feb, 2025")
        replace_icon(Path(r"C:\Users\RonJavellana\Downloads\test.png"))
        safe_name = full_name.replace(" ", "_")
        cert.save(Path(fr"C:\Users\RonJavellana\Downloads\PDF_Files\GeneratedCerts\{safe_name}.pdf"))
        cert.close()

print("Training Certificate(s) generated")

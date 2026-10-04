import os
import win32com.client
import pypdfium2
from PIL import Image
import numpy as np

docx_path = os.path.abspath('CE4023_HYDRAULIC_FIELD_STUDY/OUTPUT/CE4023_Hydraulic_Structures_Field_Report.docx')
pdf_path = os.path.abspath('CE4023_HYDRAULIC_FIELD_STUDY/OUTPUT/CE4023_Hydraulic_Structures_Field_Report.pdf')
inspect_dir = os.path.abspath('scratch_inspect_pages')
os.makedirs(inspect_dir, exist_ok=True)

print("Opening Word Application to export PDF...")
word = win32com.client.Dispatch('Word.Application')
word.Visible = False
try:
    doc = word.Documents.Open(docx_path)
    print("Document opened successfully.")
    doc.ExportAsFixedFormat(pdf_path, 17) # 17 = wdExportFormatPDF
    doc.Close(False)
    print(f"Exported PDF successfully to: {pdf_path}")
finally:
    word.Quit()

# Inspect with pypdfium2
pdf = pypdfium2.PdfDocument(pdf_path)
total_pages = len(pdf)
print(f"Total pages in generated document: {total_pages}")

# Analyze each page
issues_found = []

for page_idx in range(total_pages):
    page = pdf[page_idx]
    # Render at 150 DPI (scale ~ 2.08)
    img = page.render(scale=2.0).to_pil()
    w, h = img.size
    
    # Save first 5 pages, last 3 pages, and any page with figures/tables
    page_num = page_idx + 1
    out_img_path = os.path.join(inspect_dir, f"page_{page_num:02d}.png")
    if page_num <= 5 or page_num >= total_pages - 3 or page_num % 5 == 0:
        img.save(out_img_path)
    
    # Check for dark pixels near the left edge (< 2.0 cm) to ensure margin is respected
    arr = np.array(img.convert('L'))
    
    # Left border is expected around x = 2.2 cm to 2.4 cm
    # Text should start at x >= 2.45 cm (left margin is 2.5 cm)
    # Right border is around x = 20.1 cm to 20.3 cm
    # Top border is around y = 0.7 cm to 0.9 cm
    # Bottom border is around y = 29.3 cm to 29.5 cm
    
    # Let's check if there are horizontal lines representing the box border
    horiz_top = np.sum(arr[int(0.02 * h):int(0.04 * h), :] < 50, axis=1)
    has_top_border = np.any(horiz_top > 400)
    
    horiz_bot = np.sum(arr[int(0.97 * h):int(0.995 * h), :] < 50, axis=1)
    has_bot_border = np.any(horiz_bot > 400)
    
    # Check for overflow outside right border (> 20.3 cm)
    # Right edge is at width w, 20.4 cm is (20.4 / 21.0) * w
    right_cutoff = int((20.35 / 21.0) * w)
    overflow_right = np.sum(arr[:, right_cutoff:] < 100)
    
    # Check for overflow outside left border (< 2.2 cm)
    left_cutoff = int((2.20 / 21.0) * w)
    overflow_left = np.sum(arr[:, :left_cutoff] < 100)
    
    if not has_top_border or not has_bot_border:
        issues_found.append(f"Page {page_num}: Missing top or bottom border line!")
    if overflow_right > 50:
        issues_found.append(f"Page {page_num}: Content or line extending past right margin border ({overflow_right} dark px)!")
    if overflow_left > 50:
        issues_found.append(f"Page {page_num}: Content or line extending past left margin border ({overflow_left} dark px)!")

print("\n--- Visual Inspection Summary ---")
print(f"Total pages scanned: {total_pages}")
if not issues_found:
    print("ALL PAGES PASSED! Box border is present, margins respected, no overflow detected.")
else:
    print(f"Issues detected on {len(issues_found)} checks:")
    for issue in issues_found[:10]:
        print("  -", issue)

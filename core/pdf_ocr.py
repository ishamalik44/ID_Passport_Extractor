import fitz
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

def extract_text_from_pdf(pdf_path):

    doc = fitz.open(pdf_path)

    full_text = ""

    for page_num in range(len(doc)):

        page = doc[page_num]

        text = page.get_text()

        if text.strip():

            full_text += text + "\n"

        else:

            pix = page.get_pixmap()

            img_path = f"temp_page_{page_num}.png"

            pix.save(img_path)

            image = Image.open(img_path)

            full_text += pytesseract.image_to_string(image)

    return full_text
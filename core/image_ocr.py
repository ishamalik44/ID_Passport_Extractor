import easyocr
import pytesseract

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# Reader sirf ek baar load hoga
reader = easyocr.Reader(['en'], gpu=False)


def extract_text_from_image(image_path):

    results = reader.readtext(
        image_path,
        detail=0
    )

    text = "\n".join(results)

    print("\n===== EASYOCR OUTPUT =====\n")
    print(text)

    return text
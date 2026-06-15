# ID & Passport Data Extractor

A desktop application built with Python and CustomTkinter that extracts information from ID cards and passports using OCR (EasyOCR).

## Features

* Upload image documents

  * JPG
  * JPEG
  * PNG
  * BMP
  * TIFF
  * WEBP

* Automatic document detection

  * CNIC
  * Passport

* Extracts fields such as:

  * Document Type
  * Passport Number
  * Identity Number
  * Name
  * Father Name
  * Gender
  * Nationality
  * Date of Birth
  * Issue Date
  * Expiry Date
  * Place of Birth

* Modern Dark Theme GUI

* Document Preview

* Structured Data Extraction

* Export to Excel (.xlsx)

* Export to CSV (.csv)

* Export to JSON (.json)

## Technologies Used

* Python
* CustomTkinter
* EasyOCR
* Pandas
* Pillow
* OpenPyXL

## Project Structure

```text
ID_Passport_Extractor/
│
├── core/
│   ├── image_ocr.py
│   ├── field_extractor.py
│   └── exporter.py
│
├── gui/
│   └── main_window.py
│
├── exports/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/ishamalik44/ID_Passport_Extractor.git
```

Move to project directory:

```bash
cd ID_Passport_Extractor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

## Usage

1. Launch the application.
2. Upload an image of a CNIC or Passport.
3. Click **Extract Fields**.
4. View extracted information in the table.
5. Export data to Excel, CSV, or JSON format.

## Export Formats

The application supports:

* Excel (.xlsx)
* CSV (.csv)
* JSON (.json)



## Future Improvements

* PDF Support
* Multi-language OCR
* Batch Processing
* AI-Based Field Detection
* Face Detection
* QR Code Extraction

## Author

**Isha Maqbool**

Software Engineering Student



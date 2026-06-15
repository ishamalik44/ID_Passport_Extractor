import re


def extract_fields(text):

    data = {}

    text_upper = text.upper()

    # ==================================================
    # PASSPORT DETECTION
    # ==================================================

    if "PASSPORT" in text_upper:

        data["Document Type"] = "Passport"

        # ----------------------------------
        # Passport Number
        # Example: BC0331811
        # ----------------------------------

        passport_match = re.search(
            r'\b[A-Z]{2}\d{7}\b',
            text
        )

        if passport_match:
            data["Passport Number"] = passport_match.group()

        # ----------------------------------
        # MRZ Parsing
        # Example:
        # P<PAKMAQBOOL<<UZAIR
        # ----------------------------------

        mrz_match = re.search(
            r'P<PAK([A-Z]+)<<([A-Z]+)',
            text
        )

        if mrz_match:

            data["Surname"] = mrz_match.group(1)

            data["Given Name"] = mrz_match.group(2)

        # ----------------------------------
        # Nationality
        # ----------------------------------

        if "PAKISTANI" in text_upper:
            data["Nationality"] = "PAKISTANI"

        elif "BRITISH CITIZEN" in text_upper:
            data["Nationality"] = "BRITISH CITIZEN"

        # ----------------------------------
        # Dates
        # ----------------------------------

        dates = re.findall(
            r'\d{2}\s+[A-Z]{3}\s+\d{4}',
            text
        )

        if len(dates) >= 1:
            data["Date Of Birth"] = dates[0]

        if len(dates) >= 2:
            data["Issue Date"] = dates[1]

        if len(dates) >= 3:
            data["Expiry Date"] = dates[2]

        # ----------------------------------
        # Gender
        # ----------------------------------

        gender_match = re.search(
            r'\n(M|F)\n',
            text
        )

        if gender_match:
            data["Gender"] = gender_match.group(1)

        # ----------------------------------
        # Place Of Birth
        # ----------------------------------

        place_match = re.search(
            r'([A-Z]+,\s*PAK)',
            text
        )

        if place_match:
            data["Place Of Birth"] = place_match.group()

        return data

    # ==================================================
    # CNIC DETECTION
    # ==================================================

    elif "NATIONAL IDENTITY CARD" in text_upper:

        data["Document Type"] = "CNIC"

        # ----------------------------------
        # CNIC Number
        # ----------------------------------

        cnic_match = re.search(
            r'\d{5}-\d{7}-\d',
            text
        )

        if cnic_match:
            data["Identity Number"] = cnic_match.group()

        # ----------------------------------
        # Name
        # ----------------------------------

        name_match = re.search(
            r'Name\s*\n([A-Za-z ]+)',
            text,
            re.IGNORECASE
        )

        if name_match:
            data["Name"] = name_match.group(1).strip()

        # ----------------------------------
        # Father Name
        # ----------------------------------

        father_match = re.search(
            r'Father Name\s*\n([A-Za-z ]+)',
            text,
            re.IGNORECASE
        )

        if father_match:
            data["Father Name"] = father_match.group(1).strip()

        # ----------------------------------
        # Gender
        # ----------------------------------

        gender_match = re.search(
            r'\n(M|F)\n',
            text
        )

        if gender_match:
            data["Gender"] = gender_match.group(1)

        # ----------------------------------
        # Date Of Birth
        # ----------------------------------

        dob_match = re.search(
            r'(\d{2}[.,]\d{2}[.,]\d{4})',
            text
        )

        if dob_match:

            data["Date Of Birth"] = (
                dob_match.group(1)
                .replace(",", ".")
            )

        # ----------------------------------
        # Dates
        # ----------------------------------

        dates = re.findall(
            r'\d{2}[.,]\d{2}[.,]\d{4}',
            text
        )

        if len(dates) >= 2:

            data["Date Of Issue"] = (
                dates[1]
                .replace(",", ".")
            )

        if len(dates) >= 3:

            data["Date Of Expiry"] = (
                dates[2]
                .replace(",", ".")
            )

        return data

    # ==================================================
    # UNKNOWN DOCUMENT
    # ==================================================

    else:

        data["Document Type"] = "Unknown"

        return data
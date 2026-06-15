import pandas as pd
import json
import os

desktop = os.path.join(
    os.path.expanduser("~"),
    "Desktop"
)

def export_excel(data):

    df = pd.DataFrame(
        list(data.items()),
        columns=["Field", "Value"]
    )

    file_path = os.path.join(
        desktop,
        "result.xlsx"
    )

    df.to_excel(
        file_path,
        index=False
    )

    return file_path


def export_csv(data):

    df = pd.DataFrame(
        list(data.items()),
        columns=["Field", "Value"]
    )

    file_path = os.path.join(
        desktop,
        "result.csv"
    )

    df.to_csv(
        file_path,
        index=False
    )

    return file_path


def export_json(data):

    file_path = os.path.join(
        desktop,
        "result.json"
    )

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )

    return file_path
import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image

from core.image_ocr import extract_text_from_image
from core.field_extractor import extract_fields as parse_fields
from core.exporter import (
    export_excel,
    export_csv,
    export_json
)
from tkinter import ttk

class MainWindow(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("ID & Passport Data Extractor")
        self.geometry("1300x750")
        self.minsize(1100, 650)

        self.selected_file = None
        self.extracted_data = {}

        # ==========================
        # GRID
        # ==========================

        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # ==========================
        # LEFT PANEL
        # ==========================

        self.preview_frame = ctk.CTkFrame(self)

        self.preview_frame.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        self.preview_title = ctk.CTkLabel(
            self.preview_frame,
            text="Document Preview",
            font=("Arial", 24, "bold")
        )

        self.preview_title.pack(pady=15)

        self.image_label = ctk.CTkLabel(
            self.preview_frame,
            text=""
        )

        self.image_label.pack(
            pady=10,
            expand=True
        )

        # Upload Button

        self.upload_btn = ctk.CTkButton(
            self.preview_frame,
            text="📂 Upload Document",
            height=45,
            command=self.upload_file
        )

        self.upload_btn.pack(
            padx=20,
            pady=10,
            fill="x"
        )

        # Extract Button

        self.extract_btn = ctk.CTkButton(
            self.preview_frame,
            text="⚡ Extract Fields",
            height=45,
            fg_color="green",
            command=self.extract_document
        )

        self.extract_btn.pack(
            padx=20,
            pady=10,
            fill="x"
        )

        # ==========================
        # RIGHT PANEL
        # ==========================

        self.table_frame = ctk.CTkFrame(self)

        self.table_frame.grid(
            row=0,
            column=1,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        self.fields_title = ctk.CTkLabel(
            self.table_frame,
            text="Extracted Fields",
            font=("Arial", 24, "bold")
        )

        self.fields_title.pack(pady=15)

       # ==========================
# TABLE
# ==========================

        columns = ("Field", "Value")

        self.tree = ttk.Treeview(
            self.table_frame,
            columns=columns,
            show="headings",
            height=15
        )

        self.tree.heading(
            "Field",
            text="Field Name"
        )

        self.tree.heading(
            "Value",
            text="Value"
        )

        self.tree.column(
            "Field",
            width=180
        )

        self.tree.column(
            "Value",
            width=300
        )

        self.tree.pack(
            padx=20,
            pady=10,
            fill="both",
            expand=True
        )


        style = ttk.Style()

        style.theme_use("clam")

        style.configure(
                "Treeview",
                background="#1f2937",
                foreground="white",
                fieldbackground="#1f2937",
                rowheight=30
            )

        style.configure(
                "Treeview.Heading",
                background="#111827",
                foreground="white",
                font=("Arial", 11, "bold")
            ) 

        # ==========================
        # EXPORT BUTTONS
        # ==========================

        self.export_frame = ctk.CTkFrame(
            self.table_frame,
            fg_color="transparent"
        )

        self.export_frame.pack(
            padx=20,
            pady=10,
            fill="x"
        )

        self.export_excel_btn = ctk.CTkButton(
        self.export_frame,
        text="📊 Excel",
        command=self.export_excel_file
)

        self.export_excel_btn.pack(
            side="left",
            padx=5,
            expand=True,
            fill="x"
        )

        self.export_csv_btn = ctk.CTkButton(
        self.export_frame,
        text="📄 CSV",
        command=self.export_csv_file
    )

        self.export_csv_btn.pack(
            side="left",
            padx=5,
            expand=True,
            fill="x"
        )

        self.export_json_btn = ctk.CTkButton(
        self.export_frame,
        text="🗂 JSON",
        command=self.export_json_file
    )

        self.export_json_btn.pack(
            side="left",
            padx=5,
            expand=True,
            fill="x"
        )

    # ==================================
    # UPLOAD FILE
    # ==================================

    def upload_file(self):

        file_path = filedialog.askopenfilename(
            title="Select Document",
            filetypes=[
                (
                    "Supported Files",
                    "*.jpg *.jpeg *.png *.bmp *.tif *.tiff *.webp *.pdf"
                )
            ]
        )

        if not file_path:
            return

        self.selected_file = file_path

        try:

            if not file_path.lower().endswith(".pdf"):

                image = Image.open(file_path)

                preview = ctk.CTkImage(
                    light_image=image,
                    dark_image=image,
                    size=(650, 450)
                )

                self.image_label.configure(
                    image=preview,
                    text=""
                )

                self.image_label.image = preview

            messagebox.showinfo(
                "Success",
                "Document uploaded successfully."
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # ==================================
    # EXTRACT
    # ==================================

    def extract_document(self):

        if not self.selected_file:

            messagebox.showwarning(
                "Warning",
                "Please upload a document first."
            )

            return

        try:

            text = extract_text_from_image(
                self.selected_file
            )

            data = parse_fields(text)

            self.extracted_data = data

            for item in self.tree.get_children():
                self.tree.delete(item)

            for key, value in data.items():

                self.tree.insert(
                    "",
                    "end",
                    values=(key, value)
                )
            messagebox.showinfo(
                "Success",
                f"{len(data)} fields extracted successfully."
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # ==================================
    # EXPORT
    # ==================================

   

    def export_excel_file(self):

        if not self.extracted_data:

            messagebox.showwarning(
                "Warning",
                "No extracted data available."
            )

            return

        file_path = export_excel(
            self.extracted_data
        )

        messagebox.showinfo(
            "Success",
            f"Excel exported to:\n{file_path}"
        )


    def export_csv_file(self):

        if not self.extracted_data:

            messagebox.showwarning(
                "Warning",
                "No extracted data available."
            )

            return

        file_path = export_csv(
            self.extracted_data
        )

        messagebox.showinfo(
            "Success",
            f"CSV exported to:\n{file_path}"
        )


    def export_json_file(self):

        if not self.extracted_data:

            messagebox.showwarning(
                "Warning",
                "No extracted data available."
            )

            return

        file_path = export_json(
            self.extracted_data
        )

        messagebox.showinfo(
            "Success",
            f"JSON exported to:\n{file_path}"
        )
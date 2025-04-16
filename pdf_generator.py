# pdf_generator.py

from fpdf import FPDF

class ChecklistPDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Moving Home Checklist", new_x="LMARGIN", new_y="NEXT", align="C")
        self.ln(2)

    def section_title(self, title):
        self.set_font("Arial", "B", 12)
        self.set_text_color(0, 70, 140)
        self.cell(0, 8, title, new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(0, 0, 0)

    def checklist_item(self, item):
        self.set_font("Arial", "", 11)
        self.cell(10, 8, "[ ]", border=0)
        self.multi_cell(0, 8, item)
        self.ln(0.5)

def create_checklist_pdf(sections, filename="Moving_Home_Checklist.pdf"):
    pdf = ChecklistPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    for section, items in sections:
        pdf.section_title(section)
        for item in items:
            pdf.checklist_item(item)
        pdf.ln(2)

    pdf.output(filename)
    print(f"Checklist PDF created: {filename}")

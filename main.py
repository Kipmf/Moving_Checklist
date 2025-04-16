# main.py

from checklist_data import sections
from pdf_generator import create_checklist_pdf

def main():
    create_checklist_pdf(sections)

if __name__ == "__main__":
    main()

from fpdf import FPDF
import random
import pandas as pd

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Random Data Tables', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')

def main():
    # Create instance of FPDF class
    pdf = PDF()

    # Add a page
    pdf.add_page()

    # Set font
    pdf.set_font("Arial", size=12)

    # Generate random tables
    for _ in range(5):
        # Random number of rows (some large enough to span multiple pages)
        num_rows = random.randint(10, 100)
        num_columns = random.randint(3, 6)

        # Create DataFrame with random data
        data = [[random.randint(1, 100) for _ in range(num_columns)] for _ in range(num_rows)]
        df = pd.DataFrame(data, columns=[f'Col{i+1}' for i in range(num_columns)])

        # Add table to PDF
        pdf.set_fill_color(255, 0, 0)
        pdf.set_text_color(255)
        pdf.set_draw_color(128, 0, 0)
        pdf.set_line_width(0.3)
        pdf.set_font('', 'B')
        for col in df.columns:
            pdf.cell(40, 10, col, 1, 0, 'C', 1)
        pdf.ln()
        pdf.set_fill_color(224, 235, 255)
        pdf.set_text_color(0)
        pdf.set_font('')

        fill = False
        for row in df.values:
            for item in row:
                pdf.cell(40, 6, str(item), 'LR', 0, 'C', fill)
            pdf.ln()
            fill = not fill
        pdf.cell(0, 0, '', 'T')

        # Add a small gap after each table
        pdf.ln(10)

    # Save the pdf with name .pdf
    pdf_output = "output/Random_Tables.pdf"
    pdf.output(pdf_output)

    pdf_output

if __name__ == '__main__':
    main()
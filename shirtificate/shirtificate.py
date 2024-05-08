from fpdf import FPDF

class PDF(FPDF):

    def header(self):
        self.set_font("helvetica","B",50)
        self.cell(0,50,"CS50 Shirtificate",new_x="LMARGIN",new_y="NEXT",align = "C")

def prompt():
    return input("Enter a name: ")


def main():

    pdf = PDF()
    pdf.add_page()
    pdf.image("shirtificate.png",w=pdf.epw)
    pdf.set_font_size(28)
    pdf.set_text_color(255,255,255)
    pdf.text(x=47.5, y = 140,txt=f"{prompt()} took CS50")
    pdf.output("shirtificate.pdf")

main()
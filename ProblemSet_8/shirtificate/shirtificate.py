from fpdf import FPDF

class CertificateGenerator(FPDF):

    # Define a method to compose the certificate content.
    def compose_certificate(self):
        # Disable automatic page breaks to have full control over page layout.
        self.set_auto_page_break(False)
        # Add a new page to the PDF.
        self.add_page()
        # Add an image of the certificate background.
        self.image("shirtificate.png", x=10, y=65, w=190, h=190)
        # Set font and style for the certificate title.
        self.set_font("helvetica", "B", 50)
        # Add the title for the certificate.
        self.cell(190, 50, "CS50 Certificate", new_x="LMARGIN", new_y="TOP", align="C")

    # Define a method to set the recipient's name on the certificate.
    def set_recipient_name(self, name):
        """
        Set the recipient's name on the certificate.

        Args:
            name (str): The name of the recipient.

        """
        # Set font, style, and text color for the recipient's name.
        self.set_font("helvetica", "B", 25)
        self.set_text_color(255, 255, 255)
        # Add the recipient's name to the certificate.
        self.cell(190, 240, f"{name} took CS50", align="C")

    # Define a method to save the generated PDF with a given name.
    def save_certificate(self, file_name):
        """
        Save the generated certificate as a PDF file with a specified name.

        Args:
            file_name (str): The name of the PDF file to save.

        """
        # Output the PDF with the specified name.
        self.output(file_name)

# Main program entry point.
def main():
    # Create an instance of the CertificateGenerator class.
    pdf = CertificateGenerator()
    # Compose the certificate content.
    pdf.compose_certificate()
    # Prompt the user for the recipient's name.
    name = input("Name: ")
    # Set the recipient's name on the certificate.
    pdf.set_recipient_name(name)
    # Save the certificate as a PDF file with a specified name.
    pdf.save_certificate("shirtificate.pdf")

# Check if the script is being run as the main program.
if __name__ == "__main__":
    main()

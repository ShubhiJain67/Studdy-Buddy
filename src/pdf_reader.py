from PyPDF2 import PdfReader
from src.logger import Logger

class PDFReader:
    """
    A class to read and extract text from PDF files.
    """

    def __init__(self, logger: Logger):
        self.logger = logger

    def PDFReader(self, file_path: str):
        try:
            # Create a PDF reader object
            pdf_reader = PdfReader(file_path)
            text_content = ""
        
            # Extract text from each page
            for page in pdf_reader.pages:
                text_content += page.extract_text()
                
        except Exception as e:
            self.logger.log(f"Error reading PDF on path: {file_path} : {e}")
            text_content = ""

        return text_content
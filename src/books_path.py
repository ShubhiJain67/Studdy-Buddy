from src.logger import Logger
from src.pdf_reader import PDFReader

BASE_BOOK_PATH = "./data/"

class BooksReader:
    def __init__(self, logger: Logger, pdf_reader: PDFReader, base_path:str=BASE_BOOK_PATH):
        self.base_path = base_path
        self.logger = logger
        self.pdf_reader = pdf_reader

    def fetch_books_paths(self):
        import os
        books_paths = {}
        for root, dirs, files in os.walk(self.base_path):
            for dir in dirs:
                self.logger.log("Reading Subject: " + dir)
                subject_path = os.path.join(root, dir)
                books_paths[dir] = {}
                for file in os.listdir(subject_path):
                    if file.endswith(".pdf"):
                        books_paths[dir][file] = os.path.join(subject_path, file)
                        # self.logger.log("Found PDF: " + file)
        return books_paths
    
    def get_all_books(self):
        books_paths = self.fetch_books_paths()
        all_books_text = {}
        for subject, contents in books_paths.items():
            all_books_text[subject] = {}
            for name, path in contents.items():
                text_content = self.pdf_reader.PDFReader(path)
                all_books_text[subject][name] = text_content
                self.logger.log(f"Extracted text from {subject} {name}")
        return all_books_text
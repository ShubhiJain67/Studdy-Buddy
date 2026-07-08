from src.pdf_reader import PDFReader
from src.books_path import BooksReader
from src.logger import Logger

logger = Logger()
pdf_reader = PDFReader(logger)
books_reader = BooksReader(logger, pdf_reader)

books = books_reader.get_all_books()
print(books)
# for subject, contents in book_paths.items():
#     print(f"Subject: {subject}")
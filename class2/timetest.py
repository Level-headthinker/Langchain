import time
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.document_loaders import UnstructuredFileLoader
from langchain_community.document_loaders import OnlinePDFLoader
from langchain_community.document_loaders import MathPixLoader

class DocumentLoaders:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_pdf_using_pypdf(self):
        start_time = time.time()  # Start measuring time
        try:
            loader = PyPDFLoader(self.file_path)
            pages = loader.load()
            return time.time() - start_time  # Return elapsed time
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def load_pdf_using_pymupdf(self):
        start_time = time.time()  # Start measuring time
        try:
            loader = PyMuPDFLoader(self.file_path)
            data = loader.load()
            return time.time() - start_time  # Return elapsed time
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def load_pdf_using_unstructured_loader(self):
        start_time = time.time()  # Start measuring time
        try:
            loader = UnstructuredFileLoader(self.file_path)
            unstructured_data = loader.load()
            return time.time() - start_time  # Return elapsed time
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def load_pdf_using_onlinepdf_loader(self):
        start_time = time.time()  # Start measuring time
        try:
            loader = OnlinePDFLoader(self.file_path)
            onlinepdf_data = loader.load()
            return time.time() - start_time  # Return elapsed time
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def load_pdf_using_mathpix_loader(self):
        start_time = time.time()  # Start measuring time
        try:
            loader = MathPixLoader(self.file_path)
            mathpix_data = loader.load()
            return time.time() - start_time  # Return elapsed time
        except Exception as e:
            print(f"Error: {e}")
            return None

# Example usage:
file_path = r"D:\langchain\notebooks\documents\sensors-22-08281-v3.pdf"
dl = DocumentLoaders(file_path)
pypdf_time = dl.load_pdf_using_pypdf()
pymupdf_time = dl.load_pdf_using_pymupdf()
unstructured_time = dl.load_pdf_using_unstructured_loader()
onlinepdf_time = dl.load_pdf_using_onlinepdf_loader()
mathpix_time = dl.load_pdf_using_mathpix_loader()

print("Time taken by each loader:")
print("PyPDFLoader:", pypdf_time)
print("PyMuPDFLoader:", pymupdf_time)
print("UnstructuredFileLoader:", unstructured_time)
print("OnlinePDFLoader:", onlinepdf_time)
print("MathPixLoader:", mathpix_time)

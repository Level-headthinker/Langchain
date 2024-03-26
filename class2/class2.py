from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.document_loaders import UnstructuredFileLoader
from langchain_community.document_loaders import OnlinePDFLoader
from langchain_community.document_loaders import MathpixPDFLoader

class document_loaders:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_pdf_using_pypdf(self):
        try:
            loader = PyPDFLoader(self.file_path)
            pages = loader.load()
            return pages
        
        except Exception as e:
            print(f"Error: {e}")    
    
    def load_pdf_using_pymupdf(self):
        try:
            loader = PyMuPDFLoader(self.file_path)
            data = loader.load()
            return data
        
        except Exception as e:
            print(f"Error: {e}")
            
    def load_pdf_using_unstructure_loader(self):
        try:
            loader = UnstructuredFileLoader(self.file_path)
            unstructuredata = loader.load()
            return unstructuredata
        except Exception as e:
            print(f"Error: {e}") 
            
    def load_pdf_using_onlinepdf_loader(self, pdf_url):
        try:
            loader = OnlinePDFLoader(pdf_url)
            onlinepdf_data = loader.load()
            return onlinepdf_data
        except Exception as e:
            print(f"Error: {e}")
    
    def load_pdf_using_mathpix_loader(self):
        try:
            loader = MathpixPDFLoader(self.file_path)
            mathpix_data = loader.load()
            return mathpix_data
        except Exception as e:
            print(f"Error: {e}")                   

dl = document_loaders(r"D:\langchain\notebooks\documents\sensors-22-08281-v3.pdf")
pdf_url = "https://www.sjsu.edu/writingcenter/docs/handouts/Articles.pdf"  
onlinepdf_results = dl.load_pdf_using_onlinepdf_loader(pdf_url)
# print(onlinepdf_results)
# math_pdf_url="https://www.lehman.edu/faculty/dgaranin/Mathematical_Physics/Mathematical_physics-13-Partial_differential_equations.pdf"
# mathpix_results = dl.load_pdf_using_mathpix_loader(math_pdf_url)
# print(mathpix_results)
pypdf_results = dl.load_pdf_using_pypdf()
pymupdf_results = dl.load_pdf_using_pymupdf()
unstructed_results = dl.load_pdf_using_unstructure_loader()
# mathpix_results = dl.load_pdf_using_mathpix_loader()
# print(mathpix_results)
# onlinepdf_results = dl.load_pdf_using_onlinepdf_loader()

# print(onlinepdf_results)

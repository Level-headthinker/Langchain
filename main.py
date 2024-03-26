from langchain_community.document_loaders import UnstructuredHTMLLoader

class MyHTMLLoader(UnstructuredHTMLLoader):
  def load(self):
    with open(self.file_path, "r") as file:
      return file.read()
  def load_html(self):
        try:
            loader = UnstructuredHTMLLoader(self.file_path)
            htmldata = loader.load()
            return htmldata
           
        except Exception as e:
            print(f"Error:{e}")
  

loader = MyHTMLLoader(r"D:\langchain\notebooks\index.html")
data = loader.load()
print(data)
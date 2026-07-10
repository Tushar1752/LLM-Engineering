"""
docchat/file_loader.py - turn an uploaded file into plain text.

One job: given a filename and its raw bytes, return the text inside. The rest of
the app never has to know whether the upload was a PDF, a DOCX or a TXT - it just
calls load_text() and gets a string. (This is exactly the "hide messy details
behind one clean function" idea from lesson 03.)

Concepts reused from lessons 01 and 02:
    .txt  -> decode the bytes         (lesson 01)
    .pdf  -> pypdf                     (lesson 02)
    .docx -> python-docx              (lesson 02)
"""

from io import BytesIO
from docx import Document
from pypdf import PdfReader

def _read_pdf(data:bytes)->str:
    reader=PdfReader(BytesIO(data))
    return "\n".join((page.extract_text() or "") for page in reader.pages)

def _read_docx(data:bytes) -> str:
    doc = Document(BytesIO(data))
    return "\n".join(paragraph.text for paragraph in doc.paragraphs)

def _read_txt(data:bytes)-> str:
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        return data.decode("latin-1", errors="ignore")
    
def load_text(filename :str, data:bytes)-> str:
    name = filename.lower()
    if name.endswith(".txt"):
        text = _read_txt(data)
    elif name.endswith(".pdf"):
        text= _read_pdf(data)
    elif name.endswith(".docx"):
        text=_read_docx(data)
    else:
        raise ValueError (f"Unsupported file type:{filename}")
    
    if not text.strip():
        raise ValueError(
            f"No readable text found in {filename}."
            "If it's a scanned pdf, it has no selectable text to extract."

        )
    return text


if __name__ == "__main__":
    demo = load_text("demo.txt",b"Chroma stores vectors.RAG retrieves them.")
    print("load_text() returned:", repr(demo))
   


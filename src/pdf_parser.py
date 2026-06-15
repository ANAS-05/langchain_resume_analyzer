import fitz  # PyMuPDF
from pathlib import Path

def extract_text_from_pdf(file_path: str | Path) -> str:
    """
    Extracts raw text from a PDF document.
    
    Args:
        file_path (str | Path): The relative or absolute path to the PDF file.
        
    Returns:
        str: The concatenated text from all pages of the document.
        
    Raises:
        FileNotFoundError: If the provided path does not exist.
        RuntimeError: If PyMuPDF fails to read or process the file.
    """
    path_obj = Path(file_path)
    
    if not path_obj.exists():
        raise FileNotFoundError(f"The document at '{file_path}' could not be found.")
        
    extracted_pages = []
    
    try:
        # Open the PDF document using fitz
        with fitz.open(path_obj) as pdf_document:
            for page_num in range(len(pdf_document)):
                page = pdf_document[page_num]
                # Extract text from the current page
                page_text = page.get_text()
                extracted_pages.append(page_text)
                
    except Exception as e:
        raise RuntimeError(f"An error occurred while processing '{file_path}': {str(e)}")
        
    # Join all pages with a double newline to maintain clear page separation
    return "\n\n".join(extracted_pages)
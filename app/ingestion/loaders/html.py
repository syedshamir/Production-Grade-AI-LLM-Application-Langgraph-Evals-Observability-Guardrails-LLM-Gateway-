from bs4 import BeautifulSoup 
import logfire

def parse_html(file_path: str):
    """
    Parse HTML into readable plain text for retrieval.

    Non-content tags are removed before text extraction so navigation scripts,
    styling, and metadata do not pollute embeddings or downstream answers.
    """
    with logfire.span("📄 HTML Parsing", filename=file_path):
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            soup = BeautifulSoup(content, "html.parser")
            
            # Remove content that is useful to browsers but noisy for RAG.
            for script in soup(["script", "style", "meta", "noscript"]):
                script.decompose()
                
            # Preserve visible block boundaries by separating extracted text with newlines.
            text = soup.get_text(separator="\n")
            
            # Collapse repeated whitespace while keeping one logical line per phrase.
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text_clean = '\n'.join(chunk for chunk in chunks if chunk)
            
            return text_clean
        except Exception as e:
            logfire.error(f"❌ HTML Parse Failed: {e}")
            raise e

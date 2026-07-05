from typing import List
import logfire

def chunk_text(text: str, chunk_size: int = 1500) -> List[str]:
    """
    Split raw document text into retrieval-friendly chunks.

    Paragraph boundaries are preserved where possible because they usually carry
    more semantic meaning than fixed-width slicing. This keeps related ideas
    together for embeddings while still enforcing an approximate upper size.
    """
    with logfire.span("✂️ Text Chunking", text_length=len(text)):
        if not text.strip(): 
            return []
            
        paragraphs = text.split("\n\n")
        chunks = []
        current_chunk = ""
        
        for p in paragraphs:
            # Keep appending paragraphs until the next one would exceed the
            # target size, then flush the accumulated context as one chunk.
            if len(current_chunk) + len(p) < chunk_size:
                current_chunk += p + "\n\n"
            else:
                if current_chunk.strip():
                    chunks.append(current_chunk.strip())
                current_chunk = p + "\n\n"
        
        if current_chunk.strip():
            chunks.append(current_chunk.strip())
            
        # Guard against whitespace-only chunks caused by noisy source files.
        valid_chunks = [c for c in chunks if c.strip()]
        logfire.info(f"✅ Generated {len(valid_chunks)} chunks")
        return valid_chunks

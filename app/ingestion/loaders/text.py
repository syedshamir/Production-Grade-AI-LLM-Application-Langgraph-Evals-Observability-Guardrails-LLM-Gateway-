import logfire

def parse_text(file_path: str):
    """
    Read plain text files into the same string interface used by richer loaders.

    Encoding errors are ignored so a single bad byte in noisy source data does
    not prevent the rest of the file from being indexed.
    """
    with logfire.span("📄 Text Parsing", filename=file_path):
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                return f.read()
        except Exception as e:
            logfire.error(f"❌ Text Parse Failed: {e}")
            raise e

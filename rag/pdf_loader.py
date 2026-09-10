from pypdf import PdfReader


def load_pdf_pages(filename):
    reader = PdfReader(filename)

    pages = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""

        pages.append({
            "text": text,
            "source": filename,
            "page": page_number
        })

    return pages


def chunk_pages(pages, chunk_size=1000, overlap=200):
    chunks = []

    step = chunk_size - overlap

    for page in pages:
        text = page["text"]

        if not text.strip():
            continue

        for i in range(0, len(text), step):
            chunk_text = text[i:i + chunk_size]

            chunks.append({
                "text": chunk_text,
                "source": page["source"],
                "page": page["page"]
            })

    return chunks


def load_and_chunk_pdf(filename):
    pages = load_pdf_pages(filename)

    return chunk_pages(pages)



















# from pypdf import PdfReader


# def load_and_chunk_pdf(filename):
#     reader = PdfReader(filename)

#     all_text = ""

#     for page in reader.pages:
#         all_text += page.extract_text() or ""
#         all_text += "\n"

#     chunk_size = 1000
#     overlap = 200
#     step = chunk_size - overlap

#     chunks = []

#     for i in range(0, len(all_text) - overlap, step):
#         chunk = all_text[i:i + chunk_size]
#         chunks.append(chunk)

#     return chunks
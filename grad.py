import fitz
import cv2
import numpy as np
import pytesseract
import gradio as gr

def extract_text_from_pdf(pdf_file):
    doc = fitz.open(pdf_file.name)  # open document from the uploaded file
    num_of_pages = doc.page_count

    for page in doc:
        pix = page.get_pixmap(matrix=fitz.Matrix(300 / 72, 300 / 72), alpha=False)  # render page to an image
        pix.save(f"page_{page.number:03d}.jpg")  # store image as a JPEG

    extracted_text = ""
    for i in range(num_of_pages):
        img = cv2.imread(f'page_{i:03d}.jpg')
        
        # RGB for mac is 250,205,90 for highlight
        lower_yellow = np.array([0, 200, 230]) # yellow
        upper_yellow = np.array([90,205,250]) # yellow
        mask = cv2.inRange(img, lower_yellow, upper_yellow)
        result = cv2.bitwise_and(img, img, mask=mask)
        text = pytesseract.image_to_string(result)
        extracted_text += text

    return extracted_text

def main():
    
    iface = gr.Interface(fn=extract_text_from_pdf, inputs="file", outputs="text", title="PDF Highlight to Text Converter", description="This demo is only capable of recognizing yellow highlights from Mac Preview.")
         
    iface.launch(share=True)

if __name__ == '__main__':
    main()

# PDF Highlight to Text Converter
This is a Python program that extracts text from a PDF file, specifically yellow highlighted text from Mac Preview. The program converts the PDF pages into JPEG images and applies a color filter to extract the highlighted text. The extracted text is then processed using the Tesseract OCR engine to convert it into a machine-readable format.

## Packages Used:
fitz
cv2
numpy
pytesseract
gradio
## How to Use:
Run the program and launch the Gradio interface.
Upload the PDF file containing yellow highlighted text from Mac Preview.
The program will convert the PDF pages to JPEG images, extract the highlighted text, and return it as machine-readable text.

## Example:
<img width="1526" alt="PDF_Highlight_to_Text_Converter" src="https://user-images.githubusercontent.com/33205097/222986865-590c8d36-90c1-4846-a462-b03de5b35c01.png">

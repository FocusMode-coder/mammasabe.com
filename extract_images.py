#!/usr/bin/env python3
"""
Extract all images from PDF brochure using PyMuPDF (fitz)
Output: Numbered images saved to /assets folder
"""

import fitz  # PyMuPDF
import os
from pathlib import Path

def extract_images_from_pdf(pdf_path, output_folder):
    """
    Extract all embedded images from a PDF file.
    
    Args:
        pdf_path: Path to the PDF file
        output_folder: Folder to save extracted images
    """
    # Create output folder if it doesn't exist
    Path(output_folder).mkdir(parents=True, exist_ok=True)
    
    # Open the PDF
    pdf_document = fitz.open(pdf_path)
    
    total_images = 0
    
    print(f"📄 Processing: {pdf_path}")
    print(f"📁 Output folder: {output_folder}")
    print("-" * 50)
    
    # Iterate through each page
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        image_list = page.get_images(full=True)
        
        print(f"Page {page_num + 1}: Found {len(image_list)} image(s)")
        
        # Extract each image from the page
        for img_index, img in enumerate(image_list):
            xref = img[0]  # Image reference number
            
            try:
                # Extract image data
                base_image = pdf_document.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]  # jpg, png, etc.
                
                # Create filename with page number and image index
                # Format: p01_img001.jpg, p02_img003.png, etc.
                image_filename = f"p{page_num + 1:02d}_img{img_index + 1:03d}.{image_ext}"
                image_path = os.path.join(output_folder, image_filename)
                
                # Save the image
                with open(image_path, "wb") as image_file:
                    image_file.write(image_bytes)
                
                print(f"  ✓ Saved: {image_filename} ({len(image_bytes)} bytes)")
                total_images += 1
                
            except Exception as e:
                print(f"  ✗ Error extracting image {img_index + 1}: {e}")
    
    pdf_document.close()
    
    # Print summary
    print("-" * 50)
    print(f"✨ Extraction complete!")
    print(f"📊 Total images extracted: {total_images}")
    print(f"📁 Images saved to: {os.path.abspath(output_folder)}")
    
    return total_images


if __name__ == "__main__":
    # Configuration
    PDF_FILE = "BrochureFINAL_MammaSabe.pdf"
    OUTPUT_FOLDER = "assets"
    
    # Check if PDF exists
    if not os.path.exists(PDF_FILE):
        # Try to find any PDF file in the directory
        pdf_files = [f for f in os.listdir('.') if f.lower().endswith('.pdf')]
        
        if pdf_files:
            PDF_FILE = pdf_files[0]
            print(f"⚠️  'BrochureFINAL_MammaSabe.pdf' not found")
            print(f"✓ Using: {PDF_FILE}")
            print()
        else:
            print(f"❌ Error: No PDF files found in current directory")
            print(f"📁 Current directory: {os.getcwd()}")
            print()
            print("Please place your PDF file (e.g., BrochureFINAL_MammaSabe.pdf) in:")
            print(f"  {os.getcwd()}")
            print()
            print("Then run the script again.")
            exit(1)
    
    # Extract images
    try:
        extract_images_from_pdf(PDF_FILE, OUTPUT_FOLDER)
    except Exception as e:
        print(f"❌ Error: {e}")
        exit(1)

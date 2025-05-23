import cv2
from qreader import QReader
import os
import webbrowser

def detect_and_open_qr(image_path):
    # Step 1: Validate file path
    if not os.path.isfile(image_path):
        print(f"File not found: {image_path}")
        return

    # Step 2: Read image
    image = cv2.imread(image_path)
    if image is None:
        print("Could not read the image. Make sure it's a valid image file.")
        return

    # Step 3: Initialize QReader
    qr = QReader()
    data_list = qr.detect_and_decode(image)

    # Step 4: Process results
    if data_list:
        print("QR code(s) detected!")
        valid_data = [d for d in data_list if d]  # Remove None values

        if not valid_data:
            print("QR codes were found but no data could be decoded.")
            return

        for data in valid_data:
            print("Data:", data)
            if data.startswith("http"):
                print("🌐 Opening URL in web browser...")
                webbrowser.open(data)
    else:
        print("No QR code found in the image.")

path = input("Enter the full image path: ").strip()
detect_and_open_qr(path)


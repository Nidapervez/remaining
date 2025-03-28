from pyzbar.pyzbar import decode
from PIL import Image
import os

# Path of the QR code image
img_path = r"C:\Users\Burhan\Desktop\New folder\QR-code-encoder-decoder\qrcode.png"

# Check if file exists
if not os.path.exists(img_path):
    print("❌ QR Code image not found! Please generate it first.")
else:
    # Open the image
    img = Image.open(img_path)

    # Decode the QR code
    result = decode(img)

    # Print the decoded text
    if result:
        for barcode in result:
            print("✅ Decoded Text:", barcode.data.decode('utf-8'))
    else:
        print("❌ No QR code found in the image.")

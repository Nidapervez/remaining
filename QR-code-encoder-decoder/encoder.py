import qrcode
import os

# Data to encode
data = "Don't forget to subscribe!"

# Path to save the QR code image
save_dir = r"C:\Users\Burhan\Desktop\New folder\QR-code-encoder-decoder"
img_path = os.path.join(save_dir, "qrcode.png")

# Ensure directory exists
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Create QR code instance
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5,
)

qr.add_data(data)
qr.make(fit=True)

# Generate the QR code image
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image
img.save(img_path)

print(f"✅ QR Code saved at: {img_path}")

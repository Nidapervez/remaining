import streamlit as st
import qrcode
import io
from PIL import Image

# Function to generate QR code
def generate_qr_code(data, color):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create the QR code image
    qr_image = qr.make_image(fill=color, back_color="white")

    # Convert PIL image to bytes
    img_bytes = io.BytesIO()
    qr_image.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    return img_bytes

# Streamlit UI
def main():
    st.set_page_config(page_title="QR Code Generator", page_icon="🔗", layout="centered")

    st.title("🔗 QR Code Generator")
    st.markdown("### Generate a custom QR Code easily!")

    # Input for QR Code Data
    qr_data = st.text_input("Enter text or URL", "")

    # Color Picker for QR Code
    qr_color = st.color_picker("Pick QR Code Color", "#000000")

    # Button to generate QR Code
    if st.button("Generate QR Code"):
        if qr_data:
            img_bytes = generate_qr_code(qr_data, qr_color)

            # Display QR Code
            st.image(img_bytes, caption="Your QR Code", use_container_width=True)

            # Download button
            st.download_button(
                label="Download QR Code",
                data=img_bytes,
                file_name="qrcode.png",
                mime="image/png"
            )
        else:
            st.warning("⚠️ Please enter text or a URL to generate the QR Code.")

# Run the app
if __name__ == "__main__":
    main()

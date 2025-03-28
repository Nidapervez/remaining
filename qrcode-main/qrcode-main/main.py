import streamlit as st
import qrcode
import io
from PIL import Image
import cv2
import numpy as np
from pyzbar.pyzbar import decode

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

# Function to decode QR code
def decode_qr_code(image):
    image = Image.open(image).convert("RGB")
    image_np = np.array(image)
    qr_codes = decode(image_np)
    
    if qr_codes:
        return qr_codes[0].data.decode("utf-8")
    else:
        return None

# Streamlit UI
def main():
    st.set_page_config(page_title="QR Code Generator & Decoder", page_icon="🔗", layout="centered")

    st.title("🔗 QR Code Generator & Decoder")
    st.markdown("### Generate and Decode QR Codes Easily!")

    # Tabs for Generator and Decoder
    tab1, tab2 = st.tabs(["Generate QR Code", "Decode QR Code"])

    with tab1:
        st.subheader("Generate QR Code")
        qr_data = st.text_input("Enter text or URL", "")
        qr_color = st.color_picker("Pick QR Code Color", "#000000")

        if st.button("Generate QR Code"):
            if qr_data:
                img_bytes = generate_qr_code(qr_data, qr_color)
                st.image(img_bytes, caption="Your QR Code", use_container_width=True)

                st.download_button(
                    label="Download QR Code",
                    data=img_bytes,
                    file_name="qrcode.png",
                    mime="image/png"
                )
            else:
                st.warning("⚠️ Please enter text or a URL to generate the QR Code.")

    with tab2:
        st.subheader("Decode QR Code")
        uploaded_file = st.file_uploader("Upload a QR Code image", type=["png", "jpg", "jpeg"])
        
        if uploaded_file:
            st.image(uploaded_file, caption="Uploaded QR Code", use_container_width=True)
            decoded_text = decode_qr_code(uploaded_file)
            
            if decoded_text:
                st.success(f"✅ Decoded Text: {decoded_text}")
            else:
                st.error("❌ No QR code detected. Please upload a valid QR code image.")

if __name__ == "__main__":
    main()
import streamlit as st
import os
import zipfile
from io import BytesIO

def rename_images(files, prefix):
    renamed_files = []
    for i, file in enumerate(files):
        file_extension = os.path.splitext(file.name)[1]  # Get file extension
        new_name = f"{prefix}_{i+1}{file_extension}"  # Rename format
        renamed_files.append((new_name, file))
    return renamed_files

def create_zip(renamed_files):
    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for new_name, file in renamed_files:
            zip_file.writestr(new_name, file.getvalue())
    zip_buffer.seek(0)
    return zip_buffer

# Streamlit UI
st.title("📂 Bulk Image Renamer with Drag & Drop")

uploaded_files = st.file_uploader("Drag and drop images here", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

prefix = st.text_input("Enter prefix for renamed images", "image")

if uploaded_files and st.button("Rename Images"):
    renamed_files = rename_images(uploaded_files, prefix)
    zip_buffer = create_zip(renamed_files)
    st.success(f"Renamed {len(renamed_files)} images successfully!")
    
    # Provide download link for renamed images
    st.download_button(
        label="Download Renamed Images",
        data=zip_buffer,
        file_name="renamed_images.zip",
        mime="application/zip"
    )
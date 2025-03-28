import streamlit as st
import markovify

# Streamlit UI
st.title("📜 Text Generator with Markov Chains")
st.write("Upload a text file, and this app will generate new text using a Markov chain model.")

# File upload
uploaded_file = st.file_uploader("Upload a text file", type=["txt"])

if uploaded_file is not None:
    # Read the text file
    text = uploaded_file.read().decode("utf-8")

    # Train Markov model
    text_model = markovify.Text(text)

    # Button to generate text
    if st.button("Generate Text"):
        generated_text = text_model.make_sentence(tries=100)
        if generated_text:
            st.subheader("📝 Generated Text:")
            st.write(generated_text)
        else:
            st.warning("Couldn't generate a sentence. Try uploading a different text file.")


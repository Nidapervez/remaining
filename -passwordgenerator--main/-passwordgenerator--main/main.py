import streamlit as st
import base64
import random
import numpy as np
import matplotlib.pyplot as plt

# Function to set background image
def set_bg(image_file):
    with open(image_file, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
             color: black
        }}
        .title {{
            font-size: 70px; /* Increased font size */
            font-weight: bold;
            color: white; /* White text for contrast */
            text-shadow: 2px 2px 4px black; /* Black shadow for visibility */
            text-align: center;
            margin-bottom: 20px;
            padding: 10px;
            background-color: rgba(0, 0, 0, 0.6); /* Semi-transparent background */
            border-radius: 10px;
            display: inline-block;
        }}
        .button {{
            background-color: #ff6600;
            color: white;
            border-radius: 10px;
            padding: 12px;
            font-size: 20px; /* Increased font size */
            width: 100%;
            text-align: center;
            font-weight: bold;
            box-shadow: 2px 2px 5px black;
        }}
        </style>
    
        
        """,
        unsafe_allow_html=True
    )

# Set background image
set_bg("background.jpg")  # Ensure this image exists

# Streamlit Navigation
st.sidebar.title("🔐 Password & Pattern Generator")
page = st.sidebar.radio("Go to", ["Password Generator", "Pattern Generator"])

# ---------------------------- PASSWORD GENERATOR ----------------------------
if page == "Password Generator":
    st.markdown('<p class="title">🔑 Secure Password Generator</p>', unsafe_allow_html=True)
    st.write("Generate strong passwords with a mix of letters, numbers, and symbols.")

    # Password length input
    st.markdown('<p style="color: white; font-size: 18px;">Select Password Length</p>', unsafe_allow_html=True)
    plen = st.slider("", min_value=4, max_value=20, value=12)


    # Generate password
    import string
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    all_chars = list(s1 + s2 + s3 + s4)
    random.shuffle(all_chars)
    password = "".join(random.sample(all_chars, plen))

    if st.button("Generate Password 🔄"):
       st.markdown(
    f'<p style="color: white; background-color: green; padding: 10px; border-radius: 5px;">🔒 Your Secure Password: <b>{password}</b></p>',
    unsafe_allow_html=True
)


# ---------------------------- PATTERN GENERATOR (Mobile-Like) ----------------------------
elif page == "Pattern Generator":
    st.markdown('<p class="title">📱 Mobile Pattern Lock Generator</p>', unsafe_allow_html=True)
    st.write("Randomly generated 3x3 mobile unlock pattern.")

    def generate_pattern():
        """Generate a random pattern in a 3x3 grid."""
        grid_points = [(i, j) for i in range(3) for j in range(3)]
        random.shuffle(grid_points)
        selected_points = grid_points[:random.randint(4, 9)]  # Select between 4-9 points
        return selected_points

    def draw_pattern(pattern_points):
        """Draw the pattern using Matplotlib."""
        fig, ax = plt.subplots(figsize=(3, 3))
        ax.set_xlim(-0.5, 2.5)
        ax.set_ylim(-0.5, 2.5)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_frame_on(False)

        # Draw grid dots
        for i in range(3):
            for j in range(3):
                ax.scatter(i, j, s=500, color='gray')  # Dots

        # Draw pattern lines
        if len(pattern_points) > 1:
            x_vals, y_vals = zip(*pattern_points)
            ax.plot(x_vals, y_vals, 'o-', color='red', markersize=15, linewidth=3)  # Line connecting points

        ax.invert_yaxis()  # Flip y-axis to match mobile pattern lock layout
        st.pyplot(fig)

    if st.button("Generate Pattern 🔄"):
        pattern = generate_pattern()
        draw_pattern(pattern)


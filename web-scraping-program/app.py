import streamlit as st
import requests

# App Title
st.title("GitHub Profile Image Scraper")

# Input field for GitHub username
username = st.text_input("Enter GitHub Username:")

if st.button("Get Profile Image"):
    if username:
        # GitHub API URL for user details
        github_api_url = f"https://api.github.com/users/{username}"
        response = requests.get(github_api_url)

        if response.status_code == 200:
            data = response.json()
            profile_image_url = data.get("avatar_url")

            # Display the image using the updated parameter
            if profile_image_url:
                st.image(profile_image_url, caption=f"{username}'s Profile Picture", use_container_width=True)
            else:
                st.error("Profile image not found!")
        else:
            st.error("User not found! Please check the username.")
    else:
        st.warning("Please enter a GitHub username.")

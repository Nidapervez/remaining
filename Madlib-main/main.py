import streamlit as st
import random

# 🎉 Streamlit App Title
st.title("🔥 The Ultimate Mad Libs Adventure! 🔥")

st.write("😆 Fill in the blanks and create your own hilarious, action-packed story!\n")

# 📌 User Inputs in Sidebar
st.sidebar.header("Enter Your Words ✍️")
name = st.sidebar.text_input("😜 Enter your name:")
superpower = st.sidebar.text_input("⚡ Enter a superpower:")
animal = st.sidebar.text_input("🐾 Enter a random animal:")
place = st.sidebar.text_input("📍 Enter a weird place:")
food = st.sidebar.text_input("🍕 Enter a delicious food:")
object = st.sidebar.text_input("🎾 Enter a random object:")
emotion = st.sidebar.text_input("😊 Enter an emotion:")
sound = st.sidebar.text_input("🔊 Enter a funny sound (like 'Boing' or 'Kaboom'): ")

# 🎲 Random Actions
actions = [
    "started breakdancing like a robot 🤖💃",
    "flew around like a superhero 🦸‍♂️✨",
    "suddenly turned into a giant marshmallow 🍡😂",
    "sang an opera song about pineapples 🎤🍍",
    "did 500 jumping jacks in 10 seconds 💪🔥"
]
random_action = random.choice(actions)

# 🚀 Generate Story on Button Click
if st.sidebar.button("Generate Story 🚀"):
    if not (name and superpower and animal and place and food and object and emotion and sound):
        st.warning("⚠️ Please fill in all the blanks to generate your story!")
    else:
        story = f"""
        🌟✨ **THE LEGEND OF {name.upper()}** ✨🌟

        📌 One ordinary morning, **{name}** 😴 woke up and discovered they had an extraordinary power: **{superpower}!** ⚡💥  
        Overjoyed, **{name}** dashed straight to **{place}** 🏃‍♂️💨.

        🐾 But upon arrival, a giant **{animal}** 🦖 appeared out of nowhere, blocking the way! 😱  
        Thinking fast, **{name}** used their **{superpower}** 💪 and suddenly **{random_action.upper()}** 🌀💨.

        🎉 The **{animal}** was so **{emotion}** 🤩 that it let out a huge **'{sound}!'** 🔊 and disappeared in a puff of glitter! ✨💨  

        🍛 Victorious, **{name}** plopped down, picked up a **{object}** 🎾, and treated themselves to a feast of **{food}** 🤤.  
        🏆🔥 And from that day on, **{name}** became the legendary hero of **{place}!** 🎭🌍

        💥 **The End... or is it just the beginning? 🤔✨**
        """

        # 📝 Display the Story
        st.markdown(story)
        st.success("🎉 Your story is ready! Share it with your friends! 🚀")


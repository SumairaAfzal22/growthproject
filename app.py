import streamlit as st

st.set_page_config(page_title= "growth mindset projects", page_icon="🌹")

st.title("Growth Mindset Challenge")

st.header('😍 Welcome To Your Growth Journey!')
st.write('Embrace challenges,see failures as learning opportunities,learn from your mistake and unlock your potential. This AI-powered app helps you build a growth mindset with reflection,challenges and achievements! 🌟 ')

st.header("🌻 Today's Growth Mindset Quote")
st.write('“One can choose to go back toward safety or forward toward growth. Growth must be chosen again and again; fear must be overcome again and again.” -Abraham Maslow')

st.header("What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")

if user_input:
    st.success(f"You're facing: {user_input}. Keep pushing forward towords your goal!😄")
else: 
    st.warning('Tell us about your challenge to get started!')


st.header("Reflect on Your Learning")
reflection = st.text_area("Write your Reflections here:")

if reflection:
    st.success(f"Great Insight! Your reflection: {reflection}")

else:
    st.info("Reflecting on past experience help you grow! Share your difficulties")

st.header("✌Celebrate Your Wins!")
achievement = st.text_input("Share something you've recently accomplished:")

if achievement:
    st.success(f"🌟Amazing! You achieved: {achievement}")

else: 
    st.info("Big or small , every achievement counts! Share one now 😍")

st.write("- - - - - ")
st.write("⭐ Keep believing in yourself. Growth is a journey, not a destination!")
st.write(" ** Created by Sumaira Afzal **")


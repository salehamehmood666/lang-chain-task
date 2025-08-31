import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# API Keys (auto pick from .env)
openai_llm = ChatOpenAI(model="gpt-4o-mini")
gemini_llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# ---------------- UI ---------------- #
st.set_page_config(page_title="Meeting & Office Assistant", layout="wide")
st.title("📋 Meeting & Office Task Assistant")

# User Input
date = st.text_input("📅 Meeting Date", "25 Aug 2025")
time = st.text_input("⏰ Meeting Time", "10:00 AM")
agenda = st.text_area("📝 Agenda", "Budget planning and resource allocation")

if st.button("Generate Documents 🚀"):
    with st.spinner("Generating professional documents..."):

        # Step 1: Meeting Notice (OpenAI)
        notice = openai_llm.invoke(
            f"Draft a professional meeting notice.\nDate: {date}\nTime: {time}\nAgenda: {agenda}"
        ).content

        # Step 2: Summary Email (Gemini)
        email = gemini_llm.invoke(
            f"Write a short, polite, formal summary email for staff based on this agenda: {agenda}."
        ).content

        # Step 3: MOM Template (OpenAI)
        mom = openai_llm.invoke(
            f"Generate a clean template for Minutes of Meeting (MOM) for this agenda: {agenda}."
        ).content

        # Step 4: Task List (Gemini)
        tasks = gemini_llm.invoke(
            f"Create a follow-up task list with responsibilities for this meeting agenda: {agenda}."
        ).content

        # Output UI
        st.subheader("📑 Meeting Notice")
        st.write(notice)

        st.subheader("📧 Staff Email")
        st.write(email)

        st.subheader("🗒️ MOM Template")
        st.write(mom)

        st.subheader("✅ Task List")
        st.write(tasks)

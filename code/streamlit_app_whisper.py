# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 19:10:05 2023

@author: Subodh Deolekar
"""

import streamlit as st
#import openai
import os
import tempfile
import whisper

model = whisper.load_model('base')

# Set your OpenAI API key
# api_key = "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"

# # Initialize the OpenAI API client
# openai.api_key = api_key

# Create a Streamlit app
st.title("Audio Transcription with Whisper API")

# Upload a .wav or .mp3 file
uploaded_file = st.file_uploader("Upload a .wav or .mp3 file", type=["wav", "mp3"])

if uploaded_file:
    # Store the uploaded file in a temporary location
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
        temp_file.write(uploaded_file.read())

    st.success("File uploaded successfully!")

    # Transcribe the audio using Whisper
    st.write("Transcribing...")

    

    # Use the Whisper API to transcribe the audio
    try:
        transcript = model.transcribe(temp_file.name)
        print(transcript["text"])
        
        # Display the transcript in a textbox
        st.subheader("Transcript:")
        st.text(transcript["text"])
    except Exception as e:
        st.error(f"Error during transcription: {str(e)}")

    # Remove the temporary file
    os.remove(temp_file.name)
else:
    st.warning("Please upload a .wav or .mp3 file.")



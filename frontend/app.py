import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:5000"  # Replace with your backend URL if deployed

st.title("Transcript Sentiment Analysis")

uploaded_file = st.file_uploader("Upload a transcript", type=["txt"])
method = st.selectbox("Choose Sentiment Analysis Method", ["TextBlob", "Transformers"])

if uploaded_file is not None:
    st.write("Uploaded Transcript Content:")
    content = uploaded_file.read().decode('utf-8')
    # st.text(content)

    # Save file temporarily with utf-8 encoding
    with open("temp_transcript.txt", "w", encoding="utf-8") as temp_file:
        temp_file.write(content)

    # Upload file to backend
    with st.spinner("Uploading file..."):
        with open("temp_transcript.txt", "rb") as file:
            response = requests.post(
                f"{BACKEND_URL}/upload",
                files={"file": file}
            )
        if response.status_code == 200:
            filepath = response.json().get("filepath")
            st.success("File uploaded successfully!")
            st.write(f"Filepath: {filepath}")

            # Analyze sentiment
            with st.spinner("Analyzing sentiment..."):
                analysis_response = requests.post(
                    f"{BACKEND_URL}/analyze",
                    json={"filepath": filepath, "method": method.lower()}
                )
                if analysis_response.status_code == 200:
                    analysis = analysis_response.json()
                    st.write(f"Sentiment Analysis Results ({method}):")
                    st.json(analysis)
                else:
                    st.error(f"Error analyzing sentiment: {analysis_response.json().get('error')}")
        else:
            st.error(f"Error uploading file: {response.json().get('error')}")





# Transcript Sentiment Analysis Application

A web application that performs sentiment analysis on text transcripts using both TextBlob and Hugging Face Transformers. The application features a Flask backend API and a Streamlit frontend interface with interactive visualizations.

## Features

- File upload support for text transcripts
- Dual sentiment analysis methods:
  - TextBlob: Quick analysis with polarity and subjectivity scores
  - Transformers (DistilBERT): Advanced deep learning-based analysis with chunked processing
- Interactive visualizations of sentiment analysis results
- User-friendly Streamlit interface
- RESTful API backend

## Prerequisites

- Python 3.8+
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd transcript-sentiment-analysis
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Project Structure

```
transcript-sentiment-analysis/
├── backend/
│   ├── app.py
├── frontend/
│   └── streamlit_app.py
├── requirements.txt
└── README.md
```

## Configuration

1. Backend configuration:
   - The Flask backend runs on `http://127.0.0.1:5000` by default
   - Upload folder is created automatically at `./uploaded_files`
   - Model used: `distilbert-base-uncased-finetuned-sst-2-english`

2. Frontend configuration:
   - The Streamlit frontend connects to the backend URL defined in `BACKEND_URL`
   - Supports .txt file uploads
   - Includes interactive visualizations for sentiment analysis results

## API Endpoints

### POST /upload
- Uploads a text file
- Returns: filepath of uploaded file
- Example response:
```json
{
    "message": "File uploaded successfully",
    "filepath": "./uploaded_files/example.txt"
}
```

### POST /analyze
- Analyzes sentiment of uploaded file
- Parameters:
  - filepath: Path to the uploaded file
  - method: "textblob" or "transformers"
- Example response (TextBlob):
```json
{
    "method": "textblob",
    "polarity": 0.2,
    "subjectivity": 0.5,
    "sentiment": "Positive"
}
```

## Usage

1. Start the Flask backend:
```bash
cd backend
python app.py
```

2. In a new terminal, start the Streamlit frontend:
```bash
cd frontend
streamlit run streamlit_app.py
```

3. Open your browser and navigate to the Streamlit URL (typically `http://localhost:8501`)

4. Upload a text file and select your preferred analysis method

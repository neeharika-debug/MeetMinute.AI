# MeetMinute.AI — Smart Meeting Minutes Generator

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-Backend-black)
![Whisper](https://img.shields.io/badge/Faster--Whisper-STT-green)
![Pyannote](https://img.shields.io/badge/Pyannote-Speaker%20Diarization-orange)
![LLaMA3](https://img.shields.io/badge/LLaMA%203-Groq-blueviolet)
![Gemini](https://img.shields.io/badge/Gemini-AI-4285F4)

---

## Table of Contents

- [Overview](#-overview)
- [Goals](#-goals)
- [Tech Stack](#-tech-stack)
- [Key Features](#-key-features)
- [Project Workflow](#-project-workflow)
- [Project Structure](#-project-structure)
- [System Architecture](#-system-architecture)
- [What I Learned](#-what-i-learned)
- [Future Improvements](#-future-improvements)

---

## Overview

MeetMinute.AI is an AI-powered web application that transforms meeting recordings into structured meeting minutes. The application automatically transcribes audio, 
identifies different speakers, extracts important discussion points, decisions, and action items, and generates a downloadable PDF summary.

Instead of manually reviewing lengthy recordings or writing meeting notes, users can upload a meeting recording and receive organized, professional meeting minutes 
within minutes.

This project was developed as a university capstone and personal learning project to explore speech recognition, natural language processing, large language 
models, and full-stack AI application development.

---

## Goals

This project was built to learn how to:

- Build an end-to-end AI application
- Process meeting audio using Speech-to-Text
- Perform speaker diarization
- Apply NLP techniques for transcript cleaning
- Use LLMs to classify and extract structured information
- Generate professional PDF reports
- Design a responsive multi-page web interface
- Build authentication and meeting history features

---

## Tech Stack

### Backend

- Python
- Flask

### AI & Machine Learning

- Faster-Whisper
- pyannote.audio
- spaCy
- Groq API (LLaMA-3)
- Google Gemini API

### Frontend

- HTML
- CSS
- JavaScript

### Other Libraries

- ReportLab
- Pandas
- Regular Expressions
- Supabase

---

## Key Features

- User authentication
- Upload recorded meeting audio
- Automatic speech transcription
- Speaker diarization
- Transcript preprocessing
- AI-powered extraction of:
  - Discussion points
  - Decisions
  - Action items
- Priority-based refinement using Gemini
- Downloadable PDF meeting minutes
- Meeting history
- Light & Dark mode

---

## Project Workflow

Meeting Audio
↓
Faster-Whisper
↓
Speaker Diarization (Pyannote)
↓
Transcript Cleaning
↓
Sentence Segmentation (spaCy)
↓
Sentence Classification (LLaMA-3)
↓
Decision & Action Item Extraction
↓
Gemini Refinement
↓
Structured Meeting Minutes
↓
PDF Generation

---

## Project Structure

```text
MeetMinute.AI/
├──CODES_F
  ├── static/
    ├──script.js
    ├──style.css
  ├── templates/
    ├──index.html
  ├── webapp.py
  ├── db.py
  ├── MASTER_FILE.ipynb
  └── README.md
```

---

## System Architecture

The application follows a modular pipeline where each stage performs a dedicated task before passing the output to the next component.

- Authentication & User Management
- Audio Upload
- Speech-to-Text
- Speaker Diarization
- Transcript Processing
- LLM-based Classification
- Information Extraction
- PDF Generation
- Meeting History Storage

---

## What I Learned

Building MeetMinute.AI gave me practical experience with:

- Speech recognition using Faster-Whisper
- Speaker diarization with pyannote.audio
- Transcript preprocessing with NLP
- Prompt engineering using multiple LLMs
- Integrating Groq and Gemini APIs
- PDF generation with ReportLab
- Designing modular AI processing pipelines
- Building an end-to-end full-stack AI application

---

## Future Improvements

- Real-time meeting transcription
- Live meeting assistant
- Calendar integration
- Email generated meeting minutes
- Named speaker identification
- Collaborative editing
- Cloud deployment
- Multi-language support
- Meeting analytics dashboard

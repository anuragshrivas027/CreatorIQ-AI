# CreatorIQ AI - Full Stack RAG Video Intelligence Platform

## Project Overview

CreatorIQ AI is a Full Stack AI-powered video intelligence platform designed to analyze and compare YouTube videos and Instagram Reels using Retrieval-Augmented Generation (RAG), vector search, transcript intelligence, and contextual AI reasoning.

The platform enables creators to upload two video URLs, automatically extract transcripts and metadata, calculate engagement metrics, store transcript embeddings in a vector database, and interact with an AI analyst capable of answering context-aware questions about performance, engagement, hooks, audience signals, creator strategy, and content optimization.

This project was built as part of the Techsolv Full Stack AI Engineer Technical Challenge.

---

## Challenge Requirements Covered

### Video URL Processing

Supported Platforms:

* YouTube Videos
* Instagram Reels

Extracted Data:

* Video Title
* Creator Name
* Follower Count
* Views
* Likes
* Comments
* Upload Date
* Duration
* Hashtags
* Transcript

### Engagement Rate Calculation

The platform automatically calculates:

Engagement Rate = ((Likes + Comments) / Views) × 100

### Retrieval-Augmented Generation (RAG)

The system:

1. Extracts transcripts
2. Splits transcripts into chunks
3. Generates embeddings
4. Stores embeddings inside ChromaDB
5. Retrieves relevant transcript chunks
6. Generates grounded AI responses

### AI Chat Interface

Users can ask questions such as:

* Why did Video A outperform Video B?
* What is the engagement rate of each video?
* Compare the hooks in both videos.
* Suggest improvements for Video B.
* Which creator has stronger audience engagement?
* What transcript evidence supports this conclusion?

### Conversation Memory

The chatbot maintains memory across multiple interactions and uses previous conversations as context.

### Source Attribution

Responses include transcript sources:

* Video Identifier
* Chunk Identifier

This improves transparency and trustworthiness.

### Video Comparison Engine

The comparison module generates:

* Winner Selection
* Engagement Analysis
* Hook Analysis
* Creator Analysis
* Recommendations
* Action Plan
* Final Verdict

All results are generated dynamically.

---

## System Architecture

Frontend

React + Vite

↓

Backend

FastAPI

↓

Orchestration Layer

LangChain

↓

LLM

Google Gemini 2.5 Flash

↓

Retriever

↓

ChromaDB Vector Database

↓

Transcript Embeddings

---

## Technology Stack

### Frontend

* React
* Vite
* Axios
* JavaScript

### Backend

* FastAPI
* Python
* Uvicorn

### AI & RAG

* LangChain
* Gemini 2.5 Flash
* Sentence Transformers

### Vector Database

* ChromaDB

### Transcript Processing

* yt-dlp
* youtube-transcript-api

### Environment Management

* Python Virtual Environment
* python-dotenv

---

## Project Structure

```text
CreatorIQ-AI

├── backend
│   ├── app
│   │   ├── models
│   │   ├── rag
│   │   ├── routes
│   │   ├── services
│   │   ├── utils
│   │   └── main.py
│
├── frontend
│   ├── public
│   ├── src
│   │   ├── assets
│   │   ├── components
│   │   ├── pages
│   │   ├── services
│   │   ├── App.jsx
│   │   └── main.jsx
│
├── screenshots
│
├── docs
│
├── requirements.txt
├── .env.example
├── README.md
└── .gitignore
```

## Why ChromaDB?

I selected ChromaDB because:

* Lightweight and open source
* Simple setup for local development
* Strong LangChain integration
* No external infrastructure required
* Fast prototyping and experimentation

For large-scale production deployments, I would migrate to Qdrant or Pinecone to support distributed retrieval workloads.

---

## Why LangChain?

LangChain provides:

* Prompt orchestration
* Retrieval pipelines
* Output parsing
* Conversation management
* Memory integration
* Streaming support

This allowed the application to remain modular while reducing implementation complexity.

---

## Why Gemini 2.5 Flash?

Gemini 2.5 Flash was selected because:

* Fast inference speed
* Good reasoning capability
* Lower latency
* Cost-efficient deployment
* Strong transcript analysis performance

For creator analytics, it offers an effective balance between quality and operational cost.

---

## Chunking Strategy

Current Configuration:

```python
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
```

Reasoning:

* Large enough to preserve transcript context
* Small enough to maintain retrieval accuracy
* Overlap prevents information loss between chunks

Trade-Off:

Smaller chunks improve retrieval precision but may lose context.

Larger chunks preserve context but reduce retrieval relevance.

The selected configuration provides a balanced approach.

---

## Scalability Considerations

Current Architecture:

* FastAPI
* LangChain
* ChromaDB
* Gemini Flash
* Local Memory Store

Potential Bottlenecks at Scale:

* In-memory conversation storage
* Single FastAPI instance
* Local vector database
* Embedding generation latency

Production Improvements:

* Qdrant or Pinecone
* Redis Memory Layer
* Background Processing Queues
* Docker Containers
* Kubernetes Deployment
* Horizontal Scaling
* Cached Embeddings
* Cloud Storage

These improvements would allow the platform to efficiently support thousands of creators per day.

---

## Software Used During Development

Development Environment:

* Windows
* Visual Studio Code
* Git
* GitHub

Backend Libraries:

* FastAPI
* Uvicorn
* LangChain
* LangChain Google GenAI
* ChromaDB
* Sentence Transformers
* yt-dlp
* youtube-transcript-api
* python-dotenv

Frontend Libraries:

* React
* Vite
* Axios

AI Services:

* Google Gemini 2.5 Flash

---

## Environment Variables

Create a `.env` file and add:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
CHROMA_DB_PATH=./chroma_db
```

Example configuration is available in:

```text
.env.example
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>

cd CreatorIQ-AI
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

```bash
venv\Scripts\activate
```

### Install Backend Dependencies

```bash
pip install -r requirements.txt
```

### Start Backend

```bash
cd backend/app

uvicorn main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

### Start Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

---

## Screenshots

Project screenshots are available inside the screenshots directory.

Included:

* Dashboard
* Video A Analysis
* Video B Analysis
* AI Comparison Report
* RAG Chat Interface
* Architecture Diagram

---

## Future Improvements

* True token-level streaming
* Persistent user sessions
* Authentication
* Trend Analysis
* Sentiment Analysis
* Creator Benchmarking
* Cloud Deployment
* Advanced Analytics Dashboard

---

## Engineering Notes

This project was built with a focus on engineering trade-offs rather than simply connecting APIs.

Key considerations included:

* Retrieval Quality
* Cost Optimization
* Latency
* Scalability
* Maintainability
* Transparency through source attribution

The architecture provides a clear path from prototype to production deployment while maintaining explainability and creator-focused insights.

---

## Author

Author: Anurag Shrivas

Email: [anuragshrivas357@gmail.com](mailto:anuragshrivas357@gmail.com)

Contact: +91 7089385383

LinkedIn: https://www.linkedin.com/in/anuragshrivas027

GitHub: https://github.com/anuragshrivas027

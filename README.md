# CreatorIQ AI - Full Stack RAG Video Intelligence Platform

## Live Application

Frontend (Vercel)

https://creator-iq-ai.vercel.app/

Backend (Railway)

https://creatoriq-ai-production.up.railway.app/

API Documentation

https://creatoriq-ai-production.up.railway.app/docs

---

## Project Overview

CreatorIQ AI is a Full Stack AI-powered Video Intelligence Platform that analyzes and compares YouTube videos and Instagram Reels using Retrieval-Augmented Generation (RAG), Vector Search, Embeddings, and Large Language Models.

The goal of this project was not simply to connect APIs together. The objective was to build a system capable of understanding video content, retrieving relevant transcript information, comparing creator performance, maintaining conversational memory, and generating actionable insights for content creators.

The platform accepts two social media video URLs, extracts transcripts and metadata, calculates engagement metrics, stores transcript embeddings in a vector database, and allows users to interact with an AI Video Analyst capable of answering context-aware questions about performance, hooks, audience behavior, content strategy, and optimization opportunities.

---

## Challenge Requirements Covered

### Supported Platforms

* YouTube Videos
* YouTube Shorts
* Instagram Reels

### Extracted Information

For every video, the system attempts to collect:

* Video Title
* Creator Name
* Follower Count
* Views
* Likes
* Comments
* Upload Date
* Duration
* Hashtags
* Description
* Transcript

### Engagement Rate Calculation

The platform automatically calculates:

```text
Engagement Rate = ((Likes + Comments) / Views) × 100
```

This metric is used throughout the comparison and recommendation pipeline.

---

## What The Application Can Do

### Analyze Individual Videos

Users can upload:

* One YouTube Video
* One Instagram Reel

and receive:

* Transcript Intelligence
* Metadata Analysis
* Engagement Metrics
* Creator Information

### Compare Two Videos

Supported Combinations:

* YouTube vs YouTube
* Instagram vs Instagram
* YouTube vs Instagram
* Instagram vs YouTube

The AI comparison engine generates:

* Winner Selection
* Engagement Analysis
* Hook Analysis
* Creator Analysis
* Recommendations
* Action Plan
* Final Verdict

### AI Video Analyst Chat

The chatbot can answer questions such as:

* Why did Video A outperform Video B?
* What is the engagement rate of each video?
* Compare the hooks in the first few seconds.
* Suggest improvements for Video B.
* Which creator has stronger audience engagement?
* What transcript evidence supports this conclusion?
* Compare storytelling approaches.
* What content strategy should be reused?

### Conversational Memory

The chatbot maintains memory across multiple interactions.

Example:

User:
Which video performed better?

User:
Why?

User:
Give three improvements.

The chatbot remembers previous context and continues the conversation naturally.

### Streaming Responses

AI responses are streamed in real time using FastAPI StreamingResponse, reducing perceived latency and improving user experience.

---

## System Architecture

```text
User

↓

React Frontend

↓

FastAPI Backend

↓

Video Processing Layer

↓

Transcript Extraction

↓

Chunking

↓

Embedding Generation

↓

ChromaDB Vector Store

↓

LangChain Retrieval

↓

Gemini 2.5 Flash

↓

AI Insights & Recommendations
```

---

## Technology Stack

### Frontend

* React
* Vite
* JavaScript
* Axios

### Backend

* Python
* FastAPI
* Uvicorn

### AI & RAG

* LangChain
* Gemini 2.5 Flash
* Sentence Transformers

### Vector Database

* ChromaDB

### Video Processing

* yt-dlp
* youtube-transcript-api

### Deployment

* Railway
* Vercel

### Development Tools

* Visual Studio Code
* Git
* GitHub

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
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

---

## Why I Chose ChromaDB

For this challenge, I intentionally selected ChromaDB instead of Pinecone or Qdrant.

The primary reason was development speed and simplicity. I wanted a vector database that could run locally without requiring additional cloud infrastructure while I focused on transcript retrieval quality and the RAG workflow.

Advantages:

* Open Source
* Lightweight
* Easy Setup
* Strong LangChain Integration
* No External Infrastructure Required

Trade-Off:

While ChromaDB is excellent for development and prototyping, I would migrate to Qdrant or Pinecone for production-scale workloads because they offer better horizontal scalability, distributed retrieval, monitoring, and operational reliability.

---

## Why I Chose LangChain

LangChain simplified the orchestration layer by providing:

* Prompt Management
* Retrieval Pipelines
* Output Parsing
* Conversation Management
* Streaming Support
* Memory Integration

Instead of building custom retrieval pipelines from scratch, LangChain allowed me to focus on retrieval quality and application logic.

---

## Why I Chose Gemini 2.5 Flash

Gemini 2.5 Flash was selected because:

* Fast inference speed
* Strong reasoning capabilities
* Lower latency
* Cost-effective deployment
* Excellent transcript analysis performance

For creator analytics, it provides a strong balance between quality, speed, and cost.

---

## Embedding Strategy

Embedding Model:

```text
all-MiniLM-L6-v2
```

Reasons:

* Lightweight
* Fast
* Free
* Good semantic retrieval quality
* Low infrastructure requirements

Embedding Dimension:

```text
384
```

This model was sufficient for transcript retrieval while keeping embedding generation efficient.

---

## Chunking Strategy

Current Configuration:

```python
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
```

This decision was made after evaluating the trade-off between context preservation and retrieval precision.

Smaller Chunks:

* Better retrieval precision
* Increased risk of losing context

Larger Chunks:

* Better context retention
* Reduced retrieval relevance

The selected configuration provided a balanced approach for transcript-based retrieval.

The overlap helps preserve meaning between adjacent chunks and prevents important information from being split across chunk boundaries.

---

## Retrieval-Augmented Generation (RAG)

Pipeline:

```text
Transcript

↓

Chunking

↓

Embeddings

↓

ChromaDB

↓

Similarity Search

↓

Relevant Chunks Retrieved

↓

Gemini 2.5 Flash

↓

Grounded Response
```

Why RAG?

Without retrieval, the system would need to send entire transcripts to the LLM repeatedly.

RAG reduces:

* Token consumption
* Latency
* Cost

while improving factual grounding.

---

## Development Journey

This project went through multiple iterations during development.

Initially, the focus was on transcript extraction and metadata processing.

Once video ingestion worked reliably, the next phase involved:

* Chunking strategy selection
* Embedding generation
* ChromaDB integration
* LangChain orchestration
* Conversational memory
* Streaming responses

Deployment introduced additional engineering challenges involving dependency management, transcript extraction reliability, cloud deployment behavior, environment variables, API integration, and production debugging.

The final deployed system successfully supports transcript retrieval, video comparison, conversational memory, and AI-powered creator insights.

---

## Software Installed During Development

### Operating System

* Windows

### Development Environment

* Visual Studio Code
* Git
* GitHub

### Frontend

* Node.js
* npm
* React
* Vite
* Axios

### Backend

* Python
* FastAPI
* Uvicorn
* LangChain
* LangChain Google GenAI
* ChromaDB
* Sentence Transformers
* yt-dlp
* youtube-transcript-api
* python-dotenv

### AI Services

* Google Gemini 2.5 Flash

### Deployment Platforms

* Railway
* Vercel

---

## Installation Guide

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

### Create Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
CHROMA_DB_PATH=./chroma_db
```

### Run Backend

```bash
cd backend/app

uvicorn main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

### Run Frontend

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

## Scalability Considerations

Current Architecture:

* FastAPI
* LangChain
* ChromaDB
* Gemini Flash
* In-Memory Conversation Storage

This architecture is suitable for development, prototyping, demonstrations, and small-to-medium workloads.

---

## What Breaks At 10,000 Users?

The first bottlenecks would likely be:

### In-Memory Conversation Storage

Current memory is stored in application memory.

A restart would clear conversation history.

Production Solution:

* Redis

### ChromaDB

While ChromaDB works well for development, production workloads would benefit from:

* Pinecone
* Qdrant
* Weaviate

### Embedding Generation

Generating embeddings synchronously for every upload becomes expensive at scale.

Production Solution:

* Background workers
* Embedding cache
* Queue-based processing

### Single Backend Instance

A single FastAPI instance becomes a bottleneck.

Production Solution:

* Docker Containers
* Load Balancers
* Kubernetes
* Horizontal Scaling

---

## Production Upgrade Path

If this platform were supporting thousands of creators daily, I would redesign the architecture as:

```text
React Frontend

↓

Load Balancer

↓

FastAPI Cluster

↓

Redis

↓

PostgreSQL

↓

Pinecone / Qdrant

↓

Gemini
```

This would provide better scalability, reliability, and operational control.

---

## Testing Completed

Successfully Verified:

* YouTube vs YouTube
* Instagram vs Instagram
* YouTube vs Instagram
* Instagram vs YouTube

Verified Features:

* Video Analysis
* Transcript Extraction
* Metadata Extraction
* Engagement Calculation
* AI Comparison
* RAG Retrieval
* Conversational Memory
* Streaming Responses
* Frontend Deployment
* Backend Deployment

---

## Future Improvements

* TikTok Support
* Persistent User Sessions
* Authentication
* Redis-Based Memory
* Pinecone Integration
* Qdrant Integration
* Trend Analysis
* Sentiment Analysis
* Creator Benchmarking
* Audience Segmentation
* Multi-Language Support
* Advanced Analytics Dashboard

---

## Engineering Notes

This project was built with a focus on engineering trade-offs rather than simply connecting APIs together.

Important considerations included:

* Retrieval Quality
* Cost Optimization
* Latency
* Scalability
* Maintainability
* Explainability
* Deployment Reliability

Every major decision in the project can be defended through performance, maintainability, scalability, or cost considerations.

The goal was not only to make the system work, but to understand:

* Why this vector database was selected
* Why this chunk size was selected
* What breaks at scale
* How the architecture evolves in production
* Which trade-offs were made and why

Those considerations guided the design and implementation of this project from start to finish.

---

## Author

Author: Anurag Shrivas

Email: [anuragshrivas357@gmail.com](mailto:anuragshrivas357@gmail.com)

Contact: +91 7089385383

LinkedIn: https://www.linkedin.com/in/anuragshrivas027

GitHub: https://github.com/anuragshrivas027

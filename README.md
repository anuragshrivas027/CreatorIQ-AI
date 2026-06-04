# CreatorIQ AI - Full Stack RAG Video Intelligence Platform

## Live Application

Frontend (Vercel)

https://creator-iq-ai.vercel.app/

Backend (Railway)

https://creatoriq-ai-production.up.railway.app/

API Documentation

https://creatoriq-ai-production.up.railway.app/docs

---

# Project Overview

CreatorIQ AI is a Full Stack AI-powered Video Intelligence Platform built to analyze, compare, and understand social media video performance using Retrieval-Augmented Generation (RAG), Vector Search, Embeddings, and Large Language Models.

The platform allows creators, marketers, and analysts to upload two social media video URLs and receive detailed AI-powered insights about engagement, content quality, creator performance, hooks, storytelling, audience interaction, and content strategy.

Unlike a traditional chatbot, CreatorIQ AI combines transcript intelligence, metadata analysis, vector retrieval, memory-aware conversations, and AI reasoning to provide grounded responses supported by video content.

The objective of this project was not simply to connect APIs together. The goal was to build a complete end-to-end system capable of:

- Extracting video metadata
- Extracting transcripts
- Generating embeddings
- Building a searchable knowledge base
- Performing semantic retrieval
- Maintaining conversation memory
- Comparing creator performance
- Generating actionable recommendations

The final result is a production-style Full Stack RAG application deployed on Railway and Vercel.

---

# Challenge Requirements Covered

## Supported Platforms

- YouTube Videos
- YouTube Shorts
- Instagram Reels

## Input

The application accepts:

- Video URL A
- Video URL B

Supported combinations:

- YouTube vs YouTube
- Instagram vs Instagram
- YouTube vs Instagram
- Instagram vs YouTube

---

# Metadata Extracted

For every video the system attempts to extract:

- Video Title
- Creator Name
- Follower Count
- Views
- Likes
- Comments
- Duration
- Upload Date
- Description
- Hashtags
- Transcript

---

# Engagement Rate Calculation

The platform automatically calculates:

```text
Engagement Rate = ((Likes + Comments) / Views) × 100
```

This metric is used throughout the comparison engine and recommendation workflow.

---

# Core Features

## Video Analysis

Users can upload:

- One YouTube Video
- One Instagram Reel

and receive:

- Transcript Analysis
- Metadata Analysis
- Engagement Metrics
- Creator Information
- Performance Insights

---

## AI Video Comparison

The system compares Video A and Video B and generates:

- Winner Selection
- Engagement Analysis
- Hook Analysis
- Creator Analysis
- Transcript Analysis
- Recommendations
- Action Plan
- Final Verdict

The comparison engine uses actual transcript context and engagement data instead of relying purely on metadata.

---

## Retrieval-Augmented Generation (RAG)

Transcripts are:

1. Extracted
2. Chunked
3. Embedded
4. Stored in ChromaDB

When a user asks a question:

1. Relevant chunks are retrieved
2. Context is assembled
3. Gemini receives only the relevant information
4. Grounded responses are generated

This significantly reduces hallucinations and improves factual accuracy.

---

## AI Video Analyst Chat

Example Questions:

- Why did Video A outperform Video B?
- What is the engagement rate of each video?
- Compare the hooks used in both videos.
- Suggest improvements for Video B.
- Which creator has stronger audience engagement?
- What transcript evidence supports this conclusion?
- Compare storytelling approaches.
- What content strategy should be reused?

---

## Conversation Memory

The chatbot maintains memory across multiple interactions.

Example:

User:

```text
Which video performed better?
```

User:

```text
Why?
```

User:

```text
Give me three improvements.
```

The system remembers previous conversation context and continues naturally.

---

## Streaming Responses

Responses are streamed using FastAPI StreamingResponse.

Benefits:

- Reduced perceived latency
- Better user experience
- Real-time answer generation
- Improved responsiveness

---

# System Architecture

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

ChromaDB Vector Database

↓

LangChain Retrieval

↓

Gemini 2.5 Flash

↓

AI Insights & Recommendations
```

---

# Technology Stack

## Frontend

- React
- Vite
- JavaScript
- Axios

## Backend

- Python
- FastAPI
- Uvicorn

## AI & RAG

- LangChain
- Gemini 2.5 Flash
- Sentence Transformers

## Vector Database

- ChromaDB

## Video Processing

- yt-dlp
- youtube-transcript-api

## Deployment

- Railway
- Vercel

## Development Tools

- Visual Studio Code
- Git
- GitHub

---

# Complete Project Structure

```text
CreatorIQ-AI

├── backend
│
│   ├── app
│   │
│   │   ├── main.py
│   │   │
│   │   │   FastAPI application entry point.
│   │   │   Registers routes, middleware,
│   │   │   CORS configuration and API startup.
│   │
│   │   ├── models
│   │   │
│   │   ├── video_model.py
│   │   │   Request schema for video URLs.
│   │   │
│   │   └── chat_model.py
│   │       Request schema for chat questions.
│   │
│   │   ├── routes
│   │   │
│   │   ├── video_routes.py
│   │   │   YouTube and Instagram endpoints.
│   │   │
│   │   ├── compare_routes.py
│   │   │   Video comparison endpoint.
│   │   │
│   │   └── chat_routes.py
│   │       Chat and streaming endpoints.
│   │
│   │   ├── services
│   │   │
│   │   ├── youtube_service.py
│   │   │   YouTube transcript and metadata extraction.
│   │   │
│   │   ├── instagram_service.py
│   │   │   Instagram Reel metadata extraction.
│   │   │
│   │   ├── video_processing_service.py
│   │   │   Coordinates transcript processing,
│   │   │   vector storage and metadata preparation.
│   │   │
│   │   ├── comparison_service.py
│   │   │   AI-powered video comparison engine.
│   │   │
│   │   └── metrics_service.py
│   │       Engagement rate calculations.
│   │
│   │   ├── rag
│   │   │
│   │   ├── rag_pipeline.py
│   │   │   Core Retrieval-Augmented Generation workflow.
│   │   │
│   │   ├── process_video.py
│   │   │   Transcript processing pipeline.
│   │   │
│   │   ├── text_splitter.py
│   │   │   Transcript chunk generation.
│   │   │
│   │   ├── embedding_service.py
│   │   │   Embedding generation using
│   │   │   all-MiniLM-L6-v2.
│   │   │
│   │   ├── chroma_client.py
│   │   │   ChromaDB initialization.
│   │   │
│   │   ├── vector_store.py
│   │   │   Vector insertion and retrieval.
│   │   │
│   │   ├── memory_manager.py
│   │   │   Conversation memory management.
│   │   │
│   │   └── prompt_templates.py
│   │       AI system prompts.
│   │
│   │   └── utils
│   │
│   │       └── video_registry.py
│   │           Stores Video A and Video B.
│
├── frontend
│
│   ├── public
│   │
│   │   Static frontend assets.
│   │
│   ├── src
│   │
│   │   ├── main.jsx
│   │   │   React entry point.
│   │   │
│   │   ├── App.jsx
│   │   │   Root application component.
│   │   │
│   │   ├── services
│   │   │
│   │   └── api.js
│   │       Backend communication layer.
│   │
│   │   ├── components
│   │   │
│   │   │   Reusable UI components.
│   │
│   │   ├── pages
│   │   │
│   │   │   Application views.
│   │
│   │   ├── assets
│   │   │
│   │   │   Images and static resources.
│   │
│   │   └── styles
│   │
│   │       Styling and layouts.
│
├── requirements.txt
│
│   Backend dependencies.
│
├── package.json
│
│   Frontend dependencies.
│
├── .env.example
│
│   Example environment variables.
│
├── README.md
│
│   Project documentation.
│
└── .gitignore
│
    Git exclusion rules.
```

---

# End-to-End Data Flow

```text
User Uploads Video URL

↓

video_routes.py

↓

youtube_service.py / instagram_service.py

↓

video_processing_service.py

↓

process_video.py

↓

text_splitter.py

↓

embedding_service.py

↓

vector_store.py

↓

ChromaDB

↓

rag_pipeline.py

↓

Gemini 2.5 Flash

↓

Final AI Response
```

---

# Why I Chose ChromaDB

For this challenge, I intentionally selected ChromaDB instead of Pinecone or Qdrant.

Reasons:

- Open Source
- Lightweight
- Easy Local Setup
- Strong LangChain Integration
- No Additional Infrastructure Required

Trade-Off:

For large-scale production workloads, I would migrate to:

- Pinecone
- Qdrant
- Weaviate

for better scalability, distributed retrieval, monitoring, and operational reliability.

---

# Why I Chose LangChain

LangChain simplified:

- Prompt Management
- Retrieval Pipelines
- Output Parsing
- Memory Management
- Streaming Responses
- Context Assembly

Instead of building retrieval orchestration manually, LangChain allowed faster development and cleaner architecture.

---

# Why I Chose Gemini 2.5 Flash

Gemini 2.5 Flash provides:

- Fast inference speed
- Strong reasoning capabilities
- Lower latency
- Good transcript understanding
- Cost-effective deployment

For creator analytics, it provides an excellent balance of quality, speed, and cost.

---

# Embedding Strategy

Embedding Model:

```text
all-MiniLM-L6-v2
```

Reasons:

- Lightweight
- Fast
- Free
- High-quality semantic retrieval
- Low infrastructure cost

Embedding Dimension:

```text
384
```

---

# Chunking Strategy

Current Configuration:

```python
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
```

Trade-Off Analysis:

Smaller Chunks:

- Better retrieval precision
- Less context

Larger Chunks:

- Better context retention
- Lower retrieval precision

The selected configuration provides a balanced solution for transcript retrieval.

---

# Development Journey

The project evolved through multiple phases:

Phase 1

- Frontend setup
- Backend setup
- API integration

Phase 2

- YouTube extraction
- Instagram extraction
- Engagement calculations

Phase 3

- ChromaDB integration
- Embedding generation
- Transcript chunking

Phase 4

- LangChain orchestration
- RAG implementation
- Memory integration

Phase 5

- AI comparison engine
- Streaming responses
- Deployment

Phase 6

- Railway deployment
- Vercel deployment
- Production debugging
- Performance optimization

---

# Software Installed During Development

## Operating System

- Windows

## Development Environment

- Visual Studio Code
- Git
- GitHub

## Frontend

- Node.js
- npm
- React
- Vite
- Axios

## Backend

- Python
- FastAPI
- Uvicorn
- LangChain
- ChromaDB
- Sentence Transformers
- yt-dlp
- youtube-transcript-api
- python-dotenv

## AI Services

- Google Gemini 2.5 Flash

## Deployment Platforms

- Railway
- Vercel

---

# Testing Completed

Successfully Tested:

- YouTube vs YouTube
- Instagram vs Instagram
- YouTube vs Instagram
- Instagram vs YouTube

Verified Features:

- Transcript Extraction
- Metadata Extraction
- Engagement Calculation
- ChromaDB Storage
- Semantic Retrieval
- AI Comparison
- Conversational Memory
- Streaming Responses
- Frontend Deployment
- Backend Deployment

---

# What Breaks At 10,000 Users?

Potential bottlenecks:

## Memory Storage

Current:

- In-memory storage

Production:

- Redis

## ChromaDB

Current:

- Single-node vector database

Production:

- Pinecone
- Qdrant

## Embedding Generation

Current:

- Synchronous

Production:

- Background queues
- Worker services
- Caching

## Backend Scaling

Current:

- Single FastAPI instance

Production:

- Docker
- Kubernetes
- Load Balancers

---

# Production Upgrade Path

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

---

# Engineering Notes

This project was built with a focus on engineering trade-offs rather than simply connecting APIs together.

Important considerations included:

- Retrieval Quality
- Cost Optimization
- Latency
- Scalability
- Maintainability
- Explainability
- Deployment Reliability

Every major technical decision can be defended through performance, maintainability, scalability, or cost considerations.

The goal was not only to make the system work, but to understand:

- Why this vector database was selected
- Why this chunk size was selected
- What breaks at scale
- How the architecture evolves in production
- Which trade-offs were made and why

This project reflects the engineering mindset required to build systems that work today while remaining adaptable for tomorrow.

---

# Author

Author: Anurag Shrivas

Email: anuragshrivas357@gmail.com

Contact: +91 7089385383

LinkedIn: https://www.linkedin.com/in/anuragshrivas027

GitHub: https://github.com/anuragshrivas027
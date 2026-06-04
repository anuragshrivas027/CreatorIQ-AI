# CreatorIQ AI - Full Stack RAG Video Intelligence Platform

# Project Overview

CreatorIQ AI is a Full Stack AI-powered Video Intelligence Platform that analyzes and compares YouTube videos and Instagram Reels using Retrieval-Augmented Generation (RAG), Vector Search, Embeddings, and Large Language Models.

The objective of this project was not simply to connect APIs together. The goal was to build a complete system capable of understanding video content, extracting metadata, retrieving transcript context, comparing creator performance, maintaining conversational memory, and generating actionable recommendations for creators.

The platform accepts two social media video URLs, extracts transcripts and metadata, calculates engagement metrics, stores transcript embeddings in a vector database, and enables users to interact with an AI Video Analyst capable of answering context-aware questions grounded in actual video content.

This project was built to demonstrate engineering decision-making, system design, retrieval quality, deployment considerations, and scalability planning rather than simply demonstrating API integrations.

---

# Project Demonstration Video

Project Walkthrough Video

https://drive.google.com/file/d/1SWZdUrFZBPm8kdCwnS3djyp1ZEjYPgPG/view?usp=sharing

The demonstration video covers:

* End-to-End Application Workflow
* YouTube Video Analysis
* Instagram Reel Analysis
* AI-Powered Video Comparison
* Retrieval-Augmented Generation (RAG)
* ChromaDB Vector Search
* Conversational AI Video Analyst
* Engineering Decisions and Trade-Offs
* Scalability Considerations
* Production Upgrade Path

---

# Live Application

## Frontend (Vercel)

https://creator-iq-ai.vercel.app/

## Backend (Railway)

https://creatoriq-ai-production.up.railway.app/

## API Documentation

https://creatoriq-ai-production.up.railway.app/docs

---

# Challenge Requirements Covered

## Supported Platforms

* YouTube Videos
* YouTube Shorts
* Instagram Reels

## Metadata Extracted

For every video the system attempts to collect:

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

## Engagement Rate Calculation

```text
Engagement Rate = ((Likes + Comments) / Views) × 100
```

This metric is used throughout the comparison and recommendation pipeline.

---

# Core Features

## Video Analysis

Users can upload:

* One YouTube Video
* One Instagram Reel

and receive:

* Transcript Analysis
* Metadata Analysis
* Engagement Metrics
* Creator Information
* AI Insights

---

## AI Video Comparison

Supported combinations:

* YouTube vs YouTube
* Instagram vs Instagram
* YouTube vs Instagram
* Instagram vs YouTube

The comparison engine generates:

* Winner Selection
* Engagement Analysis
* Hook Analysis
* Creator Analysis
* Recommendations
* Action Plan
* Final Verdict

---

## Retrieval-Augmented Generation (RAG)

Transcripts are:

1. Extracted
2. Chunked
3. Embedded
4. Stored in ChromaDB

When users ask questions:

1. Relevant transcript chunks are retrieved.
2. Context is assembled.
3. Gemini receives only relevant information.
4. Grounded responses are generated.

This improves factual accuracy while reducing token usage and latency.

---

## AI Video Analyst Chat

Example questions:

* Why did Video A outperform Video B?
* What is the engagement rate of each video?
* Compare the hooks used in both videos.
* Suggest improvements for Video B.
* Which creator has stronger audience engagement?
* What transcript evidence supports this conclusion?
* Compare storytelling approaches.
* What content strategy should be reused?

---

## Conversation Memory

The chatbot maintains memory across multiple interactions.

Example:

User:

Which video performed better?

User:

Why?

User:

Give three improvements.

The system remembers previous context and continues naturally.

---

## Streaming Responses

Responses are streamed in real time using FastAPI StreamingResponse.

Benefits:

* Reduced perceived latency
* Better user experience
* Real-time answer generation
* Improved responsiveness

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

* React
* Vite
* JavaScript
* Axios

## Backend

* Python
* FastAPI
* Uvicorn

## AI & RAG

* LangChain
* Gemini 2.5 Flash
* Sentence Transformers

## Vector Database

* ChromaDB

## Video Processing

* yt-dlp
* youtube-transcript-api

## Deployment

* Railway
* Vercel

## Development Tools

* Visual Studio Code
* Git
* GitHub

---

# Complete Project Structure

```text
CreatorIQ-AI

├── backend
│
│   ├── app
│   │
│   ├── main.py
│   │   FastAPI application entry point.
│   │
│   ├── models
│   │
│   │   ├── video_model.py
│   │   │   Request schema for video URLs.
│   │   │
│   │   └── chat_model.py
│   │       Request schema for chat questions.
│   │
│   ├── routes
│   │
│   │   ├── video_routes.py
│   │   │   YouTube and Instagram endpoints.
│   │   │
│   │   ├── compare_routes.py
│   │   │   Video comparison endpoint.
│   │   │
│   │   └── chat_routes.py
│   │       Chat and streaming endpoints.
│   │
│   ├── services
│   │
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
│   ├── rag
│   │
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
│   │   │   Embedding generation using all-MiniLM-L6-v2.
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
│   └── utils
│
│       └── video_registry.py
│           Stores Video A and Video B.
│
├── frontend
│
│   ├── public
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
│   │   │   Reusable UI components.
│   │   │
│   │   ├── pages
│   │   │   Application views.
│   │   │
│   │   ├── assets
│   │   │   Images and static resources.
│   │   │
│   │   └── styles
│   │       Styling and layouts.
│
├── screenshots
│
│   ├── architecture.png
│   │   High-level system architecture diagram.
│   │
│   ├── dashboard.png
│   │   Main application dashboard.
│   │
│   ├── video-a-analysis.png
│   │   Video A analysis results.
│   │
│   ├── video-b-analysis.png
│   │   Video B analysis results.
│   │
│   ├── comparison-report.png
│   │   AI-generated comparison report.
│   │
│   └── rag-chat.png
│       RAG-powered AI Video Analyst chat.
│
├── requirements.txt
│   Backend dependencies.
│
├── package.json
│   Frontend dependencies.
│
├── .env.example
│   Example environment variables.
│
├── README.md
│   Project documentation.
│
└── .gitignore
    Git exclusion rules.
```

# Engineering Decisions and Trade-Offs

## Why ChromaDB?

For this challenge, I intentionally selected ChromaDB instead of Pinecone or Qdrant.

My primary objective was validating retrieval quality before introducing additional infrastructure complexity.

Advantages:

* Lightweight
* Open Source
* Fast Local Development
* Strong LangChain Integration
* No External Infrastructure Required

Trade-Off:

For a production environment supporting thousands of creators daily, I would migrate to Qdrant or Pinecone because they provide distributed indexing, horizontal scaling, monitoring, and higher operational reliability.

---

## Why LangChain?

LangChain simplified:

* Retrieval Pipelines
* Prompt Management
* Output Parsing
* Context Assembly
* Memory Management
* Streaming Responses

Rather than building custom orchestration from scratch, I used LangChain to focus on retrieval quality and application logic.

---

## Why Gemini 2.5 Flash?

Gemini 2.5 Flash provided:

* Strong reasoning capabilities
* Fast inference speed
* Lower latency
* Cost efficiency
* Good transcript understanding

For creator analytics, it offered the best balance between speed, quality, and cost.

---

# Embedding Strategy

Embedding Model:

```text
all-MiniLM-L6-v2
```

Reasons:

* Lightweight
* Fast
* Free
* Strong semantic retrieval performance
* Low infrastructure requirements

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

This configuration was selected after considering the trade-off between retrieval precision and context preservation.

Smaller Chunks:

* Better retrieval precision
* Increased risk of losing context

Larger Chunks:

* Better context retention
* Reduced retrieval accuracy

The selected configuration provided the best balance for transcript retrieval.

The overlap ensures important information is not lost across chunk boundaries.

---

# Engineering Challenges Encountered

One of the most interesting challenges during deployment involved YouTube transcript and metadata extraction.

While the application worked consistently in local development, some cloud deployments occasionally encountered restrictions caused by YouTube anti-bot protections against cloud-provider IP addresses.

Rather than immediately redesigning the architecture, I investigated deployment logs, validated application behavior, improved extraction configuration, and identified production-grade alternatives including:

* Whisper-based transcription
* Official APIs
* Dedicated ingestion services
* Fallback extraction pipelines

This reinforced an important engineering lesson:

Not every failure originates from application code. Sometimes the challenge is understanding the behavior and limitations of external systems.

Additional challenges included:

* Frontend and backend deployment coordination
* Environment variable management
* ChromaDB persistence configuration
* Streaming response integration
* RAG context quality tuning
* Embedding performance optimization

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

# Development Journey

This project evolved through several phases:

Phase 1

* Frontend setup
* Backend setup
* API integration

Phase 2

* YouTube extraction
* Instagram extraction
* Engagement calculations

Phase 3

* Transcript chunking
* Embedding generation
* ChromaDB integration

Phase 4

* LangChain orchestration
* Retrieval-Augmented Generation
* Memory implementation

Phase 5

* AI comparison engine
* Streaming responses
* UI improvements

Phase 6

* Railway deployment
* Vercel deployment
* Production debugging
* Stability testing

---

# Software Installed During Development

## Operating System

* Windows

## Development Environment

* Visual Studio Code
* Git
* GitHub

## Frontend

* Node.js
* npm
* React
* Vite
* Axios

## Backend

* Python
* FastAPI
* Uvicorn
* LangChain
* ChromaDB
* Sentence Transformers
* yt-dlp
* youtube-transcript-api
* python-dotenv

## AI Services

* Google Gemini 2.5 Flash

## Deployment Platforms

* Railway
* Vercel

---

# Installation and Local Setup

## Clone Repository

git clone ...

...

Frontend URL:

http://localhost:5173

---

## Production Deployment

Frontend (Vercel)

https://creator-iq-ai.vercel.app/

Backend (Railway)

https://creatoriq-ai-production.up.railway.app/

API Documentation

https://creatoriq-ai-production.up.railway.app/docs

---

# Testing Completed

Successfully Tested:

* YouTube vs YouTube
* Instagram vs Instagram
* YouTube vs Instagram
* Instagram vs YouTube

Verified Features:

* Transcript Extraction
* Metadata Extraction
* Engagement Calculation
* ChromaDB Storage
* Semantic Retrieval
* AI Comparison
* Conversational Memory
* Streaming Responses
* Frontend Deployment
* Backend Deployment

---

# What Breaks First at 10,000 Users?

The first component likely to become a bottleneck is conversation memory.

Current Implementation:

* In-memory storage

Production Solution:

* Redis

The second bottleneck would be embedding generation.

Current Implementation:

* Synchronous processing during uploads

Production Solution:

* Background workers
* Job queues
* Embedding cache

The third bottleneck would be ChromaDB.

Current Implementation:

* Single-node vector storage

Production Solution:

* Qdrant
* Pinecone
* Distributed vector infrastructure

The fourth bottleneck would be the backend itself.

Current Implementation:

* Single FastAPI instance

Production Solution:

* Docker
* Kubernetes
* Horizontal scaling
* Load balancing

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

Qdrant / Pinecone

↓

Gemini
```

---

# Future Improvements

* TikTok Support
* Persistent User Sessions
* Authentication
* Redis-Based Memory
* Qdrant Integration
* Pinecone Integration
* Trend Analysis
* Sentiment Analysis
* Audience Segmentation
* Creator Benchmarking
* Multi-Language Support
* Advanced Analytics Dashboard

---

# Final Notes

One of the key goals of this project was understanding the trade-offs behind technical decisions rather than simply making features work.

Important considerations included:

* Retrieval Quality
* Cost Optimization
* Latency
* Scalability
* Reliability
* Maintainability
* Explainability

Every major architectural decision in this project can be defended through performance, scalability, maintainability, or cost considerations.

The objective was not only to build a working application, but to understand:

* Why this vector database was selected
* Why this chunk size was selected
* What breaks at scale
* How the architecture evolves in production
* Which trade-offs were made and why

This project reflects the engineering mindset required to build systems that work today while remaining adaptable for future growth.

---

# Author

Author: Anurag Shrivas

Email: [anuragshrivas357@gmail.com](mailto:anuragshrivas357@gmail.com)

Contact: +91 7089385383

LinkedIn: https://www.linkedin.com/in/anuragshrivas027

GitHub: https://github.com/anuragshrivas027

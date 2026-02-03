# FastAPI Backend – AI PBX Call Processor

## Overview
This project implements a FastAPI-based backend microservice designed to handle
high-throughput call ingestion from a PBX system and orchestrate asynchronous AI
processing when human agents are unavailable.

The system is fully non-blocking and resilient to unreliable external AI services.

---

## Methodology
- Designed a non-blocking FastAPI endpoint for ingesting audio metadata packets
- Returned immediate `202 Accepted` responses to support high concurrency
- Offloaded AI transcription work to background async tasks
- Simulated unreliable external AI services with retries and exponential backoff
- Added a basic concurrency test to demonstrate race-condition awareness

---

## Technical Details
- **Framework:** FastAPI (async)
- **Database:** Async SQLAlchemy with SQLite (easily replaceable with PostgreSQL)
- **AI Simulation:** Mock service with 25% failure rate and 1–3s latency
- **Retry Strategy:** Exponential backoff using async services
- **Testing:** pytest with httpx.AsyncClient for concurrent request simulation

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/sunny7100/articence-fastapi.git
cd articence-fastapi

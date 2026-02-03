# FastAPI Backend – AI PBX Call Processor

## Overview

This project implements a **FastAPI-based backend microservice** designed to handle **high-throughput call ingestion** from a PBX system and orchestrate **asynchronous AI processing** when human agents are unavailable.

The service is built to be **fully non-blocking**, scalable, and resilient to the **unreliable nature of external AI APIs**, aligning with real-world Voice & AI system requirements.

---

## Methodology

- Designed a **non-blocking FastAPI endpoint** to ingest audio metadata packets
- Returned **immediate `202 Accepted` responses** to support thousands of concurrent calls
- Validated packet sequencing while **never blocking the ingestion pipeline**
- Offloaded AI transcription and sentiment processing to **background async tasks**
- Simulated **unreliable external AI services** with controlled failures
- Implemented **retry logic with exponential backoff** to ensure eventual processing
- Added a **basic concurrency test** to demonstrate race-condition awareness

---

## Technical Details

- **Framework:** FastAPI (async-first architecture)
- **API Endpoint:**  
  `POST /v1/call/stream/{call_id}`  
  Accepts audio metadata packets:
  ```json
  {
    "sequence": 1,
    "data": "sample_audio_chunk",
    "timestamp": 123.45
  }

  
Non-Blocking Design:
The endpoint responds within milliseconds and does not wait for AI processing.

Database:
Async SQLAlchemy with SQLite
(easily replaceable with PostgreSQL in production environments)

Call State Management:
Call lifecycle modeled using states such as:

IN_PROGRESS

PROCESSING_AI

COMPLETED

FAILED

ARCHIVED

AI Simulation:
Internal mock AI service with:

25% failure rate

Variable latency between 1–3 seconds

Retry Strategy:
Exponential backoff implemented in async background tasks to handle flaky AI responses.

Testing

Framework: pytest

HTTP Client: httpx.AsyncClient

Scenario Covered:
Simulated race condition where two packets arrive simultaneously for the same call_id, validating safe concurrent handling.




--Setup Instructions--------
1. Clone the repository
git clone https://github.com/sunny7100/articence-fastapi.git
cd articence-fastapi

2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows

3. Install dependencies
pip install -r requirements.txt

4. Run the application
uvicorn server:app --reload

5. Access API documentation
http://127.0.0.1:8000/docs

Notes

SQLite is used for simplicity; the async database layer is compatible with PostgreSQL.

WebSocket support can be added for real-time streaming if required in future iterations.

The focus of this task was non-blocking ingestion, reliability, and async orchestration.

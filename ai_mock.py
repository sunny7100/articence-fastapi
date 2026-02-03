import asyncio
import random

class FlakyAIService:
    """
    Simulates an unreliable external AI service.
    - 25% failure rate
    - Variable latency between 1–3 seconds
    """

    async def process(self, text: str) -> str:
        await asyncio.sleep(random.randint(1, 3))

        # 25% failure rate
        if random.random() < 0.25:
            raise Exception("503 Service Unavailable")

        return "Mock transcription result"

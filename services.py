import asyncio
from ai_mock import FlakyAIService

ai_service = FlakyAIService()

async def process_call_with_retry(call_id: str, text: str = ""):
    """
    Handles AI processing with retry and exponential backoff.
    This simulates unreliable external AI APIs.
    """
    delay = 1

    for attempt in range(3):
        try:
            result = await ai_service.process(text)
            print(f"[AI SUCCESS] Call {call_id}: {result}")
            return result
        except Exception as e:
            print(f"[AI FAILURE] Call {call_id}, attempt {attempt + 1}")
            await asyncio.sleep(delay)
            delay *= 2

    print(f"[AI FAILED PERMANENTLY] Call {call_id}")
    return None

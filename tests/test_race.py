import asyncio
import pytest
from httpx import AsyncClient
from server import app

@pytest.mark.asyncio
async def test_race_condition_same_call_id():
    """
    Simulates two packets arriving at the same time for the same call_id.
    The test passes if the API handles both requests without crashing.
    """

    async with AsyncClient(app=app, base_url="http://test") as client:

        payload1 = {
            "sequence": 1,
            "data": "chunk1",
            "timestamp": 1.0
        }

        payload2 = {
            "sequence": 2,
            "data": "chunk2",
            "timestamp": 2.0
        }

        async def send_packet(payload):
            return await client.post(
                "/v1/call/stream/test_race",
                json=payload
            )

        responses = await asyncio.gather(
            send_packet(payload1),
            send_packet(payload2)
        )

        assert responses[0].status_code == 202
        assert responses[1].status_code == 202

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from models import Call, Packet
import logging

router = APIRouter()
logging.basicConfig(level=logging.WARNING)

@router.post("/v1/call/stream/{call_id}", status_code=202)
async def ingest_packet(call_id: str, packet: dict, db: AsyncSession = Depends(get_db)):
    call = await db.get(Call, call_id)

    if not call:
        call = Call(id=call_id)
        db.add(call)
        await db.commit()

    if packet["sequence"] != call.last_sequence + 1:
        logging.warning("Packet sequence mismatch")

    call.last_sequence = packet["sequence"]
    db.add(Packet(call_id=call_id, sequence=packet["sequence"]))
    await db.commit()

    return {"status": "accepted"}

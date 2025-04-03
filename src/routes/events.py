from fastapi import APIRouter

event_router = APIRouter(
    prefix="/events",
    tags=["EVents"]
)


@event_router.get("/")
async def get_all_events():
    return[]

@event_router.get("/{id}")
async def get_event():
    return ""

@event_router.post("/")
async def creat_event():
    return "" 

@event_router.put("/")
async def update_event():
    return ""

@event_router.delete("/{id}")
async def delete_event():
    return ""
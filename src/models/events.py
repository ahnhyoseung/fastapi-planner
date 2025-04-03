from pydantic import BaseModel, ConfigDict



class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: list[str]
    location: str
    created_at: str
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": 1,
                "title": "아.. 집가고 싶다",
                "image": "path/to"
                "description": "아 진짜 가고싶다다"
                "tags": ["#fckkk"]
                "location": "seoul"
            }
        }
    )
    
    
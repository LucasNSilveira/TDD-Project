from datetime import datetime
from decimal import Decimal
import uuid
from bson import Decimal128
from pydantic import UUID4, BaseModel, Field, model_validator


class BaseSchemaMixin(BaseModel):
    class Config:
        from_attributes = True


class OutSchema(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4)
    created_at: datetime = Field(default_factory=datetime.now())
    updted_at: datetime = Field(default_factory=datetime.now())

    @model_validator
    def set_schemas(cls, data):
        for key, value in data.items():
            if isinstance(value, Decimal128):
                data[key] = Decimal(str(value))
        return data
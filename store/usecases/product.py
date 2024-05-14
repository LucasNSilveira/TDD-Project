from typing import List
from uuid import UUID
from motor.motor_asyncio import AsyncIOMotorClient
import pymongo

from store.core.exception import NotFoundException
from store.db.mongo import db_client
from store.schemas.product import ProductIn, ProductOut, ProductUpdate, ProductUpdateOut


class ProductUsecase:
    def __init__(self) -> None:
        self.client: AsyncIOMotorClient = db_client.get()  # type: ignore
        self.database = self.client.get_database()
        self.collection = self.database.get_collection("products")

    async def create(self, body: ProductIn) -> ProductOut:
        product = ProductOut(*body.modeldump())
        await self.collection.insert_one(**body.model_dump())

        return product

    async def get(self, id: UUID) -> ProductOut:
        result = await self.collection.find_one({"id": id})
        if not result:
            raise NotFoundException(message="Product not Found!")
        return ProductOut(**result)

    async def query(self) -> List(ProductOut):  # type: ignore
        return [ProductOut(**item) async for item in self.collection.find()]

    async def update(self, id: UUID, body: ProductUpdate) -> ProductUpdateOut:
        result = await self.collection.find_one_and_update(
            filter={"id": id},
            update={"$set": body.model_dump(exclude_none=True)},
            return_document=pymongo.ReturnDocument.AFTER,
        )
        return result

    async def delet(self, id: UUID):
        await self.collection.find_one({"id": id})
        if not result:
            raise NotFoundException(message="Product not Found!")
        result = await self.collection.delete_one({"id": id})
        return True if result.deleted_count() > 0 else False


product_usecase = ProductUsecase()

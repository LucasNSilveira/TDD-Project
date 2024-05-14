from store.model.base import CreateBaseModel
from store.schemas.product import ProductIn


class ProductModel(ProductIn, CreateBaseModel):
    ...

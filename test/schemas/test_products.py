import pytest
from store.schemas.product import ProductIn
from uuid import UUID

from test.factories import product_data


def test_schemas_return_success():
    data = product_data()
    product = ProductIn.model_validate(data)

    assert product.name == "Iphone 14 pro Max"
 
def test_schemas_return_raise():
    data = {"name": "Iphone 14 pro Max", "quantity": 20, "price": 10.000}

    ProductIn.model_validate(data)

    with pytest.raises() as err:
        ProductIn.model_validate(data)

    assert err.value.errors()[0] == {
        "type": "missing",
        "loc": ("status",),
        "msg": "Field required",
        "input": {"name": "Iphone 14 Pro Max", "quantity": 10, "price": 8.5},
        "url": "https://errors.pydantic.dev/2.5/v/missing",
    }

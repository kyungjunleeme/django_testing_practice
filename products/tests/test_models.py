from mixer.backend.django import mixer
import pytest

# RuntimeError: Mixer (products.Product): Database access not allowed,
# use the "django_db" mark, or the "db" or "transactional_db" fixtures to enable it.

# @pytest.mark.django_db
# class TestModels:


@pytest.fixture
def product(request, db):
    return mixer.blend("products.Product", quantity=request.param)


@pytest.mark.parametrize("product", [1], indirect=True)
def test_product_is_in_stock(product):
    # product = mixer.blend("products.Product", quantity=1)
    assert product.is_in_stock == True


@pytest.mark.parametrize("product", [0], indirect=True)
def test_product_is_not_in_stock(product):
    # product = mixer.blend("products.Product", quantity=0)
    assert product.is_in_stock == False

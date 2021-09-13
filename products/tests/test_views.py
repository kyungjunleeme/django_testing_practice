from attr import Factory
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth import get_user_model
from products.views import product_detail
from mixer.backend.django import mixer
from django.test import TestCase
import pytest

User = get_user_model()


# @pytest.mark.django_db
# class TestViews(TestCase):

# @classmethod
# def setUpClass(cls):
#     super().setUpClass()
#     mixer.blend("products.Product")
#     cls.factory = RequestFactory()

# 호출순서가 그래요.
# setUpClass 가 가장먼저 실행되고, 그럼 이때 (클래스).factory 가능해져요.
# 그리고나서 self.factory 하면 인스턴스 레벨에는 factory가 없으니 클래스레벨까지 보게되는데
# 클래스레벨에는 factory 가 있게되서 접근되는겁니다


@pytest.fixture(scope="module")
def factory():
    print("FACTORY INSTANTIATED")
    return RequestFactory()


@pytest.fixture
def product(db):
    return mixer.blend("products.Product")


def test_product_detail_authenticated(factory, product):
    # mixer.blend("products.Product")

    path = reverse("products:product_detail", kwargs={"pk": 1})
    request = factory.get(path)
    request.user = mixer.blend(User)

    response = product_detail(request, pk=1)
    assert response.status_code == 200


def test_product_detail_unauthenticated(factory, product):

    path = reverse("products:product_detail", kwargs={"pk": 1})
    # https://stackoverflow.com/questions/44460724/can-i-access-class-variables-using-self
    request = factory.get(path)  # request = self.factory.get(path)
    request.user = AnonymousUser()

    response = product_detail(request, pk=1)
    # FAILED products/tests/test_views.py::TestViews::test_product_detail_unauthenticated - assert 302 == 200
    assert "accounts/login" in response.url

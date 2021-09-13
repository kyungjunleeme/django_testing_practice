from django.urls import reverse, resolve


class TestUrls:
    def test_detail(self):
        path = reverse("products:product_detail", kwargs={"pk": 1})
        assert resolve(path).view_name == "products:product_detail"

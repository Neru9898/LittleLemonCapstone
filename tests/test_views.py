from django.test import TestCase
from LittleLemonAPI.models import Menu


class MenuTest(TestCase):
    def setUp(self):
        Menu.objects.create(id=1, title="IceCream", price=45.50, inventory=100)
        Menu.objects.create(id=2, title="Steak", price=5.50, inventory=40)
        Menu.objects.create(id=3, title="Chicken",
                            price=145.50, inventory=1010)
        Menu.objects.create(id=4, title="Salad", price=445.50, inventory=110)
        Menu.objects.create(id=5, title="Cream", price=4.50, inventory=10)

    def test_getall(self):
        item = Menu.objects.all()

        self.assertQuerysetEqual(item, Menu.objects.all(), ordered=False)

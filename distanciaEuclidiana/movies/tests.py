from django.test import TestCase

from .views import get_distances

class MoviesTest(TestCase):
    def setUp(self):
        self.point_ok = {
            "coordinate_X": 2,
            "coordinate_Y": 3
        }

    def test_get_distances_ok(self):
        self.assertIs(type(get_distances(self.point_ok)), dict().__class__)

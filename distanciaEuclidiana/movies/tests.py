from django.test import TestCase

from .views import get_distances, get_nearest_distances, get_new_resultado

class MoviesTest(TestCase):
	def setUp(self):
		self.point_ok = {
			"coordinate_X": 2,
			"coordinate_Y": 3
		}

        self.distances_ok = {
			'1': {'resultado' : 0, 'distance' : 2},
			'2': {'resultado' : 1, 'distance': 4}, 
			'3': {'resultado' : 1, 'distance' : 3}
		}

        self.distances_sorted = {
			'1': {'resultado' : 0, 'distance' : 2}, 
			'3': {'resultado' : 1, 'distance' : 3}
		}


	def test_get_distances_ok(self):
		self.assertIs(type(get_distances(self.point_ok)), dict().__class__)

	def test_get_nearest_distances_ok(self):
		self.assertIs(type(get_nearest_distances(self.distances_ok, 3)), dict().__class__)

	def test_get_nearest_distances_sort_ok(self):
		self.assertEquals(get_nearest_distances(self.distances_ok,2), self.distances_sorted)

	def test_get_new_resultado_ok(self):
		self.assertEquals(get_new_resultado(self.distances_ok), 1)


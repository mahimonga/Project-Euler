import sys
sys.path.insert(1, "../../")
import Problem4_11.largest_product_in_a_grid as tools
import unittest

class TestLargestProductInGrid(unittest.TestCase):
    def setUp(self) -> None:
        self.Row1 = [1, 2, 9, 0, 40, 2, 30, 8, 9, 89, 9, 7, 76, 2, 1, 9]
        self.Row2 = [12, 32, 39, 10, 40, 22, 30, 87, 59, 89, 19, 7, 76, 20, 21, 9]
        self.Column1 = [1, 9, 29, 8, 47, 0, 30, 17, 0, 84, 2, 1, 6, 2, 21, 2]
        self.Column2 = [3, 22, 93, 1, 40, 22, 33, 67, 94, 92, 29, 57, 76, 20, 21, 9]
        self.Diagnol1 =

    def test_maximumProductInRow(self):
        self.assertTrue(tools.left_to_right(self.Row1), 426132)
        self.assertFalse(tools.left_to_right(self.Row2), 32)

    def test_maximumProductInColumn(self):
        self.assertTrue(tools.top_to_bottom(self.Column1), 98136)
        self.asserFalse(tools.top_to_bottom(self.Column2), 0)




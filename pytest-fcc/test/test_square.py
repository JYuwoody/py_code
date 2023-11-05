import pytest
import source.shapes as shapes

@pytest.mark.parametrize("side_length, excepted_area", [(5, 25),(4, 16), (9, 81)])
def test_multiple_square_areas(side_length, excepted_area):
    assert shapes.Square(side_length).area() == excepted_area


@pytest.mark.parametrize("side_length, excepted_perimeter", [(3, 12),(4, 16), (5, 20)])
def test_multiple_perimeter(side_length, excepted_perimeter):
    assert shapes.Square(side_length).perimeter() == excepted_perimeter    
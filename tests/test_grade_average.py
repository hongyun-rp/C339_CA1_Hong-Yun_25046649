import pytest
from src.grade_average import calculate_average


@pytest.mark.parametrize(
    "mark_one, mark_two, expected",
    [
        (0, 0, 0),  # Lowest marks allowed
        (100, 100, 100),  # Highest marks allowed
    ],
)
def test_marks_boundary_valid(mark_one, mark_two, expected):
    # Act
    result = calculate_average(mark_one, mark_two)
    # Assert
    assert result == expected


def test_marks_whole_number_average_valid():
    # Arrange
    mark_one = 40
    mark_two = 60
    # Act
    result = calculate_average(mark_one, mark_two)
    # Assert
    assert result == 50


def test_marks_decimal_average_valid():
    # Arrange
    mark_one = 50
    mark_two = 51
    # Act
    result = calculate_average(mark_one, mark_two)
    # Assert
    assert result == 50.5


@pytest.mark.parametrize(
    "mark_one, mark_two",
    [
        (-1, 50),  # mark_one below 0
        (101, 50),  # mark_one above 100
        (50, -1),  # mark_two below 0
        (50, 101),  # mark_two above 100
    ],
)
def test_marks_boundary_invalid(mark_one, mark_two):
    # Act and Assert
    with pytest.raises(ValueError):
        calculate_average(mark_one, mark_two)


@pytest.mark.parametrize(
    "mark_one, mark_two",
    [
        (50.5, 50),  # mark_one is a float
        ("50", 50),  # mark_one is a string
        (None, 50),  # mark_one is missing
        (True, 50),  # mark_one is a boolean
        (50, 50.5),  # mark_two is a float
        (50, "50"),  # mark_two is a string
        (50, None),  # mark_two is missing
        (50, True),  # mark_two is a boolean
    ],
)
def test_marks_type_invalid(mark_one, mark_two):
    # Act and Assert
    with pytest.raises(TypeError):
        calculate_average(mark_one, mark_two)

import pytest
from src.grade_pass import has_passed


@pytest.mark.parametrize(
    "score, expected",
    [
        (0, False),  # Lowest score allowed
        (100, True),  # Highest score allowed
    ],
)
def test_score_boundary_valid(score, expected):
    # Act
    result = has_passed(score)
    # Assert
    assert result is expected


@pytest.mark.parametrize(
    "score, expected",
    [
        (49, False),  # Just below the pass mark
        (50, True),  # Exactly the pass mark
        (51, True),  # Just above the pass mark
    ],
)
def test_score_pass_mark_boundary_valid(score, expected):
    # Act
    result = has_passed(score)
    # Assert
    assert result is expected


@pytest.mark.parametrize(
    "score",
    [
        -1,  # Below 0
        101,  # Above 100
    ],
)
def test_score_boundary_invalid(score):
    # Act and Assert
    with pytest.raises(ValueError):
        has_passed(score)


@pytest.mark.parametrize(
    "score",
    [
        49.5,  # Float
        "50",  # String
        None,  # Missing score
        True,  # Boolean
    ],
)
def test_score_type_invalid(score):
    # Act and Assert
    with pytest.raises(TypeError):
        has_passed(score)

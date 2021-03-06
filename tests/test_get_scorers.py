import pytest
from game_of_greed.game_logic import Game_logic

# pytestmark = [pytest.mark.version_3]


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (tuple(), tuple()),
        ((1,), (1,)),
        ((1, 2), (1,)),
        ((1, 2, 3), (1,)),
        ((1, 2, 3, 5), (1, 5)),
        ((5, 1, 2, 3), (1, 5)),
        ((2, 3, 4), tuple()),
    ],
)
def test_get_scorers(test_input, expected):
    actual = Game_logic.get_scorers(test_input)
    assert sorted(actual) == sorted(expected)
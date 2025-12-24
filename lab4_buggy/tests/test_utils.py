import pytest

from src import utils


def test_parse_numbers_with_commas():
    assert utils.parse_numbers("1, 2,3") == [1.0, 2.0, 3.0]


def test_parse_numbers_with_whitespace():
    assert utils.parse_numbers("4 5 6") == [4.0, 5.0, 6.0]


def test_parse_numbers_invalid():
    with pytest.raises(ValueError, match="Некорректное число"):
        utils.parse_numbers("1 two 3")


def test_mean():
    assert utils.mean([1, 2, 3]) == 2


def test_median_even():
    assert utils.median([1, 2, 3, 4]) == 2.5


def test_median_odd():
    assert utils.median([3, 1, 2]) == 2


def test_normalize():
    assert utils.normalize([1, 2, 3]) == [0.0, 0.5, 1.0]


def test_normalize_flat():
    assert utils.normalize([5, 5, 5]) == [0.0, 0.0, 0.0]


def test_format_report():
    report = utils.format_report([1, 2, 3], include_normalized=True)
    assert "Отчет по статистике" in report
    assert "Количество: 3" in report
    assert "Минимум: 1" in report
    assert "Максимум: 3" in report
    assert "Среднее: 2.0000" in report
    assert "Медиана: 2.0000" in report
    assert "Нормализованные: 0.0000,0.5000,1.0000" in report

from spinners.codepage import get_codepage


def test_codepage():
    assert isinstance(get_codepage(), str)


def test_mock(mocker):
    mocker.patch("re.search", return_value=None)

    cp = "cpXXX"

    assert get_codepage(default=cp) == cp

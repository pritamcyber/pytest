import test
import API_module
import pytest

import unittest.mock as mock


# @mock.patch("API_module.url")


@pytest.fixture
def test_request():
    return API_module.url_response()

@pytest.mark.parametrize("id, result",[(str(6),'Tracey'),(1,'George'),(2,"Janet"),(3,"Emma"),(4,"Eve")])
def test_value_checker(id,result):
    # test_request()
    # assert API_module.url_response(id) == 200
    result = test_request
    assert result == 200
    assert str(API_module.User_response(id)["first_name"]) == result











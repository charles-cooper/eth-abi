import pytest

from eth_abi import (
    is_encodable_type,
)
from tests.common.unit import (
    CORRECT_SINGLE_ENCODINGS,
)


@pytest.mark.parametrize(
    'type_str,_python_value,_1,_2,_3',
    CORRECT_SINGLE_ENCODINGS,
)
def test_is_encodable_type_returns_true(type_str, _python_value, _1, _2, _3):
    assert is_encodable_type(type_str)


def test_is_encodable_type_returns_false():
    assert not is_encodable_type('foo')

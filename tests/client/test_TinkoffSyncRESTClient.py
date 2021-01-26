import pytest

from tinkoff_investing_api import TinkoffSyncRESTClient


def test_client_have_property_token():
    client = TinkoffSyncRESTClient(token='<TOKEN>')
    assert hasattr(client, 'token')


def test_client_property_token_return_str():
    client = TinkoffSyncRESTClient(token='<TOKEN>')
    assert isinstance(client.token, str)


def test_client_property_token_equal_input_argument():
    input_token = '<TOKEN>'
    client = TinkoffSyncRESTClient(token=input_token)
    assert client.token == input_token


def test_client_property_token_is_first_constructor_param():
    input_token = '<TOKEN>'
    client = TinkoffSyncRESTClient(input_token)
    assert client.token == input_token


def test_client_property_token_cannot_be_changed():
    client = TinkoffSyncRESTClient(token='<TOKEN>')
    with pytest.raises(AttributeError):
        client.token = '<NEW_TOKEN>'

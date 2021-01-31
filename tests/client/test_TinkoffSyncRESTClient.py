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


def test_client_have_property_is_sandbox():
    client = TinkoffSyncRESTClient(token='<TOKEN>')
    assert hasattr(client, 'is_sandbox')


def test_client_property_is_sandbox_return_bool():
    client = TinkoffSyncRESTClient(token='<TOKEN>')
    assert isinstance(client.is_sandbox, bool)


def test_client_property_is_sandbox_cannot_be_changed():
    client = TinkoffSyncRESTClient(token='<TOKEN>')
    with pytest.raises(AttributeError):
        client.is_sandbox = False


def test_client_property_is_sandbox_default_false():
    client = TinkoffSyncRESTClient(token='<TOKEN>')
    assert client.is_sandbox is False


def test_client_property_is_sandbox_can_be_set_in_constructor():
    set_value = True
    client = TinkoffSyncRESTClient(token='<TOKEN>', is_sandbox=set_value)
    assert client.is_sandbox == set_value

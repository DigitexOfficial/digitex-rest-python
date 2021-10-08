from dgtx.client import Client

client = Client(
    api_client=Client.testnet,
    api_key='PUT-YOUR-TRADING-TOKEN-HERE'
)


def test_get_order_status():
    assert client.get_order_status(
        client_id='7fce7478-a241-4b0d-bca3-2948d0f7ce2e'
    )[0].client_id == '7fce7478-a241-4b0d-bca3-2948d0f7ce2e'

from dgtx.public import PublicApiClient
from dgtx.private import PrivateApiClient
from dgtx.digitex_rest_core import Configuration
from dgtx.digitex_rest_core import ApiClient

import logging

logger = logging.getLogger(__name__)


class Client(PublicApiClient, PrivateApiClient):
    """
    Trading client of Digitex
    """

    testnet: str = "https://testnet.digitexfutures.com/dapi"
    mainnet: str = "https://digitex.io/dapi"

    def __init__(self, api_key=None, api_client=None):

        # init configuration
        configuration = Configuration()
        if api_key is not None:
            configuration.api_key['TradersToken'] = api_key
            configuration.api_key_prefix['TradersToken'] = 'Token'
        if api_client is None:
            logger.warning("You did not supply any api_client, will default to TESTNET")
            configuration.host = self.testnet
        else:
            configuration.host = api_client

        # init client with configuration
        self.client = ApiClient(configuration)

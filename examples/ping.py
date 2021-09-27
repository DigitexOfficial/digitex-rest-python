# add dgtx to path
import sys
sys.path.append('../.')

from dgtx.client import Client
from dgtx.digitex_rest_core import ApiException

client = Client(
    api_client=Client.testnet,
    api_key='PUT-YOUR-API-TOKEN-HERE'
)

# client either returns a data class or ApiException instance
# error code can be found in ApiException.status
# more detailed error description is in ApiException.reason

# ping the exchange
ping = client.ping()
print(ping)

# return instance in most of the cases is a python class
# which allows to access its properties directly
if not isinstance(ping, ApiException):
    print(f"Current server time in nanoseconds is {ping.timestamp}")
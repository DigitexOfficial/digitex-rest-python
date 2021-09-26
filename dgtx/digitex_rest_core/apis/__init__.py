
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.exchange_meta_data_api import ExchangeMetaDataApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from dgtx.digitex_rest_core.api.exchange_meta_data_api import ExchangeMetaDataApi
from dgtx.digitex_rest_core.api.private_api import PrivateApi
from dgtx.digitex_rest_core.api.public_api import PublicApi

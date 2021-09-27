Getting Started
================


API Description
---------------

API description can be found `here <https://digitexofficial.github.io/rest-api-docs/>`_

Installation
------------

Current version of REST client is in test mode only, therefore it is available as github repository only at the moment.

**Option 1. Install from git directly**

.. code:: python

    pip install git@github.com:DigitexOfficial/digitex-rest-python.git@master


**Option 2. Clone repository to the folder of your choice and then install locally. This could be a better choice for users that want to try files in the example folder**

.. code:: python

    git clone git@github.com:DigitexOfficial/digitex-rest-python.git@master


Then install Digitex client into your current project folder/virtual environment

.. code:: python

    pip install path/to/Digitex/Client



Register at Digitex
-------------------
In order to start, one has to register either at https://testnet.digitexfutures.com for testnet (virtual funds trading) or at https://digitex.io - our mainnet (real money trading).

After registration you need to obtain your trading token in your account.

Direct links to the account page:

- testnet - https://testnet.digitexfutures.com/profile/account
- mainet - https://digitex.io/trade/profile/account

If you have already created your token, you can simply copy it, else click on "Create" in the API section of your account.

**IMPORTANT NOTES!**

    - All of the data which is expected to be float or decimal are passed as strings in the API. Data is converted into Decimal format on the client level
    - All timestamps are in nanoseconds UTC

Enums, such as order types, status etc can be found in Exchange Meta Data group of endpoints in the API
or in the `Get Exchange Info <public.html#dgtx.public.PublicApiClient.get_exchange_info>`_ method of this client


Initialise the client
---------------------

.. code:: python

    from dgtx.client import Client
    client = Client(Client.testnet, api_ket = 'YOUR_TRADING_API_KET')



Basic Usage
-----------------

After you initialised the clien you can simply call one of the methods with arguments,
if they are available:


.. code:: python

    ping_response = client.ping()
    print(ping_response)


This prints human readable representation of the method call:

.. code-block:: json

    {
        "message":"pong",
        "timestamp": 1632567734971007 // in nanoseconds
    }


Unless stated otherwise and in most of the cases, the method output is either a list of data models
or a data model. This will allow you to call data model properties directly without the need
to convert json to e.g. dictionary and allows you to use dot-notation when calling the arguments.


.. code:: python

    print(ping_response.timestamp)





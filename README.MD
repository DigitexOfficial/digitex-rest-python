Digitex REST python client
----------------

**Getting Started**


[API description can be found here](https://digitexofficial.github.io/rest-api-docs/)

Example folder contains some usage examples for each method

**Installation**

Current version of REST client is in test mode only,
therefore it is available as github repository only
at the moment.

***Option 1.*** Install from git directly
```
pip install git+https://github.com/DigitexOfficial/digitex-rest-python.git@master
# or if for some reason you want to use dev version
pip install git+https://github.com/DigitexOfficial/digitex-rest-python.git@development
```
***Option 2.*** Clone repository to the folder of your choice and then install locally.
This could be a better choice for users that want to try files in the
example folder

```
git clone git@github.com:DigitexOfficial/digitex-rest-python.git@master
```

Then install Digitex client into your current project folder/virtual
environment.

```
pip install path/to/Digitex/Client
```

**Basic Usage**

Init the client:
```
from dgtx.client import Client

client = Client(
    api_client=Client.testnet, # or Client.mainnet
    api_key='PUT-YOUR-API-TOKEN-HERE'
)

client.ping()

```

**Register at Digitex**

In order to start, one has to register either at
[https://testnet.digitexfutures.com](https://testnet.digitexfutures.com)
for testnet (virtual funds trading) or at 
[https://digitex.io](https://digitex.io) - our mainnet (real money trading).

After registration you need to obtain your trading token in your account.

Direct links to the account page:

- testnet - https://testnet.digitexfutures.com/profile/account
- mainet - https://digitex.io/trade/profile/account

If you have already created your token, you can simply copy it, else click on "Create" in the API section of your account.

**IMPORTANT NOTES!**

1. All of the data which is expected to be float or decimal are passed as strings in the API. Data is converted into Decimal format on the client level 
   
2. All timestamps are in microseconds UTC

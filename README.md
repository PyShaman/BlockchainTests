# Blockchain Tests 
_User guide_
###### Author: Michał Bek
###### Email: michal.bek@gmail.com


**List of contents**

**1. Python version and installation**

**2. Installing required packages and tools**

**3. Usage**


_1. Python version and installation_

Tests are written in Python 3.5+ and it should be ran on this version or higher.
User can download newest version of Python at [Python download site](https://www.python.org/downloads/).

Install [PIP](https://pypi.org/project/pip/).

_2. Installing required packages and tools_

After cloning [Blockchain Tests](https://github.com/PyShaman/BlockchainTests.git) repository locally user should enter 
BlockchainTests folder and install required packages using following command:

```
$ pip3 install -r requirements.txt
```

This will automatically download and install following packages: 
[requests](http://docs.python-requests.org/en/master/) and [behave](https://github.com/behave/behave).

After downloading and installing node.js and npm you need to:
```
$ npm install -g blockchain-wallet-service
```
and then start wallet service:
```
$ blockchain-wallet-service start --port 3000
```
Note that blockchain-wallet-service is designed to be run locally on the same machine as your application and 
therefore will only accept connections from localhost. If you modify this service to accept external connections, 
be sure to add the appropriate firewall rules to prevent unauthorized use.

An API code is required for wallet creation and higher request limits. For basic usage, no API code is required.

After this user can run tests by typing in console:
```
$ behave
```
The result of the tests will be shown in console.
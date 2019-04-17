# BlockchainTests


download and install node.js and npm from https://nodejs.org/en/#download for windows

for linux: https://github.com/nodejs/help/wiki/Installation

for MacOS: 

After downloading and installing node.js and npm you need to:
```
$ npm install -g blockchain-wallet-service
```
and then start wallet service:
```
$ blockchain-wallet-service start --port 3000
```
Note that blockchain-wallet-service is designed to be run locally on the same machine as your application and therefore will only accept connections from localhost. If you modify this service to accept external connections, be sure to add the appropriate firewall rules to prevent unauthorized use.

An API code is required for wallet creation and higher request limits. For basic usage, no API code is required.

After this user can run tests
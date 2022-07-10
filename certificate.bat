cd .\EasyRSA-3.1.0\
.\EasyRSA-Start.bat
./easyrsa init-pki
./easyrsa build-ca nopass
./easyrsa build-server-full server nopass
./easyrsa build-client-full client1.domain.tld nopass
exit
mkdir ../certificate
copy pki\ca.crt ../certificate
copy pki\issued\server.crt ../certificate
copy pki\private\server.key ../certificate
copy pki\issued\client1.domain.tld.crt ../certificate
copy pki\private\client1.domain.tld.key ../certificate
cd ../certificate
aws acm import-certificate --certificate fileb://server.crt --private-key fileb://server.key --certificate-chain fileb://ca.crt

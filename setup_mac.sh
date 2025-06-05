echo "Current directory: "
pwd
mkdir regtest_data
wget https://bitcoincore.org/bin/bitcoin-core-29.0/bitcoin-29.0-arm64-apple-darwin-unsigned.tar.gz 
tar -xvf bitcoin-29.0-arm64-apple-darwin-unsigned.tar.gz
rm bitcoin-29.0-arm64-apple-darwin-unsigned.tar.gz
python3 -m venv simulation
source simulation/bin/activate
pip install jupyter

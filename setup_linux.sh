echo "Current directory: "
pwd
mkdir regtest_data
wget https://bitcoincore.org/bin/bitcoin-core-29.0/bitcoin-29.0-x86_64-linux-gnu.tar.gz
tar -xvf bitcoin-29.0-x86_64-linux-gnu.tar.gz
rm bitcoin-29.0-x86_64-linux-gnu.tar.gz
python3 -m venv simulation
source simulation/bin/activate
pip install jupyter

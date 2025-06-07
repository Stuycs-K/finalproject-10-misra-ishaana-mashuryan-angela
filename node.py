from io import StringIO
import os
import subprocess
import sys
import time

NODE_NUMBER = 0
BASE_DATADIR = os.getcwd() + "/regtest_data/"
EXEC_DIR = "bitcoin-29.0/bin"

class Node():
    def __init__(self, name):
        global NODE_NUMBER
        self.name = name
        self.num = NODE_NUMBER
        self.port = 18444+(self.num*2)
        self.rpcport = 8333+self.num
        self.datadir = BASE_DATADIR + f"{self.num}"
        try:
            os.system(f"mkdir {self.datadir}")
        except Exception:
            print("file exists")
        os.system(f"./{EXEC_DIR}/bitcoind -regtest -datadir={self.datadir} -port={self.port} -rpcport={self.rpcport} -rpcuser={self.name} -rpcpassword={self.num} -fallbackfee=0.0002 -daemon")

        NODE_NUMBER += 1

    def connect(self, port):
        os.system(f"./{EXEC_DIR}/bitcoin-cli -datadir={self.datadir} -rpcport={self.rpcport} -rpcuser={self.name} -rpcpassword={self.num} addnode \"127.0.0.1:{port}\" \"onetry\"")

    def get_nodes(self):
        os.system(f"./{EXEC_DIR}/bitcoin-cli -datadir={self.datadir} -rpcport={self.rpcport} -rpcuser={self.name} -rpcpassword={self.num} getpeerinfo")

    def create_wallet(self):
        os.system(f"./{EXEC_DIR}/bitcoin-cli -datadir={self.datadir} -rpcport={self.rpcport} -rpcuser={self.name} -rpcpassword={self.num} createwallet \"{self.name}_wallet\" false false \"\" true")
        # os.system(f"./{EXEC_DIR}/bitcoin-cli -datadir={self.datadir} -rpcport={self.rpcport} -rpcuser={self.name} -rpcpassword={self.num} loadwallet \"{self.name}_wallet\"")

    def get_address(self):
        os.system(f"./{EXEC_DIR}/bitcoin-cli -datadir={self.datadir} -rpcport={self.rpcport} -rpcuser={self.name} -rpcpassword={self.num} getnewaddress")
        ret = subprocess.check_output([f"pwd"], shell=True)
        subprocess.check_output([f"./{EXEC_DIR}/bitcoin-cli -datadir={self.datadir} -rpcport={self.rpcport} -rpcuser={self.name} -rpcpassword={self.num} getbalances"], shell=True)

    def mine_block(self, address):
        os.system(f"./{EXEC_DIR}/bitcoin-cli -datadir={self.datadir} -rpcport={self.rpcport} -rpcuser={self.name} -rpcpassword={self.num} generatetoaddress 1 \"{address}\"")

    def wallet_balance(self):
        os.system(f"./{EXEC_DIR}/bitcoin-cli -datadir={self.datadir} -rpcport={self.rpcport} -rpcuser={self.name} -rpcpassword={self.num} getbalances")

    def list_addresses(self):
        os.system(f"./{EXEC_DIR}/bitcoin-cli -datadir={self.datadir} -rpcport={self.rpcport} -rpcuser={self.name} -rpcpassword={self.num} listreceivedbyaddress 0 true")

    def get_priv_key(self, address):
        os.system(f"./{EXEC_DIR}/bitcoin-cli -datadir={self.datadir} -rpcport={self.rpcport} -rpcuser={self.name} -rpcpassword={self.num} dumpprivkey {address}")

    def send(self, address, amount):
        os.system(f"./{EXEC_DIR}/bitcoin-cli -datadir={self.datadir} -rpcport={self.rpcport} -rpcuser={self.name} -rpcpassword={self.num} sendtoaddress {address} {amount}")

    # it is better to use a regular function instead of a destructor here because 
    # a destructor would get too complicated while using Jupyter
    def cleanup(self):
        print("shutting down")
        time.sleep(3)
        os.system(f"./{EXEC_DIR}/bitcoin-cli -datadir={self.datadir} -rpcport={self.rpcport} -rpcuser={self.name} -rpcpassword={self.num} stop")

"""
if __name__ == '__main__':
    alice = Node("alice")
    bob = Node("bob")
    charlie = Node("charlie")
    alice.cleanup()
    bob.cleanup()
    charlie.cleanup()
"""

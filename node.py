import os
import time

NODE_NUMBER = 0
BASE_DATADIR = os.getcwd() + "/regtest_data/"
EXEC_DIR = "bitcoin-29.0/bin"

class Node():
    def __init__(self, name):
        global NODE_NUMBER
        self.name = name
        self.num = NODE_NUMBER
        self.datadir = BASE_DATADIR + f"{self.num}"
        try:
            os.system(f"mkdir {self.datadir}")
        except Exception:
            print("file exists")
        os.system(f"./{EXEC_DIR}/bitcoind -regtest -datadir={self.datadir} -port={18444+self.num} -rpcport={19443+self.num} -rpcuser={self.name} -rpcpassword={self.num} -daemon")

        NODE_NUMBER += 1

    def __del__(self):
        print("shutting down")
        time.sleep(3)
        os.system(f"./{EXEC_DIR}/bitcoin-cli -datadir={self.datadir} -rpcport={19443+self.num} -rpcuser={self.name} -rpcpassword={self.num} stop")

if __name__ == '__main__':
    alice = Node("alice")
    bob = Node("bob")

import os

class Simulation():
    def __init__(self):
        os.system("bash setup_linux.sh")

    def __del__(self):
        os.system("bash cleanup_linux.sh")

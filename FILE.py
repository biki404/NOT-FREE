import os, sys
try:
    __import__("biki").menu()
except Exception as e:
    exit(str(e))

import os, sys
try:
    __import__("od").main()
except Exception as e:
    exit(str(e))

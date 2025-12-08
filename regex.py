# Lightweight shim that implements a subset of the 'regex' API using the stdlib re
import re

def findall(pattern, string, flags=0):
    return re.findall(pattern, string, flags=flags)

# Keep a couple of names commonly used from the regex package
compile = re.compile
search = re.search
match = re.match

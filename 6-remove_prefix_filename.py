#!/usr/bin/python3

import os

prefix = "movies"
[os.rename(file, file.replace(prefix, "")) for file in os.listdir('.') if file.startswith(prefix)]

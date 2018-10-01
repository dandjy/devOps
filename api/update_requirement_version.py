import re

requirements = open("app/setup.py").read()
version = re.search("VERSION *= *'(\d+\.\d+.\d+)'", requirements).groups()[0].split(".")
open("app/setup.py", "w").write(
    re.sub("VERSION = '\d+\.\d+.\d+'",
           "VERSION = {}.{}.{}".format(version[0], str(int(version[1]) + 1), version[2]),
           requirements)
)

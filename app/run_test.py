import os
import logging
import argparse

# get loops count
parser = argparse.ArgumentParser()
parser.add_argument("loops", help="loop count")
args = parser.parse_args()
loops = args.loops

# Logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# console logging
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# formatting
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
strtmp = ""
for x in range(int(loops)):
    strtmp = strtmp + "it gets even longer"

logger.debug("output_bytes="+ str(len(strtmp)))
logger.debug("starting test this is a log line.."+ strtmp)

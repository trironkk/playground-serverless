from __future__ import print_function

import json
import logging
import subprocess
import socket

log = logging.getLogger()
log.setLevel(logging.DEBUG)

def handler(event, context):
    log.debug("Received event {}".format(json.dumps(event)))
    command = event["command"]
    output = subprocess.check_output(command, shell=True)
    return {
        "host":socket.gethostname(),
        "command":command,
        "output":output
    }

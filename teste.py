import json
from datetime import datetime
import time


with open('log.json', 'a+') as log:
    now = datetime.now()
    time = f"{now.hour}:{now.minute}:{now.second}"
    status = {time : 1232312313}
    json.dump(status, log)
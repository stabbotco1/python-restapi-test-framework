# App level global variable setup for all shared variables
import requests
import logging
import re
import os

SESSION = requests.Session()
# APP_URL = "http://localhost:8080"
#  change to the following when running from within a docker container, per the docker docs
# APP_URL = "http://host.docker.internal:8080"

# these env variables are passed in by the docker via the make file specifying the secrets.ini file
APP_URL = os.getenv("APP_URL","")
ADMIN_USER = os.getenv("ADMIN_USER","")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD","")

LOG = logging.getLogger()

class HideSensitiveData(logging.Filter):

    def filter(self, record):
        record.msg = str(record.msg).replace(ADMIN_PASSWORD, "*******")
        record.msg = re.sub(r'Authorization.*?,','Authorization\': \'*******\', ', str(record.msg))
        return True


LOG.addFilter(HideSensitiveData())

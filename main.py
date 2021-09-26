import json
import os
from flask import Flask
from tomcatmanager import tomcat_manager

app = Flask(__name__)
tm = tomcat_manager.TomcatManager()


@app.route("/", methods=["GET"])
def home():
    return json.dumps({'Agent': 'UP'}), 200, {'ContentType': 'application/json'}


@app.route("/health", methods=["GET"])
def health():
    try:
        tm.connect(
            url=os.environ.get("TOMCAT_MGR_URL", 'http://localhost:8080/manager'),
            user='manager',
            password='password')

        for deployed_application in tm.list().result.splitlines():
            if "stopped" in deployed_application:
                raise Exception('Failed check on : %s' % deployed_application.split(':')[0])
    except Exception as error:
        app.logger.error(error)
        response = {'Server Status': 'DOWN'}
        status = 500
    else:
        response = {'Server Status': 'UP'}
        status = 200
    return json.dumps(response), status, {'ContentType': 'application/json'}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("AGENT_PORT", 8888)))

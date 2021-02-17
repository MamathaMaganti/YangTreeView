from flask import Flask, request
import re
import subprocess


app = Flask(__name__)
app.config["DEBUG"] = True
# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'your secret key'

# http://localhost:5000/pythonlogin/ - this will be the login page, we need to use both GET and POST requests
@app.route('/treeview', methods=['GET', 'POST'])
def treeview():
    cmd = "/Users/mammagan/Downloads/ibm-common.yang"
    log = open('file.txt', 'w')
    p = subprocess.Popen("pyang -f tree -p . " + cmd, stdout=subprocess.PIPE, stderr=log, encoding='utf-8', shell=True)
    out = p.communicate()[0]
    # out = out.decode("utf-8")
    print("done ", out)
    return out

app.run()
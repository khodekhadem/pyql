from flask import Flask
import os
import subprocess
def sysout( command ):
    output = subprocess.check_output( command , shell=True)
    output = output.decode("utf-8")
    print (output)
    return "hello"
sysout("mysql -e show variable")

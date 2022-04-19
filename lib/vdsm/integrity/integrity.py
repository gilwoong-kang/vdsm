import subprocess

def checkIntegrity(self):
    return subprocess.check_output(["aide","--check"])
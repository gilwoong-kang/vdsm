import subprocess


def runCmd(params):
    return subprocess.check_output(params)

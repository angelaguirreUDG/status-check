import os
import subprocess

def main():

    command = 'cd C:\\Users\\angel\\Documents\\Tolerante a fallas\\Status\\checkpointing  && npm run server'

    while True:
        
        response = os.popen(f"cd C:\\Users\\angel && tcping 127.0.0.1").read()

        if "4 successful" not in response:
            subprocess.run(["start", "/wait", "cmd", "/K", command], shell=True)

main()
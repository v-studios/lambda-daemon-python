import subprocess
import time
from urllib.request import Request, urlopen

print("Launching Server in Cold Start")
# res = subprocess.run(["python", "server.py"])  # runs in foreground, server hangs
server = subprocess.Popen(["python", "server.py"])  # run in background
print(f"Cold started server {server=} sleeping for it to start")
time.sleep(1)


def handler(event={}, context=None):
    req = Request("http://localhost:3000/")
    print(f"Request {req=}")
    res = urlopen(req)
    print(f"Handler {res=}")
    body = res.read()
    print(f"Body {len(body)=}")
    return {"statusCode": 200, "body": body}


if __name__ == "__main__":
    res = handler()
    print(res)
    server.terminate()

import json
import os

useless = open('info.json')
info = json.load(useless)

def main():
    print(f"{info["name"]}, {info["version"]}")
    info["name"] = "Forgor"
    print(f"{info["name"]}, {info["version"]}")
    useless = json.dumps(info)
    print(useless)
    json.dump(useless, "info.json")
main()
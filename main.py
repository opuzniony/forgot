#!/usr/bin/env python3

import os
import sys
import json

home_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(home_dir, 'info.json'), 'r') as file:
    info = json.load(file)

args = sys.argv[1:]

match args:
    case ["v"]:
        print(f"{info['name']} {info['version']}")

    case ["save", string_name, *string]:

        #directory cant be different if terminal is ran from somewhere else
        data_path = os.path.join(home_dir, "data.json")

        #see if it exists and take it
        if os.path.exists(data_path):
            with open(data_path, "r") as file:
                data = json.load(file)

        #fallback if theres nothing
        else:
            data = {"commands": {}}

        #add tge stuff
        data["commands"][string_name] = string

        #write to the file with the stuff
        with open(data_path, "w") as file:
                json.dump(data, file, indent=4)

        #confirm it so the user doesnt panick
        print(f"Saved command as {string_name}")

    case ["rm", string_name]:
        #same as above it has to read them to edit anything
        data_path = os.path.join(home_dir, "data.json")
        with open(data_path, "r") as file:
                data = json.load(file)

        #check if its there and delete if yes
        if string_name in data["commands"]:
            del data["commands"][string_name]

            with open(data_path, "w") as file:
                json.dump(data, file, indent=4)

            print(f"Deleted {string_name}")
        else:
            print(f"{string_name} does not exist.")
    
    case ["list"]:
        data_path = os.path.join(home_dir, "data.json")
        with open(data_path, "r") as file:
                data = json.load(file)
        
        for name in data["commands"]:
            print(name)
    case ["run", string_name]:
        data_path = os.path.join(home_dir, "data.json")
        with open(data_path, "r") as file:
                data = json.load(file)
        
        command = " ".join(data["commands"][string_name])
        os.system(command)
    case _:
        print("Unknown command")
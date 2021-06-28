import yaml
import os

if not os.path.isfile("config.yaml"):
    print("Terminating... No configuration found")
    exit()

with open("config.yaml", "r") as config_file:
    config = yaml.load(config_file, Loader=yaml.FullLoader)

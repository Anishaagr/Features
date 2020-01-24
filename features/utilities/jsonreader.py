import json
import os

BASE_PATH = "C:\\Users\\anisha.agarwal\\PycharmProjects\\cortex\\features\\"
country_file = os.path.join(BASE_PATH, "data\\country.json")


def read_json():
    with open(country_file) as file:
        return json.load(file)
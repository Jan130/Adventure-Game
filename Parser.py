import yaml

def get_config(filename):
    stream = open(filename, "r")
    return yaml.load(stream)

def get_health(filename, job):
    input = get_config(filename)
    return input["Jobs"][job]["Health"]

def get_weapon_name(filename, job, level):
    input = get_config(filename)
    return input["Jobs"][job]["Weapons"][level]["name"]

def get_weapon_damage(filename, job, level):
    input = get_config(filename)
    return input["Jobs"][job]["Weapons"][level]["damage"]

def get_screen_width(filename):
    input = get_config(filename)
    return input["Screen"]["Width"]

def get_screen_height(filename):
    input = get_config(filename)
    return input["Screen"]["Height"]

def get_keys(filename):
    input = get_config(filename)
    for key in input["Keys"]:
        input["Keys"][key] = "K_" + input["Keys"][key]
    return input["Keys"]

def get_range(filename, job):
    input = get_config(filename)
    return input["Jobs"][job]["Range"]

import yaml

def get_config(filename):
    stream = open(filename, "r")
    return yaml.load(stream)

def get_health(filename, job):
    input = get_config(filename)
    return input[job]["Health"]

def get_weapon_name(filename, job, level):
    input = get_config(filename)
    return input[job]["Weapons"][level]["name"]

def get_weapon_damage(filename, job, level):
    input = get_config(filename)
    return input[job]["Weapons"][level]["damage"]

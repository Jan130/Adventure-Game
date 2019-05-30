import yaml

def get_config(filename):
    stream = open(filename, "r")
    return yaml.load(stream)

def get_health(filename, job):
    input = get_config(filename)
    return input[job]["Health"]

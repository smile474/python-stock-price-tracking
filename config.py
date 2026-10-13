import yaml

def load_config():
    config = {}
    with open("config/config.yaml") as f:
        config = yaml.safe_load(f)
        try:
            webhook_url = config["discord"]["webhook_url"]
        except:
            webhook_url = ""
        config['webhook_url'] = webhook_url
    return config

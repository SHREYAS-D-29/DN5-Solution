import configparser
class Config: pass
class DatabaseConfig(Config): pass
cfg=configparser.ConfigParser(); cfg.read('db.ini')
print(dict(cfg['DATABASE']))

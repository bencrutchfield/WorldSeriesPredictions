import logging
import pymysql
import json
import config
from flask_cors import CORS

x = pymysql.connect(host=config._DB_CONF['host'], 
                           port=config._DB_CONF['port'], 
                           user=config._DB_CONF['user'], 
                           passwd=config._DB_CONF['passwd'], 
                           db=config._DB_CONF['db'])
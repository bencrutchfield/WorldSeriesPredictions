import logging
from flask import Flask, request, render_template
import datetime
import decimal
import pymysql
import json
import config
from flask_cors import CORS
import sql
from flask import render_template_string

x = pymysql.connect(host=config._DB_CONF['host'], 
                           port=config._DB_CONF['port'], 
                           user=config._DB_CONF['user'], 
                           passwd=config._DB_CONF['passwd'], 
                           db=config._DB_CONF['db'])


def type_handler(x):
    if isinstance(x, datetime.datetime):
        return x.isoformat()
    if isinstance(x, decimal.Decimal):
        return '$%.2f'%(x)
    raise TypeError("Unknown type")

def rows_to_json(cols,rows):
    result = []
    for row in rows:
        data = dict(zip(cols, row))
        result.append(data)
    return json.dumps(result, default=type_handler)


def player_16():
    conn = x
    cur = conn.cursor()
    sql="SELECT * FROM player_stats_2016_season;"
    cur.execute(sql)
    # get all column names
    columns = [desc[0] for desc in cur.description]
    # get all data
    rows=cur.fetchall()
    # build json 
    result = rows_to_json(columns,rows)
    #print(result)
    cur.close()
    conn.close()
    return result

def player_17():
    conn = x
    cur = conn.cursor()
    sql="SELECT * FROM player_stats_2017_season;"
    cur.execute(sql)
    columns = [desc[0] for desc in cur.description]
    rows=cur.fetchall()
    result = rows_to_json(columns,rows)
    cur.close()
    conn.close()
    return result

def player_18():
    conn = x
    cur = conn.cursor()
    sql="SELECT * FROM player_stats_2018_season;"
    cur.execute(sql)
    columns = [desc[0] for desc in cur.description]
    rows=cur.fetchall()
    result = rows_to_json(columns,rows)
    cur.close()
    conn.close()
    return result

def sep():
    conn = x
    cur = conn.cursor()
    sql="SELECT * FROM sep_2018_full_stats;"
    cur.execute(sql)
    columns = [desc[0] for desc in cur.description]
    rows=cur.fetchall()
    result = rows_to_json(columns,rows)
    cur.close()
    conn.close()
    return result


    
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 13:04:17 2020

@author: nickf
"""
import sqlite3
import csv

OSM_DB = "austin_osm.db"

def load_db():
    #connect to db
    cnn = sqlite3.connect(OSM_DB)
    cur = cnn.cursor()    
    #populate nodes
    with open('nodes.csv','rt', encoding='utf-8') as fin:
        dr = csv.DictReader(fin) 
        row_vals = [(i['id'], i['lat'], i['lon'], i['user'], i['uid'], i['version'], i['changeset'], i['timestamp']) \
                 for i in dr]
    cur.executemany("insert into nodes (id, lat, lon, user, uid, version, changeset, timestamp) \
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?);", row_vals)
    cnn.commit()

    #populate nodes_tags
    with open('nodes_tags.csv','rt', encoding='utf-8') as fin:
        dr = csv.DictReader(fin) 
        row_vals = [(i['id'], i['key'], i['value'], i['type']) for i in dr]
    cur.executemany("insert into nodes_tags (id, key, value, type) VALUES (?, ?, ?, ?);", row_vals)
    cnn.commit()

    #populate ways
    with open('ways.csv','rt', encoding='utf-8') as fin:
        dr = csv.DictReader(fin) 
        row_vals = [(i['id'], i['user'], i['uid'], i['version'], i['changeset'], i['timestamp']) for i in dr]    
    cur.executemany("insert into ways (id, user, uid, version, changeset, timestamp) VALUES (?, ?, ?, ?, ?, ?);", row_vals)
    cnn.commit()    

    #populate ways_nodes
    with open('ways_nodes.csv','rt', encoding='utf-8') as fin:
        dr = csv.DictReader(fin) 
        row_vals = [(i['id'], i['node_id'], i['position']) for i in dr]    
    cur.executemany("insert into ways_nodes (id, node_id, position) VALUES (?, ?, ?);", row_vals)
    cnn.commit()
    
    #populate ways_tags
    with open('ways_tags.csv','rt', encoding='utf-8') as fin:
        dr = csv.DictReader(fin) 
        row_vals = [(i['id'], i['key'], i['value'], i['type']) for i in dr]    
    cur.executemany("insert into ways_tags (id, key, value, type) VALUES (?, ?, ?, ?);", row_vals)
    cnn.commit()
    
def create_db():
    #connect to db
    cnn = sqlite3.connect(OSM_DB)
    cur = cnn.cursor()
    
    #create db schema
    cur.execute('drop table if exists nodes;')
    cur.execute('drop table if exists nodes_tags;')
    cur.execute('drop table if exists ways;')
    cur.execute('drop table if exists ways_tags;')
    cur.execute('drop table if exists ways_nodes;')
    cur.execute('create table nodes (id integer, lat float, lon float, user string, uid integer, version string, changeset integer, timestamp string);')
    cur.execute('create table nodes_tags (id integer, key string, value string, type string);')
    cur.execute('create table ways (id integer, user string, uid integer, version string, changeset integer, timestamp string);')
    cur.execute('create table ways_tags (id integer, key string, value string, type string);')
    cur.execute('create table ways_nodes (id integer, node_id integer, position integer);')
    
    #close db
    cur.close
    cnn.close 
    
if __name__ == '__main__':
    create_db()
    load_db()
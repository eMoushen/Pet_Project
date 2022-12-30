#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import sqlite3

con = sqlite3.connect('example.db')
cur = con.cursor()
cur.execute('''CREATE TABLE users (id VARCHAR(255), lang VARCHAR(255))''')

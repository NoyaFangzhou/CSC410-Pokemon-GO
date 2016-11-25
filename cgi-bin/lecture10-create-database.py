#!/usr/bin/env python

import sqlite3
import hashlib
import datetime


def create_database():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute('DROP TABLE IF EXISTS users')

    cursor.execute('CREATE TABLE IF NOT EXISTS users(username varchar(30) primary key, password varchar(200), salt charchar(100))')

    conn.commit()
    conn.close()


def insert_user(username, password):
    salt = str(datetime.datetime.now())

    hasher = hashlib.md5()
    hasher.update(password)
    hasher.update(salt)
    encrypted = hasher.hexdigest()

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users VALUES(?,?,?);", [username, encrypted, salt])

    conn.commit()
    conn.close()


def print_users():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    for row in cursor.execute('SELECT * FROM users'):
        print row


def init_database():
    create_database()
    insert_user('bobby', 'a great password')
    insert_user('buttercup', 'woof!')
    print_users()


init_database()

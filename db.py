import sqlite3
import os
import csv

def create(dbname):
    conn = sqlite3.connect(dbname)
    curs = conn.cursor()

    lodging = """CREATE TABLE Lodging (lodgingID VARCHAR(50) primary key, Name VARCHAR(100), Address VARCHAR(100), PhoneNumber INT, StarRating INT(1), Price DECIMAL)"""
    restaurant = """CREATE TABLE Restaurant (restaurantID VARCHAR(50) primary key, Name VARCHAR(100), Address VARCHAR(100), PhoneNumber INT, Price DECIMAL)"""
    entertainment = """CREATE TABLE Entertainment (entertainmentID varchar(50) primary key, Name varchar(50), Address varchar(100), PhoneNumber INT, Rating int, url varchar(100))"""
    tags = """CREATE TABLE Tags (lodgingID varchar(50), restaurantID varchar(50), entertainmentID varchar(50), tags varchar(50))"""

    curs.execute(lodging)
    curs.execute(restaurant)
    curs.execute(entertainment)
    curs.execute(tags)

    conn.commit()
    conn.close()

def parseLodging(dbname):
    conn = sqlite3.connect(dbname)
    curr = conn.cursor()

    abspath = os.path.abspath('resources/lodging.csv')
    with open(abspath, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == 'Lodging ID':
                continue
            _id, name, address, number, rating, price = row[0], row[1], row[2], int(row[3].replace("-", "")), row[4], row[5]
            tag = row[6:9]
            lodging = """INSERT INTO Lodging values (?, ?, ?, ?, ?, ?)"""
            tags = """insert into Tags values (?, NULL, NULL, ?)"""
            curr.execute(lodging, (_id, name, address, number, rating, price))
            for i in tag:
                curr.execute(tags, (_id, i))

    conn.commit()
    conn.close()
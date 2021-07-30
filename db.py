#!/usr/bin/env python3

import sqlite3
import os
import csv

def create(dbname):
    conn = sqlite3.connect(dbname)
    curs = conn.cursor()

    lodging = """CREATE TABLE Lodging (lodgingID VARCHAR(50) primary key, Name VARCHAR(100), Address VARCHAR(100), PhoneNumber INT, StarRating INT(1), Price DECIMAL)"""
    restaurant = """CREATE TABLE Restaurant (restaurantID VARCHAR(50) primary key, Name VARCHAR(100), Address VARCHAR(100), PhoneNumber INT, Price DECIMAL)"""
    entertainment = """CREATE TABLE Entertainment (entertainmentID VARCHAR(50), Description VARCHAR(50), Includes VARCHAR(50), Contact VARCHAR(50), StreetAddress VARCHAR(50),City VARCHAR(50),State VARCHAR(2), Zip VARCHAR(5), PricePerPerson INT, PriceTotal INT, PhoneNumber VARCHAR(12), GoogleRating INT, URL varchar(100), OpeningTime varchar(20),ClosingTime varchar(20),Morning boolean,Afternoon boolean,Evening boolean,ChildFriendly boolean)"""
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

def parseEnt(dbname):
    conn = sqlite3.connect(dbname)
    curr = conn.cursor()

    abspath = os.path.abspath('resources/ent.csv')
    with open(abspath, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == 'Entertainment ID':
                continue
            ent = row[:-5]

            tag = row[-5:]
            for i in range(len(ent)):
                if (ent[i] == "N/A" or ent[i] == "" or ent[i] == " "):
                    ent[i] = "NULL"
            # ent = ["NULL" for i in ent if (i == "N/A" or i == "" or i == " ")]
            # print(ent)
            entertainment = """INSERT INTO Entertainment values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
            # lodging = """INSERT INTO Lodging values (?, ?, ?, ?, ?, ?)"""
            tags = """insert into Tags values (NULL, NULL, ?, ?)"""
            curr.execute(entertainment, ent)
            for i in tag:
                curr.execute(tags, (row[0], i))

    conn.commit()
    conn.close()

# def parseRest(dbname):
#     conn = sqlite3.connect(dbname)
#     curr = conn.cursor()
#
#     abspath = os.path.abspath('resources/lodging.csv')
#     with open(abspath, newline='') as csvfile:
#         reader = csv.reader(csvfile)
#         for row in reader:
#             if row[0] == 'Lodging ID':
#                 continue
#             _id, name, address, number, rating, price = row[0], row[1], row[2], int(row[3].replace("-", "")), row[4], row[5]
#             tag = row[6:9]
#             lodging = """INSERT INTO Lodging values (?, ?, ?, ?, ?, ?)"""
#             tags = """insert into Tags values (NULL, ?, NULL, ?)"""
#             curr.execute(lodging, (_id, name, address, number, rating, price))
#             for i in tag:
#                 curr.execute(tags, (_id, i))
#
#     conn.commit()
#     conn.close()

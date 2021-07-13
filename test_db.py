import unittest
import db
import os
import sqlite3

class DBTestCase(unittest.TestCase):

    def setUp(self):
        db.create('test.db')
        db.parseLodging('test.db')
        # print("g")
        self.conn = sqlite3.connect('test.db')
        self.cur = self.conn.cursor()

    def tearDown(self):

        self.cur.execute('''DROP TABLE Lodging''')
        self.cur.execute('''DROP TABLE Restaurant''')
        self.cur.execute('''DROP TABLE Entertainment''')
        self.cur.execute('''DROP TABLE Tags''')
        self.conn.commit()
        self.conn.close()
        os.remove('test.db')

    def test_category(self):   #, 

        self.cur.execute("select Lodging.lodgingID, name, address, tags from Lodging join Tags on Lodging.lodgingID = Tags.lodgingID")
        rows = self.cur.fetchall()
        for i in rows:
            print(i)

# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
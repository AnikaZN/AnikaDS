from SQL_test import cursor
import os
import sqlite3
import pandas as pd

conn = sqlite3.connect(r'C:\Users\anika\Desktop\AnikaDS\Study_Ahead\SQL\demo.db')
cursor = conn.cursor()
#cursor.execute("CREATE TABLE NUMBERS([A] text, [B] integer, [C] integer)")
list = [('g', 3, 0), ('l', 1, 9), ('r', 6, 13)]

# cursor.executemany("INSERT INTO NUMBERS VALUES (?, ?, ?)", list)
# conn.commit()

'''Count how many rows you have'''
q1 = cursor.execute("SELECT COUNT(*) FROM NUMBERS").fetchall()

'''How many rows are there where both B and C are at least 5?'''
q2 = cursor.execute("SELECT COUNT(*) FROM NUMBERS WHERE B >= 5 AND C >= 5").fetchall()

'''How many unique values of B are there?'''
q3 = cursor.execute("SELECT DISTINCT B FROM NUMBERS").fetchall()

if __name__ == '__main__':
    print(q1, q2, q3)


#make notes on the process
#make a function that makes pretty results

import csv
import sqlite3


# conn = sqlite3.connect("db.sqlite3")
#
# cur = conn.cursor()
#
# example_csv = open('example_batch_records.csv')
#
# rows = csv.reader(example_csv)
#
# cur.execute("CREATE TABLE batch_jobs (batch_number varchar(255), submitted_at varchar(255), nodes_used varchar(255))")
#
# with open("example_batch_records.csv") as infile:
#     for row in infile:
#         cur.execute("INSERT INTO batch_jobs VALUES (?, ?, ?)", row.split(","))
#         conn.commit()
#
#
#
# cur.execute("SELECT * FROM batch_jobs LIMIT 3")
#
#
# print(cur.fetchall())

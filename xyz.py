import pymysql.cursors
import myconnutils

# Connect to the database
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             port = 3388,
                             password='159753',
                             db='python',
                             charset='utf8mb4',
                             )

connection = myconnutils.getConnection()

print("Connect successful!")

sql = "Select adie from Employee"

try:
    cursor = connection.cursor()

    # Execute sql, and pass 1 parameter.
    cursor.execute(sql, (10))


    print()

    for row in cursor:
        print(" ----------- ")
        print("Row: ", row)


finally:
    # Close connection.
    connection.close()

from mysql.connector import connect

connection = connect(
    host="localhost",
    user="root",
    password="", #sesuaikan dengan password database kalian
    database="kampus"
)
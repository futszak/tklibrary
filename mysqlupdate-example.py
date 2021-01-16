from tklibrary import mysqlupdate

q="CREATE TABLE tablica (task_id INT AUTO_INCREMENT PRIMARY KEY,title VARCHAR(255) NOT NULL)"
print(mysqlupdate(q))
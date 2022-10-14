import sqlite3
import customer as cust

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        
    def fetch(self, table, id, alt_lookup):
        if table == "Customers":
            if id != "":
                self.cur.execute("SELECT * FROM Customers where cust_id = ?", id)
            else:
                self.cur.execute("SELECT * FROM Customers where cust_phone = ?", (alt_lookup,))
        rows = self.cur.fetchone()
        return rows        

    def insert(self, data):
        if isinstance(data, cust.Customer):
            self.cur.execute("INSERT INTO Customers VALUES (NULL, ?, ?, ?, ?)", (data.name, data.phone, data.addr, data.dist))
        self.conn.commit()

    def remove(self, data):
        if isinstance(data, cust.Customer):
            self.cur.execute("DELETE FROM Customers WHERE cust_id = ?", (data.id))
        self.conn.commit()

    def update(self, id, furniture, customer, employee, price):
        self.cur.execute("UPDATE furniture SET furniture = ?, customer = ?, retailer = ?, price = ? WHERE id = ?",
                         (furniture, customer, employee, price, id))
        self.conn.commit()

    def delete(self):
        self.conn.close()
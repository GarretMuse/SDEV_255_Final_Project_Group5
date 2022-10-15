import sqlite3
import customer as cust
import furniture as furn

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        
    def fetch(self, table, id, alt_lookup):
        if table == "Customers":
            if id != "":
                self.cur.execute("SELECT * FROM Customers where cust_id = ?", (id,))
            else:
                self.cur.execute("SELECT * FROM Customers where cust_phone = ?", (alt_lookup,))
        if table == "Furniture":
            self.cur.execute("SELECT * FROM Furniture where furn_id = ?", (id,))
        rows = self.cur.fetchone()
        return rows        

    def insert(self, data):
        if isinstance(data, cust.Customer):
            self.cur.execute("INSERT INTO Customers VALUES (NULL, ?, ?, ?, ?)", (data.name, data.phone, data.addr, data.dist))
        if isinstance(data, furn.Furniture):
            self.cur.execute("INSERT INTO Furniture VALUES (NULL, ?, ?, ?)", (data.desc, data.price, data.stock))
        self.conn.commit()

    def remove(self, data):
        if isinstance(data, cust.Customer):
            self.cur.execute("DELETE FROM Customers WHERE cust_id = ?", (data.id))
        if isinstance(data, furn.Furniture):
            self.cur.execute("DELETE FROM Furniture WHERE furn_id = ?", (data.id))

        self.conn.commit()

    def update(self, data):
        if isinstance(data, cust.Customer):
            self.cur.execute("UPDATE Customers SET cust_name = ?, cust_phone = ?, cust_addr = ?, cust_dist = ? WHERE cust_id = ?",
                (data.name, data.phone, data.addr, data.dist, data.id))                
        if isinstance(data, furn.Furniture):
            self.cur.execute("UPDATE Furniture SET furn_desc = ?, furn_price = ?, furn_stock = ? WHERE furn_id = ?",
                (data.desc, data.price, data.stock, data.id))                
        self.conn.commit()

    def delete(self):
        self.conn.close()
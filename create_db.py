import sqlite3

def create_db():
    try:
        con = sqlite3.connect(database='rms.db')
        cur = con.cursor()
        
        # Create course table
        cur.execute("""CREATE TABLE IF NOT EXISTS course (
            cid INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            duration TEXT,
            charges TEXT,
            description TEXT
        )""")
        
        # Create student table
        cur.execute("""CREATE TABLE IF NOT EXISTS student (
            roll INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT,
            gender TEXT,
            dob TEXT,
            contact TEXT,
            admission TEXT,
            course TEXT,
            state TEXT,
            city TEXT,
            pin TEXT,
            address TEXT
        )""")

        # Create result table
        cur.execute("""CREATE TABLE IF NOT EXISTS result (
            rid INTEGER PRIMARY KEY AUTOINCREMENT,
            roll TEXT,
            name TEXT,
            course TEXT,
            marks_ob TEXT,
            full_marks TEXT,
            per TEXT
        )""")
        
        con.commit()
        print("Tables created successfully!")
        
    except Exception as ex:
        print(f"Error: {str(ex)}")
    finally:
        if con:
            con.close()

if __name__ == "__main__":
    create_db()
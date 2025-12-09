from db import get_connection
def company(name):
    conn = get_connection()
    cursor=conn.cursor()
    query = "insert into company (name) values (%s)"
    cursor.execute(query,(name,))
    conn.commit()
    conn.close()
    print("Company Added Success-Fully")

def show():
    conn=get_connection()
    cursor=conn.cursor()
    query="select * from company"
    cursor.execute(query)
    row=cursor.fetchall()
    conn.close()
    
    print("Company")
    for i in row:
        print(i)
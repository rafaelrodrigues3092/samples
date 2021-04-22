import json
import sqlite3

con = sqlite3.connect('/etc/pihole/gravity.db')
adlist_file = "adlist.json"

def main():
    f = open(adlist_file)
    js_list = f.read()
    f.close()

# Create table

    try:
        cur = con.cursor()
        for item in json.loads(js_list):
            q = f"INSERT INTO adlist (address,enabled,comment) VALUES ('{item['address']}',{item['enabled']},'{item['comment']}')"
            cur.execute(q)
        con.commit()
    except Exception as e:
        print("===================== ERROR ===============================================")
        print(str(e))
        con.rollback()
        raise e
    finally:
        con.close()

if __name__ == "__main__":
    # execute only if run as a script
    main()
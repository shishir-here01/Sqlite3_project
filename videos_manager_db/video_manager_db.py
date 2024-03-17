import sqlite3
con = sqlite3.connect("videos.db")
cu = con.cursor()
cu.execute('''
    CREATE TABLE IF NOT EXISTS videos (
           id INTEGER PRIMARY KEY,
           name TEXT NOT NULL,
           time TEXT NOT NULL
    )
''')

def add_videos(name, time):
    cu.execute("INSERT into videos (name, time) VALUES (?, ?)", (name, time))
    con.commit()


def list_videos():
    cu.execute("SELECT * FROM videos")
    for row in cu.fetchall():
        print(row)

def update_videos(vid_id, new_name, new_time):
    cu.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, vid_id))
    con.commit()

def delete_videos(vid_id):
    cu.execute("DELETE FROM videos where id = ?", (vid_id,))
    con.commit()
    


def main(): 
    while True:
        print("\n video manager with sqlite3 db")
        print("1. Add Videos")
        print("2. List Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit")

        choice = input("enter ur choice: ")

        match choice:
            case '1' :
                name = input("give video name: ")
                time = input("enter duration of video: ")
                add_videos(name, time)



            case '2' :
                list_videos()
            case '3' :
                vid_id = input("enter vid id to update: ")
                name = input("give video name: ")
                time = input("enter duration of video: ")


                update_videos(vid_id, name, time)
            case '4' :
                vid_id = input("enter vid id to delete: ")

                delete_videos(vid_id)
            case '5' :
                break
            case _:
                print("invalid choice")

    con.close()

if __name__ == "__main__":
    main()


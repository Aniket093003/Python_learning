import sqlite3

# Connect to database
con = sqlite3.connect("Youtube_videos.db")
cursor = con.cursor()

# Create table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        duration TEXT NOT NULL
    )
''')
con.commit()

# List all videos
def list_videos():
    cursor.execute("SELECT * FROM videos")
    videos = cursor.fetchall()
    if not videos:
        print("No videos found.")
    else:
        print("\n Your Videos:")
        for video in videos:
            print(f"ID: {video[0]} | Name: {video[1]} | Duration: {video[2]}")

# Add new video
def add_videos(name, duration):
    cursor.execute("INSERT INTO videos (name, duration) VALUES (?, ?)", (name, duration))
    con.commit()
    print(" Video added successfully!")

# Update existing video
def update_videos(vid_id, name, duration):
    cursor.execute("UPDATE videos SET name = ?, duration = ? WHERE id = ?", (name, duration, vid_id))
    con.commit()
    print(" Video updated successfully!")

# Delete video
def delete_videos(vid_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (vid_id,))
    con.commit()
    print(" Video deleted successfully!")

# Main program
def main():
    while True:
        print("\n YouTube Manager (SQLite Version)")
        print("1. List videos")
        print("2. Add video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit app")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Enter video name: ")
            duration = input("Enter video duration: ")
            add_videos(name, duration)
        elif choice == "3":
            vid_id = input("Enter video ID to update: ")
            name = input("Enter new video name: ")
            duration = input("Enter new video duration: ")
            update_videos(vid_id, name, duration)
        elif choice == "4":
            vid_id = input("Enter video ID to delete: ")
            delete_videos(vid_id)
        elif choice == "5":
            print("Exiting... ")
            break
        else:
            print(" Invalid input, please try again.")

    con.close()

if __name__ == "__main__":
    main()

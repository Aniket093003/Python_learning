import json
file_name = "youtube.txt"
def load_data():
    try:
        with open(file_name, 'r') as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        return []
    
    
def save_data_helper(videos):
    with open(file_name, 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("*"*50)
    for i , video in enumerate(videos, start=1):
        print(f"{i}, {video['name']} , {video['length']} ")
    print("\n")
    print("*"*50)

def add_video(videos):
    name = input("enter video Name: ")
    length = input("enter video Length: ")
    videos.append({'name': name, 'length': length})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    idx = int(input("enter index you want to update: "))
    if 1 <= idx <= len(videos):
        name = input("enter name of video: ")
        length = input("enter duration of video: ")
        videos[idx-1] = {"name": name , "length": length}
        save_data_helper(videos)


def delete_video(videos):
    list_all_videos(videos)
    idx = int(input("enter index you want to delete: "))
    if 1 <= idx <= len(videos):
        del videos[idx-1]
        save_data_helper(videos)
    else:
        print("invalid video reference")



def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")
        print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")

if __name__ ==  "__main__":
    main() 
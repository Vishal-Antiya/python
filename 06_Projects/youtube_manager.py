import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_helper(videos):
    with open('youtube.txt', 'w') as file:
        return json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("_" *80)
    for index, video in enumerate(videos, start = 1):
            print(f"{index}: {video['name']} Duration: {video['time']}")
    print("\n")
    print("_" *80)

def add_video(videos):
    name = input("Enter the name of the video: ")
    time = input("Enter the duration of the video: ")
    videos.append({'name': name, 'time': time })
    save_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video to be updated: "))
    if 1 <= index <= len(videos):
        name = input("Enter the name of the updated video: ")
        time = input("Enter the duration of the updated video: ")
        videos[index-1] = {'name': name, 'time': time}
        save_helper(videos)
    else:
        print("Invalid Index Provided")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video to be deleted: "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_helper(videos)
    else:
        print("Invalid Index Provided")

def main():
    while True:
        print("\n YOUTUBE MANAGER | Choose any option")
        print("1. List all the videos.")
        print("2. Add a videos.")
        print("3. Update a video.")
        print("4. Delete all the videos.")
        print("5. Exit.")
        choice = int(input("Enter a choice: "))
        videos = load_data()
        match choice:
            case 1:
                list_all_videos(videos)
            case 2:
                add_video(videos)
            case 3:
                update_video(videos)
            case 4:
                delete_video(videos)
            case 5:
                break
            case _:
                print("Invalid choice selected")
        # print(videos)

if __name__ == "__main__":
    main()
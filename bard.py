from bardapi import Bard
import os
import sys
import threading
import time

# Visit https://bard.google.com/
# F12 for console
# Session: Application → Cookies → Copy the value of  __Secure-1PSID cookie.
os.environ['_BARD_API_KEY']="PASTE_YOUR_KEY_HERE"

print("Bard is here! Say \"exit\" to quit.\n")

def get_answer_with_loading(line):
    answer = None

    def request_bard():
        nonlocal answer
        answer = Bard().get_answer(line)['content']

    loading_thread = threading.Thread(target=request_bard)
    loading_thread.start()

    animation = "|/-\\"
    idx = 0

    while loading_thread.is_alive():
        print(f"~Thinking... {animation[idx % len(animation)]}", end="\r", flush=True)
        idx += 1
        time.sleep(0.1)

    loading_thread.join()
    print("\r" + " " * 20 + "\r" + answer + "\n")

while True:
    line = input()

    if line == "exit":
        break

    get_answer_with_loading(line)

print("Bye!")

sys.exit()

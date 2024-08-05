import time

attempt = 0
max_retries = 5
wait_time = 1

while attempt < max_retries:
    print("Attempt:-", attempt +1, "Wait time:", wait_time, "sec" )
    time.sleep(wait_time)
    wait_time = 2* wait_time
    attempt = attempt + 1

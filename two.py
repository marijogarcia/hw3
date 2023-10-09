def calc_time(start_time, hours):
    time = (start_time + hours) % 24
    return time

def main():
    start_time = int(input("Input the start time: "))
    hours = int(input("How many hours: "))
    now_time = calc_time(start_time, hours)
    print("It will be %d" % now_time)
    return

main()
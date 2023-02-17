def main():
    time1 = input().strip()
    time2 = input().strip()
    time_list1 = time1.split()
    time_list2 = time2.split()
    hours1 = int(time_list1[0])
    minutes1 = int(time_list1[1])
    seconds1 = int(time_list1[2])
    hours2 = int(time_list2[0])
    minutes2 = int(time_list2[1])
    seconds2 = int(time_list2[2])
    total_seconds1 = hours1 * 3600 + minutes1 * 60 + seconds1
    total_seconds2 = hours2 * 3600 + minutes2 * 60 + seconds2
    if total_seconds2 < total_seconds1:
        print(-1)
    else:
        print(total_seconds2 - total_seconds1)

if __name__ == '__main__':
    main()

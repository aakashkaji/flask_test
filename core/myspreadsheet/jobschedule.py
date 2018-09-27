import time
import datetime
import random


def schedule():
    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    minutes = random.randint(2, 10)
    time.sleep(60 * minutes)
    # print("=", time_stamp)
    return time_stamp


########## my time calculator


def time_scheduleing(tls=11):

    time_ls = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


    if tls <= 12:

        n = random.randint(0, tls-2)
        rv = time_ls[n]
        return rv
    else:
        n = random.randint(0, 13)
        rv = time_ls[n]

        return rv


# eta = datetime.datetime.utcnow()
# time_stamp = datetime.datetime.now()
# avg_ls = []
#
# for i in range(1, 15):
#     minutes = time_scheduleing(12)
#     avg_ls.append(minutes)
#     time_stamp = time_stamp + datetime.timedelta(minutes=minutes)
#     print(time_stamp.strftime('%Y-%m-%d %H:%M'), '----',minutes)
# av = sum(avg_ls)/len(avg_ls)
# print(sum(avg_ls), 'av=', av)
# print(i)
# print(i*av)
# print(avg_ls)
import time

one = "2013-10-10 23:40:00"

two = time.strptime(one, "%Y-%m-%d %H:%M:%S")
# [out]: time.struct_time(tm_year=2013, tm_mon=10, tm_mday=10, tm_hour=23, tm_min=40, tm_sec=0, tm_wday=3, tm_yday=283, tm_isdst=-1)

three = time.mktime(two)
# [out]: 1381419600.0

four = time.strftime("%Y/%m/%d %H:%M:%S", two)
# [out]: '2013/10/10 23:40:00'

time.time()
# Out[43]: 1532354577.355712

time.localtime(time.time())
# Out[45]: time.struct_time(tm_year=2018, tm_mon=7, tm_mday=23, tm_hour=22, tm_min=3, tm_sec=42, tm_wday=0, tm_yday=204, tm_isdst=0)

time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
# Out[48]: '2018-07-23 22:08:31'

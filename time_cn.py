def parse_time(date):
    if re.match('刚刚', date):
        date = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
    if re.match('\d+分钟前', date):
        minute = re.match('(\d+)', date).group(1)
        date = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time() - float(minute) * 60))
    if re.match('\d+小时前', date):
        hour = re.match('(\d+)', date).group(1)
        date = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time() - float(hour) * 60 * 60))
    if re.match('昨天.*', date):
        date = re.match('昨天(.*)', date).group(1).strip()
        date = time.strftime('%Y-%m-%d', time.localtime(time.time() - 24 * 60 * 60)) + ' ' + date
    if re.match('\d{2}-\d{2}', date):
        date = time.strftime('%Y-', time.localtime()) + date + ' 00:00'
    return date
    
parse_time('刚刚')
parse_time('3分钟前')
parse_time('5小时前')
parse_time('昨天 14:23')
parse_time('06-07')

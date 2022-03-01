from datetime import datetime, timedelta
def diff (data1, data2):
    timedelta = data2 - data1
    return timedelta.days * 24 * 3600 + timedelta.seconds
data1 = datetime.today()-timedelta(days=1)
data2 = datetime.today()
print(diff(data1, data2))
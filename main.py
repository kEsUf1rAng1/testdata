import random
import time
import sys
from datetime import datetime, timedelta


def gen_datetime(min_year=2012, max_year=datetime.now().year):
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random.random()


def gen_int(min=0, max=99):
    return random.randint(min, max)


def gen_string(len=3):
    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    str = ""
    for i in range(random.randint(1, len)):
        str = str + alphabets[random.randint(0, 25)]
    return str


def gen_date(start="2012-01-01", end="2021-12-31", time_format="%Y-%m-%d", prop=random.random()):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(time_format, time.localtime(ptime))


def gen_decimal(min=100, max=9999):
    return str(random.randrange(min, max)) + "." + str(random.randrange(10, 99))


def gen_row(data_type, type_list):
    row_val = ""
    for i in range(len(type_list)):
        col_type = type_list[i].lower().strip()
        if col_type == "string":
            col_val = gen_string()
        elif col_type == "int" or col_type == "integer":
            col_val = str(gen_int())
        elif col_type == "float" or col_type == "decimal":
            col_val = str(gen_decimal())
        elif col_type == "date":
            col_val = str(gen_date())
        elif col_type == "timestamp":
            col_val = str(gen_datetime())
        else:
            col_val = gen_string()

        if data_type == "sql" and (col_type == "string" or col_type == "date" or col_type == "timestamp"):
            col_val = "'" + col_val + "'"

        if row_val == "":
            row_val = col_val
        else:
            row_val = row_val + "," + col_val

    return row_val


if __name__ == '__main__':
    data_type = sys.argv[1]
    row_count = int(sys.argv[2])
    type_list = sys.argv[3].split(",")

    f = open("demofile2.txt", "a")
    for i in range(row_count):
        f.write(gen_row(data_type, type_list) + "\n")
    f.close()

import random
import time
import sys
from datetime import datetime, timedelta


def gen_datetime_3(min_year=2012, max_year=datetime.now().year):
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random.random()


def gen_datetime_2_7(min_year=2012, max_year=datetime.now().year):
    inicio = datetime(2017, 1, 30)
    final = datetime(2017, 5, 28)
    random_date = inicio + timedelta(seconds=int((final - inicio).total_seconds() * random.random()))
    return str(random_date) + str(round(random.random(), 6))


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


def gen_decimal(precision):
    min_prec = precision - 1
    return str(random.randrange(100, 9999)) + "." + str(random.randrange(10 ** min_prec, 10 ** precision - 1))


def gen_row(data_type, type_list):
    # "date,decimal(1),decimal(10,2),char(1),varchar(3)"
    row_val = ""
    for i in range(len(type_list)):
        col_type = type_list[i].lower().strip()
        if col_type.find("string") > -1 or col_type.find("char") > -1:
            if col_type.find("(") > -1:
                length = int(col_type[col_type.find("(") + 1:col_type.find(")")])
                col_val = gen_string(len=length)
            else:
                col_val = gen_string()
        elif col_type.find("int") > -1 or col_type.find("integer") > -1:
            col_val = str(gen_int())
        elif col_type.find("float") > -1 or col_type.find("decimal") > -1:
            if col_type.find("(") > -1:
                len_details = col_type[col_type.find("(") + 1:col_type.find(")")].split(",")
                if len(len_details) == 1:
                    prec = int(len_details[0])
                else:
                    prec = int(len_details[1])
                col_val = str(gen_decimal(precision=prec))
            else:
                col_val = str(gen_decimal())
        elif col_type.find("date") > -1:
            col_val = str(gen_date())
        elif col_type.find("timestamp") > -1:
            col_val = str(gen_datetime_2_7())
        else:
            col_val = gen_string()

        if data_type == "sql" and (
                col_type.find("string") > -1 or col_type.find("char") > -1 or col_type.find(
            "date") > -1 or col_type.find("timestamp") > -1):
            col_val = "'" + col_val + "'"

        if row_val == "":
            row_val = col_val
        else:
            row_val = row_val + "," + col_val

    if data_type == "sql":
        row_val = "INSERT INTO DBNAME.TABLENAME VALUES (" + row_val + ");"

    return row_val


if __name__ == '__main__':
    data_type = sys.argv[1]
    row_count = int(sys.argv[2])
    file_name = sys.argv[3]
    # type_list = sys.argv[4].split(",")
    type_list = "date|decimal(2)|decimal(10,3)|char(1)|varchar(3)".split("|")
    print(gen_row(data_type, type_list))

    # f = open(file_name, "a")
    # for i in range(row_count):
    #    f.write(gen_row(data_type, type_list) + "\n")
    # f.close()

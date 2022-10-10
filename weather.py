import json
import calendar

def read_data(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return{}

def write_data(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)

def max_temperature(data, date):
    x = 0
    for key in data:
        if date == key[0:8]:
            if data[key]['t'] > x:
                x = data[key]['t']
    return x

def min_temperature(data, date):
    x = 9999
    for key in data:
        if date == key[0:8]:
            if data[key]['t'] < x:
                x = data[key]['t']
    return x

def max_humidity(data, date):
    x = 0
    for key in data:
        if date == key[0:8]:
            if data[key]['h'] > x:
                x = data[key]['h']
    return x

def min_humidity(data, date):
    x = 9999
    for key in data:
        if date == key[0:8]:
            if data[key]['h'] < x:
                x = data[key]['h']
    return x

def tot_rain(data, date):
    total = 0.0
    for key in data:
        if date == key[0:8]:
            total += data[key]['r']
    return total

def report_daily(data, date):
    display = "========================= DAILY REPORT ========================\n"
    display += "Date                      Time  Temperature  Humidity  Rainfall\n"
    display += "====================  ========  ===========  ========  ========\n"
    for key in data:
        if date == key[0:8]:
            m = calendar.month_name[int(date[4:6])] + " " + str(int(date[6:8])) + ", " + str(int(date[0:4]))
            tm = key[8:10] + ":" + key[10:12] + ":" + key[12:14]
            t = date[key]['t']
            h = date[key]['h']
            r = date[key]['r']

            display += f'{m:22}{tm:8}{t:13}{h:10}{r:10.2f}' + '\n'
    return display

def report_historical(data):
    display = "============================== HISTORICAL REPORT ===========================\n"
    display += "			              Minimum      Maximum   Minumum   Maximum     Total\n"
    display += "Date                  Temperature  Temperature  Humidity  Humidity  Rainfall\n"
    display += "====================  ===========  ===========  ========  ========  ========\n"
    h = ''
    for key in data:
        if h == key[0:8]:
            continue
        else:
            h == key[0:8]
            m = calendar.month_name[int(h[4:6])] + " " + str(int(h[6:8])) + "," + str(int(h[0:4]))
            min_temp = min_temperature(data, h)
            max_temp = max_temperature(data, h)
            min_hum = min_humidity(data, h)
            max_hum = max_humidity(data, h)
            rain = tot_rain(data, h)

            display += f'{m:22}{min_temp:13}{max_temp:13}{min_hum:10}{max_hum:10}{rain:20:2f}' + '\n'
    return display
import csv
from datetime import datetime 


DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    convertiso = datetime.fromisoformat(iso_string)
    isoformat = convertiso.strftime("%A %d %B %Y")
    return isoformat


def convert_f_to_c(temp_in_farenheit):
    convert = ((float(temp_in_farenheit) - 32) * (5/9))
    format_convert = "{:.1f}".format(convert) 
    return float(format_convert)


def calculate_mean(temperatures):
    value = [float(a) for a in temperatures]
    mean = ((sum(value)) / len(value))
    return mean


def load_data_from_csv(csv_file):
    with open((csv_file)) as my_file:
        list = []
        csv_reader = csv.reader(my_file)
        next(csv_reader)
        for line in csv_reader:
            if len(line) == 3:
                line[1]= int(line[1])
                line[2]= int(line[2])
                list.append(line)
        return list


def find_min(weather_data):
    if len(weather_data) > 1:
            for num in range(0, len(weather_data)):
                weather_data[num] = float(weather_data[num])
            min_value = (min(weather_data))
            for i in range(len(weather_data)):
                if weather_data[i] == min_value:
                    index = i
            return (min_value, index)
    else:
        return ()


def find_max(weather_data):
        if len(weather_data) > 1:
            for num in range(0, len(weather_data)):
                weather_data[num] = float(weather_data[num])
            max_value = (max(weather_data))
            for i in range(len(weather_data)):
                if weather_data[i] == max_value:
                    index = i
            return (max_value, index)
        else:
            return ()


def generate_summary(weather_data):
    length_list = len(weather_data)
    low_temps = []
    high_temps = []
    for item in weather_data:
        low_temps.append(item[1])
        high_temps.append(item[2])
    min_temp, min_index = (find_min(low_temps))
    max_temp, max_index = (find_max(high_temps))
    mean_low = (calculate_mean(low_temps))
    mean_high = (calculate_mean(high_temps))
    return (f"{length_list} Day Overview\n  The lowest temperature will be {convert_f_to_c(min_temp)}{DEGREE_SYBMOL}, and will occur on {(convert_date(weather_data[min_index][0]))}.\n  The highest temperature will be {convert_f_to_c(max_temp)}{DEGREE_SYBMOL}, and will occur on {(convert_date(weather_data[max_index][0]))}.\n  The average low this week is {convert_f_to_c(mean_low)}{DEGREE_SYBMOL}.\n  The average high this week is {convert_f_to_c(mean_high)}{DEGREE_SYBMOL}.\n")


def generate_daily_summary(weather_data):
    daily_summary =[]
    for item in weather_data:
            day, min, max = item
            daily_summary.append(f"---- {convert_date(day)} ----\n  Minimum Temperature: {convert_f_to_c(min)}{DEGREE_SYBMOL}\n  Maximum Temperature: {convert_f_to_c(max)}{DEGREE_SYBMOL}\n\n")
    return ''.join(daily_summary)

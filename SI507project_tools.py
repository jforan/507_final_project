## i don't use these


from statistics import mean

def average_station(database):
    list_for_average = []
    for i in list_of_lists:
        list_for_average.append(i[2])

    return mean(list_for_average)


def country_station_average(list_of_lists):
    dict = {}
    for i in list_of_lists:
        if i[1] in dict:
            dict[i] += 1
        else:
            dict[i] = 1

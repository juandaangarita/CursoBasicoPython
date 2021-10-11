# list = ['Hi', 3, 4.5, True, 8, False]
# print(list)
# list.append(1)
# print(list)
# list.pop(3)
# print(list)
# print(list[2])

# for element in list:
#     print(element)

# print(list[::-1])
# print(list[1:3])

# numbers = [1, 2, 3, 4, 5]
# numbers2 = [6, 7, 8, 9]
# final_list = numbers + numbers2
# print(final_list)

# # Tuples
# tuple = (1, 2, 3, 4, 5)

def run():
    dictionary = {
        'key1':1,
        'key2':2,
        'key3':3,

    }
    # print(dictionary['key1'])
    # print(dictionary['key2'])
    # print(dictionary['key3'])
    country_population = {
        'Argentina': 44938712,
        'Brasil': 210147125,
        'Colombia': 50372424, 
    }

    # print(country_population['Colombia'])

    for country in country_population.keys():
        print(country)
    
    for population in country_population.values():
        print(population)

    for country, population in country_population.items():
        print(country + ' has ' + str(population) + ' people')

if __name__ == '__main__':
    run()
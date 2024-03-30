addList = 'yes'

travel_log = [
         {
          "country": "France",
          "visits": 12,
          "cities": ["Paris", "Lille", "Dijon"]
         }
     ]

while addList == 'yes':
    country = input('Country name: ') 
    visits = int(input('Number of visits: ')) 
    list_of_cities = eval(input('List of cities visited. eg: ["Sydney", "Melbourne"] >> ')) 


    def add_new_country(country, visits, list_of_cities):
       travel_log.append({
        'country': country,
        'visits': visits,
        'cities': list_of_cities
        })
       return travel_log

    data = add_new_country(country, visits, list_of_cities)
    print(data)
    addList = input('Do you want to add more list? yes or no >> ')

